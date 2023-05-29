capital = 140000  # 现有资金，单位为元
init_capital = 340000  # 初始资金，单位为元
position = 0.5  # 仓位为现有资金的一半
profit_per_day = 1  # 每天盈利一个点
trading_days_per_month = 20  # 一个月平均交易日为20天
months = 0  # 计数器

while capital < init_capital:
    for i in range(trading_days_per_month):
        profit_per_day_amount = capital * position * profit_per_day / 100
        capital += profit_per_day_amount
    months += 1

print("使用现有资金 %.2f 仓位交易，每天盈利 %.2f 个点，需要 %d 个月才能回本。" % (position, profit_per_day, months))
