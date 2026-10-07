import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Add text-wrap: balance to the section title
content = content.replace('<h2 class="section-title">', '<h2 class="section-title" style="text-wrap: balance;">')

# Fix 2: Adjust vt-center font-size and line-height for mobile
old_vt_center = r'\.vt-center \{\s*font-size: 0\.75rem !important;\s*line-height: 1\.1 !important;\s*padding: 5px !important;\s*\}'
new_vt_center = """.vt-center {
        font-size: 0.65rem !important;
        line-height: 1.1 !important;
        padding: 0 !important;
      }"""
content = re.sub(old_vt_center, new_vt_center, content)

old_start_dot = r'\.vt-start-dot \{\s*top: 0px !important;\s*width: 60px !important;\s*height: 60px !important;\s*font-size: 0\.8rem !important;\s*\}'
new_start_dot = """.vt-start-dot {
        top: 0px !important;
        width: 60px !important;
        height: 60px !important;
        font-size: 0.65rem !important;
      }"""
content = re.sub(old_start_dot, new_start_dot, content)

# Fix 3: Image always on top on mobile
# We will find all <div class="vt-col ..."> that contain <div class="vt-img-card"> and add col-img class
# And those with <div class="vt-text"> or similar, add col-text class

# Since we know the structure, we can just use regex to add col-img to the parent of .vt-img-card
# <div class="vt-col vt-right">
#   <div class="vt-img-card">

content = re.sub(r'(<div class="vt-col[^>]*>)\s*(<div class="vt-img-card">)', r'\1\n          \2', content) # normalize whitespace
content = re.sub(r'<div class="vt-col (vt-left|vt-right)">\s*<div class="vt-img-card">', r'<div class="vt-col \1 col-img">\n          <div class="vt-img-card">', content)

# Now add mobile CSS for order
order_css = """
      /* Force Image to top on mobile */
      .col-img { order: 1 !important; }
      .vt-text { order: 2 !important; }
"""
content = content.replace('/* Fix the trophy dot */', order_css + '\n      /* Fix the trophy dot */')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
