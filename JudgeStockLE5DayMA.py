import baostock as bs
import pandas as pd
import datetime


def judge5(code, start_date, end_date, days):
    # 获取K线数据
    rs = bs.query_history_k_data_plus(code,
                                      "date,close",
                                      start_date=start_date,
                                      end_date=end_date,
                                      frequency="d",
                                      adjustflag="3")
    data_list = []
    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
    df = pd.DataFrame(data_list, columns=rs.fields)
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


def judge3(code, start_date, end_date, days, abs_pctChg):
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
    is_large_than_abs_pct_chg = True
    while (rs.error_code == '0') & rs.next():
        row_data = rs.get_row_data()
        data_list.append(row_data)

        if row_data[2] != '1':
            is_normal_trade_status = False
        pct_chg = row_data[5]
        if abs_pctChg is not None and pct_chg is not None and pct_chg != '' and abs(float(pct_chg)) < abs_pctChg:
            is_large_than_abs_pct_chg = False

    if is_normal_trade_status is False or is_large_than_abs_pct_chg is False:
        return False

    df = pd.DataFrame(data_list, columns=rs.fields)
    # 计算3日线和最近几天的收盘价
    df['close'] = df['close'].astype(float)
    df['ma3'] = df['close'].rolling(window=3).mean()
    last_close = df.iloc[-days:]['close']
    last_ma3 = df.iloc[-days:]['ma3']
    # 判断是否符合条件
    if all(last_close >= last_ma3):
        print(f'{code}, 最近{days}天收盘价都不低于3日线')
        return True
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
    judge5(code, start_date, end_date, 5)
    # 登出baostock
    bs.logout()

# test()
