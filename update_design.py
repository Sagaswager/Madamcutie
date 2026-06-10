import os
import re

logo_old = '<a href="index.html" class="logo-text">Madamcutie</a>'
logo_new = '<a href="index.html" class="logo-text" style="background: linear-gradient(45deg, #d4af37, #f3e5ab, #b8860b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0px 2px 4px rgba(0,0,0,0.1); font-weight: 800; font-family: var(--font-heading); font-size: 2.2rem; letter-spacing: 2px;">Madamcutie</a>'

hero_old = """<div class="hero-bg" style="position: absolute; top:0; left:0; width: 100%; height: 100%; background-image: url('assets/images/madam/hero-bg.jpg'); background-size: cover; background-position: center;"></div>
        <!-- Overlay -->
        <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(to right, rgba(0,0,0,0.4), rgba(0,0,0,0.1));"></div>"""

hero_new = """<div class="hero-bg" style="position: absolute; top:0; left:0; width: 100%; height: 100%; background: linear-gradient(135deg, #d4af37 0%, #f3e5ab 50%, #b8860b 100%); opacity: 0.85;"></div>
        <div style="position: absolute; top: -10%; left: -5%; width: 400px; height: 400px; border-radius: 50%; background: radial-gradient(circle, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0) 70%);"></div>
        <div style="position: absolute; bottom: -20%; right: -10%; width: 600px; height: 600px; border-radius: 50%; background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0) 70%);"></div>
        <!-- Overlay -->
        <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: radial-gradient(circle at center, transparent 0%, rgba(0,0,0,0.4) 100%);"></div>"""

highlight_old = """    <!-- Highlight Strip -->
    <div class="highlight-strip" style="background-color: var(--color-primary); color: var(--color-secondary); padding: 25px 0; border-top: 2px solid #d4af37;">
        <div class="container">
            <div class="grid grid-4 text-center">
                <div class="highlight-item d-flex align-center justify-center" style="gap: 10px;">
                    <span style="font-size: 1.5rem; color: #d4af37;">✨</span>
                    <h4 style="text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.85rem; margin: 0;">Premium Fabrics</h4>
                </div>
                <div class="highlight-item d-flex align-center justify-center" style="gap: 10px;">
                    <span style="font-size: 1.5rem; color: #d4af37;">🚚</span>
                    <h4 style="text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.85rem; margin: 0;">Pan-India Shipping</h4>
                </div>
                <div class="highlight-item d-flex align-center justify-center" style="gap: 10px;">
                    <span style="font-size: 1.5rem; color: #d4af37;">↺</span>
                    <h4 style="text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.85rem; margin: 0;">Easy 7-Day Returns</h4>
                </div>
                <div class="highlight-item d-flex align-center justify-center" style="gap: 10px;">
                    <span style="font-size: 1.5rem; color: #d4af37;">🔒</span>
                    <h4 style="text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.85rem; margin: 0;">Secure Payments</h4>
                </div>
            </div>
        </div>
    </div>"""

highlight_new = """    <!-- Highlight Strip -->
    <div class="highlight-strip" style="background: linear-gradient(90deg, #b8860b 0%, #d4af37 25%, #f3e5ab 50%, #d4af37 75%, #b8860b 100%); color: #111; padding: 25px 0; border-top: 1px solid rgba(255,255,255,0.6); box-shadow: 0 4px 15px rgba(0,0,0,0.15);">
        <div class="container">
            <div class="grid grid-4 text-center">
                <div class="highlight-item d-flex align-center justify-center" style="gap: 12px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
                    <h4 style="text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; font-weight: 700; margin: 0; color: #111;">Premium Fabrics</h4>
                </div>
                <div class="highlight-item d-flex align-center justify-center" style="gap: 12px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
                    <h4 style="text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; font-weight: 700; margin: 0; color: #111;">Pan-India Shipping</h4>
                </div>
                <div class="highlight-item d-flex align-center justify-center" style="gap: 12px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <h4 style="text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; font-weight: 700; margin: 0; color: #111;">Easy 7-Day Returns</h4>
                </div>
                <div class="highlight-item d-flex align-center justify-center" style="gap: 12px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                    <h4 style="text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; font-weight: 700; margin: 0; color: #111;">Secure Payments</h4>
                </div>
            </div>
        </div>
    </div>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Logo Text
    content = content.replace(logo_old, logo_new)
    
    if 'index.html' in filepath:
        content = content.replace(hero_old, hero_new)
        content = content.replace(highlight_old, highlight_new)
        # 4. Update style edit images
        content = content.replace('lookbook-1.jpg', 'look-15.jpg')
        content = content.replace('lookbook-2.jpg', 'look-16.jpg')
        content = content.replace('lookbook-3.jpg', 'look-17.jpg')
        content = content.replace('brand-story.jpg', 'look-18.jpg')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"c:\Users\Dell\Desktop\Saurabh"
for root, dirs, files in os.walk(base_dir):
    if 'Madam-20260608T082228Z-3-001' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
