import AllStockMarketCodeLoader as allStockLoader
import ExcelMarketCodeLoader as excelStockLoader
import JudgeStockDayMA as judgeStockHelper
import ContinueLimitUpCodeLoader as continueLimitUpCodeLoader;
import baostock as bs
import datetime

# 登陆系统
lg = bs.login()


start_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
end_date = datetime.datetime.now().strftime('%Y-%m-%d')
# all_stock_list = allStockLoader.load()
all_stock_list = excelStockLoader.load()
for index, stock in enumerate(all_stock_list):
    code = stock[0]
    name = stock[2]
    if (code.startswith('sh') and code.startswith('sh.688') is False) or code.startswith('sz'):
        # result = judgeStockHelper.judge(3, stock[0], start_date, end_date, 3, 1, None, None)
        # if result:
        #     print(f'第{index}只， 股票代码是: {code}, 股票名称是: {name}')
        continueLimitUpCodeLoader.get_continuous_limit_up_stocks(code, name, 2, start_date, end_date)
#continueLimitUpCodeLoader.get_continuous_limit_up_stocks('sh.603729', '龙韵股份', 4, start_date, end_date)
# 登出系统
bs.logout()
