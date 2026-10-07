import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to extract the indices of each section
hero_start = content.find('<!-- HERO SECTION -->')
quiz_start = content.find('<!-- SECTION 2: QUIZ -->')
quote_start = content.find('<!-- QUOTE BRIDGE SECTION -->')
timeline_start = content.find('<!-- SECTION 3: ELEGANT TIMELINE -->')
final_start = content.find('<section class="section" id="final-cta"')
if final_start == -1:
    # Try finding id="final-cta"
    final_start = content.find('id="final-cta"')

print(f"Hero: {hero_start}")
print(f"Quiz: {quiz_start}")
print(f"Quote: {quote_start}")
print(f"Timeline: {timeline_start}")
print(f"Final: {final_start}")
