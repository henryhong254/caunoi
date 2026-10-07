with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The problem: 
# Block #1: has overflow:hidden but NO border-radius -> turns circle into square!
# Block #3: has font-size: 1rem overriding the 0.6rem - still too big!
# Multiple conflicting blocks scattered everywhere.

# SOLUTION: Do a targeted search-and-replace to clean up ALL blocks.

# Remove block #1 (the bad one with overflow:hidden and no border-radius)
bad_block1 = """      /* Fix Dot Text Overflow */
      .vt-center {
        width: 55px !important;
        height: 55px !important;
        min-width: 55px !important;
        font-size: 0.6rem !important;
        line-height: 1.2 !important;
        padding: 0 !important;
        font-weight: 700 !important;
        overflow: hidden !important;
        text-align: center !important;
      }
      .vt-center.vt-active {
        border-color: var(--c-lime) !important;
        color: var(--c-bg-dark) !important;
        background: var(--c-lime) !important;
        box-shadow: 0 0 0 4px var(--c-bg-dark), 0 0 15px rgba(200, 222, 49, 0.8) !important;
      }"""

# Replace with a SINGLE clean block that has everything correct
good_block1 = """      /* Fix Dot Text Overflow */
      .vt-center {
        width: 52px !important;
        height: 52px !important;
        min-width: 52px !important;
        border-radius: 50% !important;
        font-size: 0.55rem !important;
        line-height: 1.2 !important;
        padding: 4px !important;
        font-weight: 700 !important;
        text-align: center !important;
      }
      .vt-center.vt-active {
        border-color: var(--c-lime) !important;
        color: var(--c-bg-dark) !important;
        background: var(--c-lime) !important;
        box-shadow: 0 0 0 4px var(--c-bg-dark), 0 0 15px rgba(200, 222, 49, 0.8) !important;
      }"""

content = content.replace(bad_block1, good_block1)

# Remove block #2 (the redundant 0.65rem one before block #3)
bad_block2a = """      /* Fix Dot Text Overflow */
      .vt-center {
        font-size: 0.65rem !important;
        line-height: 1.1 !important;
        padding: 0 !important;
      }

      /* Specific fix for START dot */"""
good_block2a = """      /* Specific fix for START dot */"""
content = content.replace(bad_block2a, good_block2a)

# Fix block #3 - reduce font-size from 1rem to 0.55rem
content = content.replace(
    'width: 60px !important; \n        height: 60px !important;\n        font-size: 1rem !important;',
    'width: 52px !important; \n        height: 52px !important;\n        font-size: 0.55rem !important;'
)

# Remove block #4 (another redundant 0.65rem before trophy section)
bad_block4 = """      /* Fix Dot Text Overflow */
      .vt-center {
        font-size: 0.65rem !important;
        line-height: 1.1 !important;
        padding: 0 !important;
      }

      /* Fix the trophy dot */"""
good_block4 = """      /* Fix the trophy dot */"""
content = content.replace(bad_block4, good_block4)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done - cleaned up all vt-center blocks")
