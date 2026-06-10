import os
import re
import shutil

# 1. Copy images
src_dir = r"c:\Users\Dell\Desktop\Saurabh\Madam-20260608T082228Z-3-001\Madam"
dest_dir = r"c:\Users\Dell\Desktop\Saurabh\assets\images\madam"
os.makedirs(dest_dir, exist_ok=True)
images = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg'))])
for i, img in enumerate(images):
    src_path = os.path.join(src_dir, img)
    dest_path = os.path.join(dest_dir, f"look-{i+1:02d}.jpg")
    shutil.copy2(src_path, dest_path)

# 2. Update files
search_icon_old = '<span style="font-size:1.1rem">🔍</span>'
search_icon_new = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>'

bag_icon_old = '<span style="font-size:1.1rem">👜</span>'
bag_icon_new = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle;"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace icons
    content = content.replace(search_icon_old, search_icon_new)
    content = content.replace(bag_icon_old, bag_icon_new)
    
    # Replace $ with ₹ and multiply price by 15 (so 145 becomes 2175)
    def replacer(match):
        price_str = match.group(1).replace(',', '')
        price = float(price_str)
        new_price = int(price * 15)
        if new_price < 1000:
            new_price = 1000 + new_price
        return f"₹{new_price}"
        
    content = re.sub(r'\$\s?(\d+(?:,\d{3})*(?:\.\d{2})?)', replacer, content)
    
    if filepath.endswith('products.js'):
        def replacer_js(match):
            price = float(match.group(1))
            new_price = int(price * 15)
            if new_price < 1000:
                new_price = 1000 + new_price
            return f'"price": {new_price}'
        content = re.sub(r'"price":\s*(\d+(?:\.\d{2})?)', replacer_js, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"c:\Users\Dell\Desktop\Saurabh"
for root, dirs, files in os.walk(base_dir):
    # skip Madam-20260608T082228Z-3-001 or other temp folders
    if 'Madam-20260608T082228Z-3-001' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.js')):
            process_file(os.path.join(root, file))
