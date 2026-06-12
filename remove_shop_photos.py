import re

filepath = r"c:\Users\Dell\Desktop\Saurabh\shop.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The cards are in <div class="grid grid-3"> ... </div>
# We can find this div and remove its inner content.
# Alternatively, we can use regex to remove all <div class="madam-card">...</div> blocks.
# Let's remove all madam-card divs.
import re
new_content = re.sub(r'<div class="madam-card".*?</div>\s*</div>', '', content, flags=re.DOTALL)

# Update the "Showing 12 products" text
new_content = re.sub(r'Showing \d+ products', 'Showing 0 products', new_content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed all product cards from the Shop page.")
