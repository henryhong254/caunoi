with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Check if there's a wrapping section/div with dark background color
idx = c.find('<section class="parallax-solution">')
end_idx = c.find('</section>', idx) + 10

# Look at CSS for this section  
css_idx = c.find('.parallax-solution')
print("CSS def:")
print(c[css_idx:css_idx+300].encode('utf-8'))
print()

# Check if there's padding on vt-wrap or something making extra space
# Find the section AFTER timeline
timeline_end = c.rfind('</section>', 0, idx)
print("After timeline section end:")
print(c[timeline_end:idx+50].encode('utf-8'))
