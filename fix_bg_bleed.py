with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# The issue: the timeline section <section class="section vt-section" id="timeline">
# has padding: 80px 0 from .section. The parallax-solution sits INSIDE or ADJACENT 
# to it but with margin-left: calc(-50vw + 50%) creating a full bleed.
# The dark background comes from the global page background (--c-bg-dark)
# showing through ABOVE the parallax because vt-section has extra bottom padding 80px.

# FIX: Remove bottom padding from the timeline section
old = '<section class="section vt-section" id="timeline">'
new = '<section class="section vt-section" id="timeline" style="padding-bottom: 0;">'
c = c.replace(old, new)

# Also, the parallax-solution with background-color:transparent is wrong
# (the transparent shows dark body bg). Give it a real color instead.
old2 = '<section class="parallax-solution" style="background-color: transparent;">'
new2 = '<section class="parallax-solution">'
c = c.replace(old2, new2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done")
