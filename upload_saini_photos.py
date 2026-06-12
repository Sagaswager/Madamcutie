import os
import shutil
import re

src_dir = r"c:\Users\Dell\Desktop\Saurabh\Saurav Saini Photos"
dest_dir = r"c:\Users\Dell\Desktop\Saurabh\assets\images\madam"

# We will empty the dest_dir and put the new 48 photos there
if os.path.exists(dest_dir):
    for f in os.listdir(dest_dir):
        os.remove(os.path.join(dest_dir, f))
os.makedirs(dest_dir, exist_ok=True)

images = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

copied_images = []
for i, img in enumerate(images):
    src_path = os.path.join(src_dir, img)
    dest_path = os.path.join(dest_dir, f"saini-{i+1:02d}.jpg")
    shutil.copy2(src_path, dest_path)
    copied_images.append(f"saini-{i+1:02d}.jpg")

shop_file = r"c:\Users\Dell\Desktop\Saurabh\shop.html"

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
    page = (idx // 16) + 1 # 16 items per page
    display_style = "block" if page == 1 else "none"
    return f"""
                <div class="madam-card page-item page-{page}" style="position: relative; background: #fff; padding: 15px; border-radius: 2px; transition: transform 0.3s, box-shadow 0.3s; display: {display_style};">
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

cards_html = [generate_card(i, img) for i, img in enumerate(copied_images)]

with open(shop_file, 'r', encoding='utf-8') as f:
    shop_content = f.read()

# Remove old cards
shop_content = re.sub(r'<div class="madam-card.*?</p>\s*<div style="display: flex; align-items: center; justify-content: space-between;">.*?</div>\s*</div>\s*</div>', '', shop_content, flags=re.DOTALL)
# Also remove pagination if it exists from previous attempts
shop_content = re.sub(r'<div class="pagination-container".*?</div>\s*</div>', '', shop_content, flags=re.DOTALL)

shop_cards = "".join(cards_html)

# Add pagination buttons
pagination_html = """
            </div>
            
            <div class="pagination-container" style="display: flex; justify-content: center; gap: 10px; margin-top: 50px;">
                <button onclick="changePage(-1, true)" style="padding: 10px 20px; border: none; background: #f8f6f0; font-weight: 600; cursor: pointer; letter-spacing: 1px;">&lt; PREV</button>
                <button onclick="goToPage(1)" class="page-btn page-btn-1" style="padding: 10px 20px; border: 1px solid #111; background: #111; color: white; font-weight: 600; cursor: pointer;">1</button>
                <button onclick="goToPage(2)" class="page-btn page-btn-2" style="padding: 10px 20px; border: 1px solid #111; background: #fff; color: #111; font-weight: 600; cursor: pointer;">2</button>
                <button onclick="goToPage(3)" class="page-btn page-btn-3" style="padding: 10px 20px; border: 1px solid #111; background: #fff; color: #111; font-weight: 600; cursor: pointer;">3</button>
                <button onclick="changePage(1, true)" style="padding: 10px 20px; border: none; background: #f8f6f0; font-weight: 600; cursor: pointer; letter-spacing: 1px;">NEXT &gt;</button>
            </div>
            
            <script>
                let currentPage = 1;
                const totalPages = 3;
                
                function goToPage(page) {
                    if (page < 1 || page > totalPages) return;
                    currentPage = page;
                    
                    // Hide all items
                    document.querySelectorAll('.page-item').forEach(el => el.style.display = 'none');
                    // Show current page items
                    document.querySelectorAll('.page-' + page).forEach(el => el.style.display = 'block');
                    
                    // Update buttons
                    document.querySelectorAll('.page-btn').forEach(btn => {
                        btn.style.background = '#fff';
                        btn.style.color = '#111';
                    });
                    const activeBtn = document.querySelector('.page-btn-' + page);
                    if (activeBtn) {
                        activeBtn.style.background = '#111';
                        activeBtn.style.color = 'white';
                    }
                    
                    window.scrollTo({top: document.querySelector('.grid-3').offsetTop - 100, behavior: 'smooth'});
                }
                
                function changePage(delta, isRelative) {
                    goToPage(currentPage + delta);
                }
            </script>
"""

shop_content = re.sub(r'(<div class="grid grid-3">)', r'\1' + shop_cards, shop_content)
# Replace the closing div of grid-3 with our pagination html
shop_content = re.sub(r'</div>\s*</div>\s*</section>\s*<!-- Footer -->', pagination_html + r'</div>\n      </section>\n\n      <!-- Footer -->', shop_content)
shop_content = re.sub(r'Showing \d+ products', f'Showing {len(copied_images)} products', shop_content)

with open(shop_file, 'w', encoding='utf-8') as f:
    f.write(shop_content)

# We should also update index.html to use some of the new photos so it's not broken!
index_file = r"c:\Users\Dell\Desktop\Saurabh\index.html"
with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = re.sub(r'<div class="madam-card.*?</p>\s*<div style="display: flex; align-items: center; justify-content: space-between;">.*?</div>\s*</div>\s*</div>', '', index_content, flags=re.DOTALL)
index_cards = "".join(cards_html[:8])
index_content = re.sub(r'(id="madam-grid">)', r'\1' + index_cards, index_content)

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(index_content)

print(f"Added {len(copied_images)} photos with pagination.")
