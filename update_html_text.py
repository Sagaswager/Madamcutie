import os
import re

files_to_update = [
    r"c:\Users\Dell\Desktop\Saurabh\index.html",
    r"c:\Users\Dell\Desktop\Saurabh\shop.html",
    r"c:\Users\Dell\Desktop\Saurabh\product.html"
]

replacements = {
    "Madamcutie Look 01": "Designer Party Wear Dress",
    "Madamcutie Look 02": "2 Piece Co-ords Set Silver Hand Work Blouse",
    "Madamcutie Look 03": "Luxury Evening Party Dress",
    "Elegant silhouette for the office": "Perfect for parties & evening events.",
    "Comfort meets chic casuals": "Perfect for parties & evening events.",
    "Perfect for parties & evening events": "Perfect for parties & evening events."
}

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML files updated successfully.")
