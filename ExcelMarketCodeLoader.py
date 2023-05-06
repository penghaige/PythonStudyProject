import pandas as pd


def load():
    # 读取Excel文件
    df = pd.read_excel('沪港通股票代码.xlsx', sheet_name='Sheet1')

    # 转换为数组对象
    data_array = df.values
    return data_array
