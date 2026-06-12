import re

def make_admin_prominent(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the navbar links to append the admin button
    # The header has <nav class="d-none d-md-block"> ... <ul> ... </ul>
    # Or we can just append it to the nav-links
    
    # We will add a prominent floating button for the admin so it's impossible to miss.
    floating_btn = """
    <!-- Admin Floating Button -->
    <div style="position: fixed; bottom: 90px; left: 20px; z-index: 9998;">
        <button onclick="toggleAdminMode()" style="background-color: #111; color: #d4af37; border: 2px solid #d4af37; border-radius: 30px; padding: 12px 24px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.3); font-family: sans-serif; letter-spacing: 1px;">⚙️ Admin Panel</button>
    </div>
    """
    
    if "<!-- Admin Floating Button -->" not in content:
        content = content.replace('</body>', floating_btn + '\n</body>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added prominent button to {filepath}")

make_admin_prominent(r"c:\Users\Dell\Desktop\Saurabh\shop.html")
make_admin_prominent(r"c:\Users\Dell\Desktop\Saurabh\index.html")
