from gne import GeneralNewsExtractor

# 读取文件
with open('data/3UC6nkQ_ydT9Fl-Il0SM2A.html', 'rt') as f:
    data = f.read()

extractor = GeneralNewsExtractor()
html = data
result = extractor.extract(html)
print(result)