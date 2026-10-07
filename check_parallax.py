with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Also fix parallax-solution - ensure no dark padding bleeds through
old = '.parallax-solution {'
if old in content:
    idx = content.find(old)
    print(content[idx:idx+300])
