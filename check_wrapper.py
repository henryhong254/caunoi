with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find the full timeline section that wraps vt-wrap
# to see if it has a dark background-color that bleeds into parallax
idx = c.find('id="timeline"')
if idx == -1:
    idx = c.find('class="vt-wrap"')
end = c.find('</section>', idx) + 10
print("Timeline section tag:")
print(c[max(0,idx-200):idx+100].encode('utf-8'))
print()
print("Section end -> parallax start:")
print(c[end-50:end+200].encode('utf-8'))
