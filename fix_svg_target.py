import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the mobile CSS
content = content.replace('#vt-svg-container {', '.vt-svg-track {\n        left: 0 !important;\n        transform: translateX(-40px) !important;\n      }\n      #vt-svg-container {')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
