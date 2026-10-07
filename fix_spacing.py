with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the mobile vt-row CSS and increase margin-bottom
old = """        .vt-row {
        flex-direction: column !important;
        align-items: flex-start !important;
        text-align: left !important;
        padding-left: 70px !important;
        position: relative !important;
        margin-bottom: 50px !important;
      }"""

new = """        .vt-row {
        flex-direction: column !important;
        align-items: flex-start !important;
        text-align: left !important;
        padding-left: 70px !important;
        position: relative !important;
        margin-bottom: 80px !important;
        padding-bottom: 20px !important;
      }"""

content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
