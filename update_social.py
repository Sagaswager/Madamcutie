import glob
import re

html_files = glob.glob("*.html")

whatsapp_html = """
<!-- Floating WhatsApp Button -->
<a href="https://wa.me/919911852113" target="_blank" class="whatsapp-floating" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24" width="30" height="30" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" style="display:block; margin:auto;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
</a>
<style>
.whatsapp-floating {
    position: fixed;
    bottom: 25px;
    right: 25px;
    width: 60px;
    height: 60px;
    background-color: #25D366;
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    z-index: 9999;
    transition: transform 0.3s ease, background-color 0.3s ease;
}
.whatsapp-floating:hover {
    transform: scale(1.1);
    background-color: #20BA5C;
    color: white;
}
@media (max-width: 768px) {
    .whatsapp-floating {
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
    }
}
</style>
</body>"""

fb_svg = '<svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>'
ig_svg = '<svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>'
pt_svg = '<svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2C6.48 2 2 6.48 2 12c0 4.25 2.65 7.9 6.44 9.32-.09-.78-.17-1.98.03-2.83.18-.75 1.16-4.94 1.16-4.94s-.3-.6-.3-1.48c0-1.39.81-2.43 1.82-2.43.85 0 1.26.64 1.26 1.4 0 .86-.54 2.14-.83 3.32-.24.99.5 1.8 1.47 1.8 1.76 0 3.12-1.86 3.12-4.54 0-2.38-1.71-4.04-4.16-4.04-2.84 0-4.5 2.13-4.5 4.32 0 .85.33 1.76.74 2.26.08.1.09.18.06.28-.08.35-.27 1.09-.31 1.25-.05.19-.17.23-.37.14-1.38-.63-2.24-2.61-2.24-4.2 0-3.42 2.49-6.56 7.16-6.56 3.76 0 6.68 2.68 6.68 6.26 0 3.74-2.36 6.75-5.63 6.75-1.1 0-2.13-.57-2.48-1.24l-.68 2.58c-.24.92-.91 2.07-1.35 2.77 1.07.33 2.21.5 3.39.5 5.52 0 10-4.48 10-10S17.52 2 12 2z"></path></svg>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add floating WhatsApp icon
    if 'whatsapp-floating' not in content:
        content = content.replace('</body>', whatsapp_html)

    # 2. Update Social Icons in Footer
    # Replace FB
    content = re.sub(r'<a href="#" class="social-icon" style="color: white; font-size: 1\.3rem;">FB</a>', f'<a href="#" class="social-icon" style="color: white;" title="Facebook">{fb_svg}</a>', content)
    # Replace IG
    content = re.sub(r'<a href="#" class="social-icon" style="color: white; font-size: 1\.3rem;">IG</a>', f'<a href="https://www.instagram.com/madamcutie.co?igsh=OGcwdmFxYTBuZGhv&utm_source=qr" target="_blank" class="social-icon" style="color: white;" title="Instagram">{ig_svg}</a>', content)
    # Replace PT
    content = re.sub(r'<a href="#" class="social-icon" style="color: white; font-size: 1\.3rem;">PT</a>', f'<a href="#" class="social-icon" style="color: white;" title="Pinterest">{pt_svg}</a>', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
