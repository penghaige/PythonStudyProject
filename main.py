import AllStockMarketCodeLoader as allStockLoader
import JudgeStockLE5DayMA as judgeStockHelper
import baostock as bs
import datetime

# 登陆系统
lg = bs.login()

start_date = (datetime.datetime.now() - datetime.timedelta(days=20)).strftime('%Y-%m-%d')
end_date = datetime.datetime.now().strftime('%Y-%m-%d')
all_stock_list = allStockLoader.load()
for index, stock in enumerate(all_stock_list):
    code = stock[0]
    # print(f'第{index}只， 股票代码是: {code}')
    if code.startswith('sh') or code.startswith('sz'):
        judgeStockHelper.judge3(stock[0], start_date, end_date, 7)
        # print(stock)

# 登出系统
bs.logout()
