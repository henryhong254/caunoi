with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start = c.find('<div id="abs-bar">')
end = c.find('</div>', c.find('</a>', start)) + 6
print(c[start:end])
