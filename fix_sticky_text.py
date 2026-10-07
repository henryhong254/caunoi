import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the text inside #abs-bar
old_text = r'Xây Dựng 3 Trạm Chuyển Đổi Từ Khán Giả Thành Khách Trả Phí'
new_text = 'Xây Dựng 3 Trạm Chuyển Đổi<span class="desktop-only"> Từ Khán Giả Thành Khách Trả Phí</span>'

content = re.sub(old_text, new_text, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add desktop-only class to mobile media query
mobile_css = """
      .desktop-only { display: none !important; }
"""
css_content = css_content.replace('.abs-tag { display: none; }', '.abs-tag { display: none; }\n      .desktop-only { display: none !important; }')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
