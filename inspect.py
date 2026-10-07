with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the desktop vt-center definition with width 90px and add font-size override there
old = """.vt-center {
      width: 90px; height: 90px;
      background: var(--c-bg-dark);
      border: 3px solid rgba(255,255,255,0.1);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      text-align: center;
      font-weight: 700;
      color: rgba(255,255,255,0.2);
      font-size: 1.2rem;
      z-index: 10;
      box-shadow: 0 0 0 6px var(--c-bg-dark);
      transition: all 0.4s ease;
    }"""

# We need to find the actual content 
idx = content.find('width: 90px; height: 90px;')
snippet = content[idx-30:idx+400]
print("DESKTOP SNIPPET:")
print(repr(snippet))
