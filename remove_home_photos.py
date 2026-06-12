import re

filepath = r"c:\Users\Dell\Desktop\Saurabh\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all <div class="madam-card">...</div> blocks from index.html
new_content = re.sub(r'<div class="madam-card".*?</div>\s*</div>', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed all product cards from the Home page.")
