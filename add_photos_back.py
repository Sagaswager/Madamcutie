import os
import re

index_file = r"c:\Users\Dell\Desktop\Saurabh\index.html"
shop_file = r"c:\Users\Dell\Desktop\Saurabh\shop.html"
images_dir = r"c:\Users\Dell\Desktop\Saurabh\assets\images\madam"

images = sorted([f for f in os.listdir(images_dir) if f.startswith('look-') and f.endswith('.jpg')])

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

desc = "Perfect for parties & evening events."

def generate_card(idx, img_name):
    name = party_names[idx % len(party_names)]
    price = 1500 + (idx * 45) % 2000
    reviews = 80 + (idx * 23) % 400
    return f"""
                <div class="madam-card" style="position: relative; background: #fff; padding: 15px; border-radius: 2px; transition: transform 0.3s, box-shadow 0.3s;">
                    <div style="position: relative; background: linear-gradient(135deg, #f8f6f0 0%, #edeae0 100%); padding: 15px; border-radius: 2px; overflow: hidden; aspect-ratio: 3/4;">
                        { '<span style="position: absolute; top: 15px; left: 15px; background: #d4af37; color: #fff; padding: 4px 12px; font-size: 0.65rem; font-weight: bold; border-radius: 20px; z-index: 2; letter-spacing: 1px;">SALE</span>' if idx % 3 == 0 else '' }
                        <a href="product.html"><img src="/assets/images/madam/{img_name}" alt="{name}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;"></a>
                    </div>
                    <div style="padding-top: 20px; text-align: left;">
                        <p style="font-size: 0.7rem; color: var(--color-text-light); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 6px;">MADAMCUTIE</p>
                        <h3 style="font-size: 1.2rem; margin-bottom: 6px; font-weight: 500;"><a href="product.html" style="color: inherit; text-decoration: none;">{name}</a></h3>
                        <p style="font-size: 0.85rem; color: #777; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{desc}</p>
                        <div style="display: flex; align-items: center; justify-content: space-between;">
                            <div style="display: flex; align-items: center; gap: 5px; font-size: 0.8rem;">
                                <span style="color: #d4af37; letter-spacing: 2px;">★★★★★</span>
                                <span style="color: #888; margin-left: 5px;">({reviews})</span>
                            </div>
                            <span style="font-weight: 600;">₹{price}</span>
                        </div>
                    </div>
                </div>
"""

cards_html = [generate_card(i, img) for i, img in enumerate(images)]

with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

index_cards = "".join(cards_html[:8])
index_content = re.sub(r'(id="madam-grid">)', r'\1' + index_cards, index_content)

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(index_content)


with open(shop_file, 'r', encoding='utf-8') as f:
    shop_content = f.read()

shop_cards = "".join(cards_html)
shop_content = re.sub(r'(<div class="grid grid-3">)', r'\1' + shop_cards, shop_content)
shop_content = re.sub(r'Showing 0 products', f'Showing {len(images)} products', shop_content)

with open(shop_file, 'w', encoding='utf-8') as f:
    f.write(shop_content)

print("Done")
