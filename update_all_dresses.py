import os
import re

files_to_update = [
    r"c:\Users\Dell\Desktop\Saurabh\index.html",
    r"c:\Users\Dell\Desktop\Saurabh\shop.html",
    r"c:\Users\Dell\Desktop\Saurabh\product.html"
]

def replace_in_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic party-themed names to replace the remaining "Madamcutie Look XX"
    party_names = [
        "Designer Party Wear Dress",
        "2 Piece Co-ords Set Silver Hand Work Blouse",
        "Luxury Evening Party Dress",
        "Glamorous Sequin Cocktail Dress",
        "Elegant Velvet Evening Gown",
        "Stunning Embellished Party Wear",
        "Chic Metallic Co-ords Set",
        "Radiant Night Out Dress",
        "Classic Midnight Blue Gown",
        "Sparkling Silver Hand Work Set",
        "Elegant Silk Party Dress",
        "Sleek Cocktail Maxi Dress"
    ]

    # Description to replace all descriptions with
    desc = "Perfect for parties & evening events."

    # Replace all 'Madamcutie Look XX' with the party names based on the number
    def rename_match(match):
        look_num = int(match.group(1))
        idx = (look_num - 1) % len(party_names)
        return party_names[idx]
        
    content = re.sub(r'Madamcutie Look (\d+)', rename_match, content)

    # We also need to replace the old descriptions with the new one.
    old_descs = [
        "Weekend getaway essential",
        "Breezy floral arrangement",
        "A statement in monochrome",
        "Evening gown perfection",
        "Vibrant summer essential",
        "Midnight blue variation",
        "Monochrome office essential",
        "Warm tones casual wear",
        "Vibrant weekend brights",
        "Perfect for parties & evening events..",
        "Perfect for parties & evening events."
    ]
    for d in old_descs:
        content = content.replace(d, desc)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for f in files_to_update:
    replace_in_file(f)

print("All remaining dresses and descriptions updated to party theme.")
