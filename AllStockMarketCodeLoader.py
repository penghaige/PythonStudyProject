import baostock as bs
import pandas as pd


def load():
    # 调用query_shhk_stocks接口获取所有股票代码
    rs = bs.query_all_stock()
    data_list = []
    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
    return data_list


def test():
    # 登录baostock
    lg = bs.login()

    data_list = load()
    print(data_list)

    # 将数据转换为DataFrame格式
    # df = pd.DataFrame(data_list, columns=rs.fields)

    # 将数据导出到excel
    # df.to_excel('G:/temp/python/output/沪港通股票代码.xlsx', index=False)

    # 登出baostock
    bs.logout()
