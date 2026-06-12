import re
filepath = r"c:\Users\Dell\Desktop\Saurabh\contact.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the invisible button if it exists
content = re.sub(r'<button onclick="toggleAdminMode\(\)".*?opacity: 0.*?</button>', '', content, flags=re.DOTALL)

visible_btn = """
<!-- Admin Floating Button -->
<div style="position: fixed; bottom: 30px; left: 30px; z-index: 9998;">
    <button onclick="toggleAdminMode()" style="background-color: #111; color: #d4af37; border: 2px solid #d4af37; border-radius: 30px; padding: 12px 24px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.3); font-family: sans-serif; letter-spacing: 1px; display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 1.2rem;">⚙️</span> Admin Panel
    </button>
</div>
"""

# Ensure it's not added multiple times
if "Admin Floating Button" not in content:
    content = content.replace('</body>', visible_btn + '\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Visible admin button added to contact.html")
