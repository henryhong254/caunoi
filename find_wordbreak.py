with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find quiz section title
idx = c.find('class="quiz-section"')
if idx == -1:
    idx = c.find('id="quiz"')
print(f"Quiz at {idx}")
print(c[idx:idx+500].encode('utf-8'))

# Find word-break in CSS
wb_idx = c.find('word-break')
while wb_idx != -1:
    print(f"\n--- word-break at {wb_idx} ---")
    print(c[max(0,wb_idx-50):wb_idx+80].encode('utf-8'))
    wb_idx = c.find('word-break', wb_idx+1)

# Also check style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()
wb_idx = css.find('word-break')
while wb_idx != -1:
    print(f"\n--- CSS word-break at {wb_idx} ---")
    print(css[max(0,wb_idx-80):wb_idx+80].encode('utf-8'))
    wb_idx = css.find('word-break', wb_idx+1)
