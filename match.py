import re

# 从文件中读取文本，保留换行符
with open("my_file.txt", "r", encoding="utf-8") as file:
    stored_text = file.read()
# 使用集合来存储已提取的股票代码
stock_codes = set()
pattern = r"[sh|sz]\.(\d+)"
for line in stored_text.split('\n'):
    match = re.search(pattern, line)
    if match:
        stock_code = match.group(1)
        stock_codes.add(stock_code)

# 输出去重的股票代码
for code in stock_codes:
    print(code)