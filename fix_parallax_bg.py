with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# The dark bg bleed is likely from the section wrapper having dark bg from global page bg
# The parallax has 100vw width which can cause overflow with dark parent bg showing around edges
# Fix: ensure the vt-wrap section below doesn't bleed into the parallax

# Find if there's a section wrapping vt-wrap with background
old = '.parallax-solution {\n  position: relative;\n  background-image: url(\'manydoor.jpg\');\n  background-attachment: fixed;\n  background-position: center;\n  background-repeat: no-repeat;\n  background-size: cover;\n  width: 100vw;\n  margin-left: calc(-50vw + 50%);\n}'

new = '''.parallax-solution {
  position: relative;
  background-image: url('manydoor.jpg');
  background-color: #04584c;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  width: 100vw;
  margin-left: calc(-50vw + 50%);
}'''

content = content.replace(old, new)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
