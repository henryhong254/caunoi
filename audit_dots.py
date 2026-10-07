with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find ALL mobile vt-center definitions and print them
idx = 0
count = 0
while True:
    idx = content.find('.vt-center {', idx)
    if idx == -1:
        break
    count += 1
    print(f"=== #{count} at pos {idx} ===")
    end = content.find('}', idx)
    print(repr(content[idx:end+1]))
    print()
    idx += 1
