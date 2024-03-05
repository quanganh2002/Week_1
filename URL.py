import re

def check_url(text):
    patterm = '^(http|https):\/\/(www\.)?[a-zA-Z0-9]+(\.[a-z]{2,6})[^\s]*$'
    return re.match(patterm, text)

URLs = [
    'https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=mega-menu',
    'http://www.example.com',
    'ftp://invalid-url.com'
]

for i in URLs:
    if check_url(i):
        print(f"{i} hợp lệ")
    else:
        print(f"{i} không hợp lệ")