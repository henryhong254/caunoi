with open('style.css', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('.abs-bar .btn-primary-small', '#abs-bar .btn-primary-small')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(c)
