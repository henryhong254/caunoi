import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = r'Xây Dựng 3 Trạm Chuyển Đổi Từ Khán Giả Thành <br> Khách Trả Phí'
new_str = r'Để Từ Người Xem Trở Thành Khách Hàng Là Cả Một Hành Trình Dài,<br>Họ Cần Được Bạn Dẫn Dắt.'

content = re.sub(old_str, new_str, content)

# just in case it was formatted slightly differently
old_str2 = r'Xây Dựng 3 Trạm Chuyển Đổi Từ Khán Giả Thành\s*<br>\s*Khách Trả Phí'
content = re.sub(old_str2, new_str, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
