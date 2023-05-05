import chardet
with open('G:\\temp\\python\\output\\20230428不低于3日线代码.txt', 'rb') as f:
    # 读取整个文本
    rawdata = f.read()
    result = chardet.detect(rawdata)
    text = rawdata.decode(result['encoding'])

    # 按行切分文本，并截取每行:后面的文本
    lines = text.split('\n')
    for line in lines:
        # colon_index = line.find(':')
        # 查找每行最后一个字符位置
        colon_index = line.rfind(':')
        if colon_index >= 0:
            print(line[colon_index+1:])
