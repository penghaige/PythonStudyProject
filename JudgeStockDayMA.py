import baostock as bs
import pandas as pd
import datetime


def judge(mode, code, start_date, end_date, days, abs_pctChg):
    # 获取K线数据
    rs = bs.query_history_k_data_plus(code,
                                      "date,close,tradestatus,amount,volume,pctChg",
                                      start_date=start_date,
                                      end_date=end_date,
                                      frequency="d",
                                      adjustflag="3")
    data_list = []
    # 是否未停牌
    is_normal_trade_status = True
    # 是否每天涨跌幅大于指定值
    is_large_than_abs_pct_chg = True
    # 是否平均成交数量大于指定值
    is_large_than_average_volume = True
    # 总成交数量(股)
    total_volume = 0
    # 平均成交数量(股)
    average_volume = 0
    len = rs.data.__len__()
    while (rs.error_code == '0') & rs.next():
        row_data = rs.get_row_data()
        data_list.append(row_data)
        if row_data[4] != '':
            total_volume = total_volume + float(row_data[4])

        if row_data[2] != '1':
            is_normal_trade_status = False
        pct_chg = row_data[5]
        if abs_pctChg is not None and pct_chg is not None and pct_chg != '' and abs(float(pct_chg)) < abs_pctChg:
            is_large_than_abs_pct_chg = False

    if len > 0:
        average_volume = total_volume / len


    if is_normal_trade_status is False or is_large_than_abs_pct_chg is False:
        return False

    df = pd.DataFrame(data_list, columns=rs.fields)
    if 3 == mode:
        # 计算3日线和最近几天的收盘价和成交数量
        df['close'] = df['close'].astype(float)
        df['volume'] = df['volume'].astype(float)
        df['ma3'] = df['close'].rolling(window=3).mean()
        last_close = df.iloc[-days:]['close']
        last_ma3 = df.iloc[-days:]['ma3']
        last_volume = df.iloc[-3:]['volume']
        for val in last_volume.values:
            if val < average_volume:
                is_large_than_average_volume = False
                break

        # 判断是否符合条件
        if is_large_than_average_volume and all(last_close >= last_ma3):
            print(f'{code}, 最近{days}天收盘价都不低于3日线')
            return True
        else:
            return False
    elif 5 == mode:
        # 计算5日线和最近一周的收盘价
        df['close'] = df['close'].astype(float)
        df['ma5'] = df['close'].rolling(window=5).mean()
        last_close = df.iloc[-days:]['close']
        last_ma5 = df.iloc[-days:]['ma5']
        # 判断是否符合条件
        if all(last_close >= last_ma5):
            print(f'{code}, 最近{days}天收盘价都不低于5日线')
            return True
        else:
            return False
    else:
        return False


def test():
    # 登录baostock
    lg = bs.login()
    # 设置股票代码和日期范围
    code = 'sh.601360'
    # start_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    # end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    start_date = '2023-03-06'
    end_date = '2023-03-27'
    judge(5, code, start_date, end_date, 5)
    # 登出baostock
    bs.logout()

# test()
