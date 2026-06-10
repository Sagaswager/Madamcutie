import os
import glob
import re

html_files = glob.glob("*.html")

ABOUT_TEXT = """Welcome to MadamCutie – where fashion meets confidence and elegance. Based in the vibrant heart of Chandni Chowk, we bring you thoughtfully curated women's apparel that blends timeless charm with modern trends.
At MadamCutie, we believe every woman deserves to feel beautiful, confident, and comfortable in what she wears. Our collections are designed to celebrate individuality, offering stylish outfits that suit every occasion—from everyday wear to special moments.
Inspired by the rich fashion heritage of Chandni Chowk and driven by contemporary style, we focus on quality craftsmanship, attention to detail, and designs that make a lasting impression. Every piece is created with the goal of helping women express their unique personality through fashion.
Whether you're looking for elegant ethnic wear, trendy outfits, or statement pieces, MadamCutie is your destination for fashion that feels as good as it looks.
MadamCutie – Crafted for Confidence, Styled for You. ✨👗💕"""

ABOUT_HTML = f"""<p style="font-size: 1.1rem; color: var(--color-text-light); line-height: 1.8; margin-bottom: 20px;">
                        {ABOUT_TEXT.replace(chr(10), '<br><br>')}
                    </p>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Number update
    content = content.replace("9911852113", "+91-9911852113")

    # 2. Add navigation items (For Wholesale, For Creators)
    # Desktop Nav
    nav_item = '                <a href="wholesale.html">For Wholesale</a>\n                <a href="creators.html">For Creators</a>\n                <a href="contact.html"'
    content = re.sub(r'(\s*)<a href="contact.html"', r'\1<a href="wholesale.html">For Wholesale</a>\1<a href="creators.html">For Creators</a>\1<a href="contact.html"', content)

    # 3. Location update
    content = content.replace("Noida, India", "Chandni Chowk, Delhi")

    if file == 'contact.html':
        # Add return & refund policy button near contact details
        button_html = '\n                    <div style="margin-top: 40px; margin-bottom: 30px;">\n                        <a href="policy.html" class="btn btn-secondary" style="width: 100%; text-align: center; display: block; border-radius: 2px;">Return & Refund Policy</a>\n                    </div>'
        content = content.replace('<h4 style="font-size: 1.1rem; margin-bottom: 10px;">HQ Location</h4>\n                        <p style="color: var(--color-text-light); font-size: 1.05rem;">Chandni Chowk, Delhi</p>\n                    </div>', '<h4 style="font-size: 1.1rem; margin-bottom: 10px;">HQ Location</h4>\n                        <p style="color: var(--color-text-light); font-size: 1.05rem;">Chandni Chowk, Delhi</p>\n                    </div>' + button_html)

    if file == 'about.html':
        # Update text
        content = re.sub(r'<p style="font-size: 1.1rem; color: var\(--color-text-light\); line-height: 1.8; margin-bottom: 20px;">\s*Madamcutie was born out of.*? everyday queen you are\.\s*</p>', ABOUT_HTML, content, flags=re.DOTALL)
        content = content.replace('Born in Noida, Designed for the World', 'Born in Chandni Chowk, Designed for the World')

    if file in ['shop.html', 'product.html']:
        # Update Categories
        new_cats = """<li><label><input type="checkbox"> Lehenga</label></li>
                        <li><label><input type="checkbox"> Co-ords Set</label></li>
                        <li><label><input type="checkbox"> Party Wear</label></li>
                        <li><label><input type="checkbox"> Party Wear Blouse</label></li>"""
        content = re.sub(r'<li><label><input type="checkbox"> Dresses</label></li>.*?<li><label><input type="checkbox"> Workwear</label></li>', new_cats, content, flags=re.DOTALL)

        # Update Size
        new_size = '<button class="size-btn">Free Size</button>'
        content = re.sub(r'<button class="size-btn">XS</button>.*?<button class="size-btn">XL</button>', new_size, content, flags=re.DOTALL)

    if file == 'index.html':
        content = re.sub(r'<p style="font-size: 1.1rem; color: var\(--color-text-light\); margin-bottom: 20px; line-height: 1.8;">At Madamcutie, we believe that every woman deserves to feel like royalty.*? personal style journey\.</p>', ABOUT_HTML.replace('<p style="font-size: 1.1rem; color: var(--color-text-light); line-height: 1.8; margin-bottom: 20px;">', '<p style="font-size: 1.1rem; color: var(--color-text-light); margin-bottom: 20px; line-height: 1.8;">'), content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Create creators.html
creators_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For Creators | Madamcutie</title>
    <meta name="description" content="Brand collaboration with Madamcutie">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="announcement-bar">
        <div class="announcement-bar-content">
            ✦ Free complimentary shipping on orders over ₹2250 ✦ Use code: MADAM15 for 15% off your first luxury purchase ✦ New Summer Edit now live! ✦
        </div>
    </div>

    <header class="header">
        <div class="container nav-container">
            <div class="logo-wrapper">
                <img src="/assets/images/logo.jpg" alt="Madamcutie Logo" class="logo-img" style="height: 45px; object-fit: contain;">
                <a href="index.html" class="logo-text" style="background: linear-gradient(45deg, #d4af37, #f3e5ab, #b8860b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0px 2px 4px rgba(0,0,0,0.1); font-weight: 800; font-family: var(--font-heading); font-size: 2.2rem; letter-spacing: 2px;">Madamcutie</a>
            </div>
            
            <nav class="nav-links">
                <a href="index.html">Home</a>
                <a href="shop.html">Shop</a>
                <a href="about.html">Our Story</a>
                <a href="wholesale.html">For Wholesale</a>
                <a href="creators.html" class="active" style="border-bottom: 1px solid var(--color-primary);">For Creators</a>
                <a href="contact.html">Contact</a>
            </nav>

            <div class="header-actions">
                <a href="shop.html" class="action-btn" id="search-trigger" title="Search"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></a>
                <button class="mobile-menu-toggle action-btn" aria-label="Toggle Menu">☰</button>
            </div>
        </div>
    </header>

    <div class="mobile-nav-drawer-overlay" id="mobile-nav-overlay"></div>
    <div class="mobile-nav-drawer" id="mobile-nav-drawer">
        <button class="drawer-close-btn">✕</button>
        <nav class="mobile-nav-links">
            <a href="index.html">Home</a>
            <a href="shop.html">Shop</a>
            <a href="about.html">Our Story</a>
            <a href="wholesale.html">For Wholesale</a>
            <a href="creators.html">For Creators</a>
            <a href="contact.html">Contact</a>
        </nav>
    </div>

    <section style="background-color: #f8f8f8; padding: 60px 0; text-align: center; border-bottom: 1px solid var(--color-border);">
        <div class="container">
            <h1 style="font-family: var(--font-heading); font-size: 2.8rem; margin-bottom: 10px;">Brand Collaboration</h1>
            <p style="color: var(--color-text-light); font-size: 1.1rem;">Join the Madamcutie creator family.</p>
        </div>
    </section>

    <section class="section">
        <div class="container" style="max-width: 600px; margin: 0 auto;">
            <div id="success-message" style="display: none; background: #e8f5e9; color: #2e7d32; padding: 20px; border-radius: 4px; margin-bottom: 20px; text-align: center; font-weight: 600;">
                Thank you! Our team will review your profile and get back to you for collaboration opportunities.
            </div>
            
            <form id="creator-form" style="background: #fff; padding: 40px; border: 1px solid var(--color-border); border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <div style="margin-bottom: 20px;">
                    <label style="display: block; margin-bottom: 5px; font-weight: 600;">Name *</label>
                    <input type="text" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 2px;" required>
                </div>
                <div style="margin-bottom: 20px;">
                    <label style="display: block; margin-bottom: 5px; font-weight: 600;">Instagram ID *</label>
                    <input type="text" placeholder="@yourhandle" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 2px;" required>
                </div>
                <div style="margin-bottom: 20px;">
                    <label style="display: block; margin-bottom: 5px; font-weight: 600;">WhatsApp Number *</label>
                    <input type="tel" pattern="[0-9+\\- ]+" placeholder="+91 1234567890" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 2px;" required>
                </div>
                <div style="margin-bottom: 30px;">
                    <label style="display: block; margin-bottom: 5px; font-weight: 600;">Email *</label>
                    <input type="email" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 2px;" required>
                </div>
                
                <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Application</button>
            </form>
        </div>
    </section>

    <footer class="footer" style="background: var(--color-primary); color: white; padding: 80px 0 30px;">
        <div class="container text-center">
            <h3 style="font-family: var(--font-heading); font-size: 2rem; margin-bottom: 20px; letter-spacing: 1px;">Madamcutie</h3>
            <p style="color: #aaa; margin-bottom: 20px; font-size: 0.9rem;"><strong>Phone:</strong> +91-9911852113</p>
            <p style="color: #aaa; margin-bottom: 20px; font-size: 0.9rem;"><strong>Location:</strong> Chandni Chowk, Delhi</p>
        </div>
    </footer>

    <script src="/js/main.js"></script>
    <script>
        document.getElementById('creator-form').addEventListener('submit', function(e) {
            e.preventDefault();
            this.style.display = 'none';
            document.getElementById('success-message').style.display = 'block';
        });
    </script>
</body>
</html>
"""

with open('creators.html', 'w', encoding='utf-8') as f:
    f.write(creators_html)
