import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Subtitle
old_sub = r'<p class="hero-subtitle mx-auto" style="font-size: 1.6rem; margin-bottom: 32px; max-width: 800px; line-height: 1.6;">Để Từ Người Xem Trở Thành Khách Hàng Là Cả Một Hành Trình,<br>Họ Cần Được Bạn Dẫn Đường.</p>'
# Add text-wrap: balance to fix widow words naturally
new_sub = '<p class="hero-subtitle mx-auto" style="font-size: 1.6rem; margin-bottom: 32px; max-width: 800px; line-height: 1.6; text-wrap: balance;">Để Từ Người Xem Trở Thành Khách Hàng Là Cả Một Hành Trình,<br>Họ Cần Được Bạn Dẫn Đường.</p>'
content = re.sub(old_sub, new_sub, content)

# 2. Update Button Text
old_btn = r'Khám Phá Hành Trình Dẫn Dắt Từ Khán Giả Thành Khách Trả Phí <svg'
new_btn = 'Khám Phá Hành Trình <svg'
content = re.sub(old_btn, new_btn, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
