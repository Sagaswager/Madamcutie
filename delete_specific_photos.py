import os
import re

index_file = r"c:\Users\Dell\Desktop\Saurabh\index.html"
shop_file = r"c:\Users\Dell\Desktop\Saurabh\shop.html"
images_dir = r"c:\Users\Dell\Desktop\Saurabh\assets\images\madam"

# The indices of the photos to delete
# idx = 2 -> look-03.jpg
# idx = 3 -> look-04.jpg
# idx = 4 -> look-05.jpg
# idx = 5 -> look-06.jpg
# idx = 6 -> look-07.jpg
# idx = 12 -> look-13.jpg
files_to_delete = [
    "look-03.jpg",
    "look-04.jpg",
    "look-05.jpg",
    "look-06.jpg",
    "look-07.jpg",
    "look-13.jpg"
]

# Delete the image files
for f in files_to_delete:
    path = os.path.join(images_dir, f)
    if os.path.exists(path):
        os.remove(path)

# Update HTML files to remove these cards
def remove_cards(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all madam-card blocks
    # We can use a regex to find each block and replace it if it contains any of the files_to_delete
    
    def replacer(match):
        block = match.group(0)
        for f in files_to_delete:
            if f in block:
                return ""  # Remove the block
        return block

    # We need a robust regex for the block. 
    # It starts with <div class="madam-card" and ends with the matching </div>
    # In our generated HTML, each madam-card ends with \n                </div>\n
    # So we can match up to </div>\n                </div>
    # Actually, let's just match up to ₹\d+</span>\s*</div>\s*</div>\s*</div>
    new_content = re.sub(r'<div class="madam-card".*?₹\d+</span>\s*</div>\s*</div>\s*</div>', replacer, content, flags=re.DOTALL)
    
    return new_content

new_index = remove_cards(index_file)
with open(index_file, 'w', encoding='utf-8') as f:
    f.write(new_index)

new_shop = remove_cards(shop_file)
# Update the showing products count
# We deleted 6 products. Originally it was 16. So it should be 10.
new_shop = re.sub(r'Showing \d+ products', 'Showing 10 products', new_shop)
with open(shop_file, 'w', encoding='utf-8') as f:
    f.write(new_shop)

print("Deleted specific photos and removed them from HTML.")
