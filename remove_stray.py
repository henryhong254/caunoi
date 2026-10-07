with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Still 2 stray 0.65rem blocks (#2 and #4) left. Remove them.
stray = """.vt-center {
        font-size: 0.65rem !important;
        line-height: 1.1 !important;
        padding: 0 !important;
      }

      """

content = content.replace(stray, '      ')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done - removed stray blocks")
