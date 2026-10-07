with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The desktop vt-center definition is INSIDE the mobile media query!
# That's why the 0.65rem fix doesn't work - it gets overridden immediately after.
# We need to consolidate ALL mobile vt-center into ONE block with correct values.

# Step 1: Remove ALL scattered .vt-center blocks inside the mobile media query
# Then replace with a single clean one.

# Find the main mobile block that handles the timeline
old = """      /* Fix Dot Text Overflow */
      .vt-center {
        font-size: 0.65rem !important;
        line-height: 1.1 !important;
        padding: 0 !important;
      }

      .vt-center {
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
    }
    .vt-center.vt-active {
      border-color: var(--c-lime);
      color: var(--c-bg-dark);
      background: var(--c-lime);
      box-shadow: 0 0 0 6px var(--c-bg-dark), 0 0 20px rgba(200, 222, 49, 0.8);
    }"""

new = """      /* Fix Dot Text Overflow */
      .vt-center {
        width: 55px !important;
        height: 55px !important;
        min-width: 55px !important;
        font-size: 0.6rem !important;
        line-height: 1.2 !important;
        padding: 0 !important;
        font-weight: 700 !important;
        word-break: keep-all !important;
        overflow: hidden !important;
        text-align: center !important;
      }
      .vt-center.vt-active {
        border-color: var(--c-lime) !important;
        color: var(--c-bg-dark) !important;
        background: var(--c-lime) !important;
        box-shadow: 0 0 0 4px var(--c-bg-dark), 0 0 15px rgba(200, 222, 49, 0.8) !important;
      }"""

content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
