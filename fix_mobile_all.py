import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update .vt-center and #vt-car mobile CSS
mobile_css_add = """
      /* Fix Car Position */
      #vt-car {
        left: 40px !important;
      }

      /* Fix Dot Text Overflow */
      .vt-center {
        font-size: 0.75rem !important;
        line-height: 1.1 !important;
        padding: 5px !important;
      }
"""
content = content.replace('.vt-center {', mobile_css_add + '\n      .vt-center {')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Update abs-bar mobile CSS
old_abs = r'\.abs-content \{ flex-direction: column; text-align: center; gap: 12px; \}'
new_abs = """
      .abs-content { flex-direction: row; text-align: left; gap: 10px; padding: 0 10px; justify-content: space-between; }
      #abs-bar { padding: 12px 0; }
      .abs-tag { display: none; }
      .abs-text { font-size: 0.8rem; line-height: 1.3; }
      .abs-bar .btn-primary-small { padding: 8px 12px; font-size: 0.8rem; white-space: nowrap; flex-shrink: 0; }
"""
css_content = re.sub(old_abs, new_abs, css_content)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
