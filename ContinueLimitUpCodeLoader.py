import baostock as bs
import pandas as pd


def get_continuous_limit_up_stocks(stock_code, stock_name, days, start_date, end_date):

    # 获取历史K线数据
    rs = bs.query_history_k_data_plus(stock_code, "date,code,close,high,pctChg", start_date, end_date, frequency="d",
                                      adjustflag="2")
    data_list = []
    while rs.error_code == '0' and rs.next():
        data_list.append(rs.get_row_data())
    df = pd.DataFrame(data_list, columns=rs.fields)

    # 将涨幅数据转换为浮点数，并处理可能的空字符串
    df['pctChg'] = pd.to_numeric(df['pctChg'], errors='coerce')

    # 添加两个条件列，表示当天是否涨停且涨幅是否超过阈值
    df['当天涨停'] = (df['close'] == df['high'])
    df['涨幅超过阈值'] = (df['pctChg'] > 9.8)

    # 寻找符合条件的日期
    condition_met = df['当天涨停'] & df['涨幅超过阈值']
    dates = df.loc[condition_met, 'date']
    if not dates.empty and dates.size >= days:
        print(f"股票 {stock_code} ({stock_name}) 近 {days} 天连续涨停的日期：{list(dates)}")


