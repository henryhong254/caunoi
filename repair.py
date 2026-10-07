import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_next_div = False

# We need to remove the exact lines that have the stray `</div>`
# In the original file, before final_fix, the badge was:
# <div class="vt-badge-wrap"><div class="vt-badge">CHẶNG 1</div></div>
# My regex deleted `<div class="vt-badge-wrap"><div class="vt-badge">CHẶNG 1</div>`
# leaving just `</div>` on a line or something.
# Let's reconstruct by looking at the lines.

i = 0
while i < len(lines):
    line = lines[i]
    
    # If this line is the stray `</div>` caused by the bad regex:
    # It appears exactly between `</div>` (end of vt-row) and `<!-- ROW X -->`
    # Let's just manually patch the known line ranges or fix the exact strings.
    
    # Actually, it's safer to just do string replacements on the full content.
    i += 1

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the stray </div> tags:
# They look like:
#       </div>
# 
#       </div>
# 
#       <!-- ROW 1: CHANG 1 -->
content = content.replace('      </div>\n\n      </div>\n\n      <!-- ROW 1', '      </div>\n\n      <!-- ROW 1')
content = content.replace('      </div>\n\n      </div>\n\n      <!-- ROW 2', '      </div>\n\n      <!-- ROW 2')
content = content.replace('      </div>\n\n      </div>\n\n      <!-- ROW 3', '      </div>\n\n      <!-- ROW 3')
content = content.replace('      </div>\n\n      </div>\n\n      <!-- ROW 4', '      </div>\n\n      <!-- ROW 4')

# Add the absolute START button and fix Row 0 dot
# Currently Row 0 dot is:
# <div class="vt-center vt-start-dot" style="font-size:1.2rem;">START</div>
old_row0_dot = '<div class="vt-center vt-start-dot" style="font-size:1.2rem;">START</div>'
new_row0_dot = '<div class="vt-center" style="width: 40px; height: 40px;"></div>'

content = content.replace(old_row0_dot, new_row0_dot)

# Now inject the Absolute START dot before the SVG
svg_start = content.find('<!-- INLINE SVG TRACK -->')
abs_start_html = '<!-- ABSOLUTE START -->\n      <div class="vt-center" style="position: absolute; top: -50px; left: 50%; transform: translateX(-50%); z-index: 10; font-size: 1.2rem; width: 80px; height: 80px;">START</div>\n\n      '
content = content[:svg_start] + abs_start_html + content[svg_start:]


# Update JS to use correct dots
js_start = content.find('function initTimeline() {')
js_end = content.find('</script>', js_start)

# The JS is mostly correct, but let's ensure it handles the new absolute dot correctly.
# The absolute dot has left: 50%; transform: translateX(-50%).
# getBoundingClientRect().top is correct.
# The car's X is determined by the path, which connects the centers.
# Since absolute dot is at center (X=80 in SVG space), the path will start at X=80!
# This is perfect.

# Let's write back the fixed content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML repaired!")
