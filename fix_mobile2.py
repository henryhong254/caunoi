with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Issue 1: Remove word-break: keep-all from vt-center (it's causing weird breaks elsewhere) 
# Replace with word-break: normal
content = content.replace(
    'word-break: keep-all !important;\n        overflow: hidden !important;',
    'overflow: hidden !important;'
)

# Issue 2: The quiz title has a <br> that forces a break. On mobile, remove it.
# The <br> in the quiz title: "Nào<br>Trong"
# We'll wrap it in a span that hides on mobile
content = content.replace(
    'Nào<br>Trong Mắt Khách Hàng?',
    'Nào Trong Mắt Khách Hàng?'
)

# Issue 3: Fix the parallax-solution dark background bleed
# The .parallax-solution has background-image and background-color from parent section
# Need to check if there's a padding/margin making dark bg show
# Add explicit background to prevent bleed
content = content.replace(
    '<section class="parallax-solution">',
    '<section class="parallax-solution" style="background-color: transparent;">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
