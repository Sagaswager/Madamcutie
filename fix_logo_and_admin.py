import os
import re

html_files = [
    r"c:\Users\Dell\Desktop\Saurabh\index.html",
    r"c:\Users\Dell\Desktop\Saurabh\shop.html",
    r"c:\Users\Dell\Desktop\Saurabh\product.html",
    r"c:\Users\Dell\Desktop\Saurabh\about.html",
    r"c:\Users\Dell\Desktop\Saurabh\contact.html"
]

floating_btn_pattern = r'<!-- Admin Floating Button -->.*?</div>\s*'

admin_js = """
<!-- Admin Mode Script -->
<script>
function toggleAdminMode() {
    const isActive = localStorage.getItem('adminMode') === 'true';
    localStorage.setItem('adminMode', !isActive);
    if (!isActive) {
        // If activating, redirect to home page so we can edit there
        window.location.href = 'index.html';
    } else {
        location.reload();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('adminMode') === 'true') {
        const toolbar = document.createElement('div');
        toolbar.id = 'admin-toolbar';
        toolbar.style.cssText = 'position: fixed; top: 0; left: 0; width: 100%; background: #111; color: #fff; padding: 10px 20px; z-index: 10000; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.5); font-family: sans-serif;';
        toolbar.innerHTML = `
            <div style="font-weight: bold; font-size: 14px; letter-spacing: 1px;">⚙️ ADMIN MODE ACTIVE</div>
            <div>
                <button onclick="saveChanges()" style="background: #d4af37; color: #fff; border: none; padding: 5px 15px; margin-right: 10px; cursor: pointer; font-weight: bold; border-radius: 2px;">Save Changes</button>
                <button onclick="toggleAdminMode()" style="background: #fff; color: #111; border: none; padding: 5px 15px; cursor: pointer; font-weight: bold; border-radius: 2px;">Exit Admin</button>
            </div>
        `;
        document.body.prepend(toolbar);

        const titles = document.querySelectorAll('.madam-card h3 a');
        const descriptions = document.querySelectorAll('.madam-card p:nth-of-type(2)');
        const prices = document.querySelectorAll('.madam-card span:last-child');

        [...titles, ...descriptions, ...prices].forEach(el => {
            el.contentEditable = "true";
            el.style.border = "1px dashed #d4af37";
            el.style.padding = "2px";
            el.style.outline = "none";
            el.addEventListener('focus', function() {
                this.style.background = 'rgba(212, 175, 55, 0.1)';
            });
            el.addEventListener('blur', function() {
                this.style.background = 'transparent';
            });
        });
    }
});

function saveChanges() {
    const btn = document.querySelector('#admin-toolbar button');
    btn.textContent = 'Saving...';
    const toolbar = document.getElementById('admin-toolbar');
    if (toolbar) toolbar.remove();
    
    document.querySelectorAll('[contenteditable="true"]').forEach(el => {
        el.removeAttribute('contenteditable');
        el.style.border = '';
        el.style.padding = '';
        el.style.outline = '';
        el.style.background = '';
    });
    
    document.querySelectorAll('.page-item').forEach(el => {
        if(el.style.display === 'block' || el.style.display === 'none') {
            el.style.removeProperty('display');
        }
    });

    const currentHtml = "<!DOCTYPE html>\\n" + document.documentElement.outerHTML;
    localStorage.setItem('adminMode', 'true');
    const filename = location.pathname.split('/').pop() || 'index.html';
    
    fetch('/save_html', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ file: filename, content: currentHtml })
    }).then(res => res.json()).then(data => {
        if(data.status === 'success') {
            alert('Changes saved successfully!');
            location.reload();
        } else {
            alert('Error saving changes: ' + (data.message || 'Unknown error'));
            location.reload();
        }
    }).catch(err => {
        alert('Failed to connect to Admin Server. Make sure server.py is running.');
        location.reload();
    });
}
</script>
"""

for filepath in html_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Fix Logo
        content = content.replace('new_logo.png', 'logo.jpg')

        # 2. Remove floating button from all pages
        content = re.sub(floating_btn_pattern, '', content, flags=re.DOTALL)

        # 3. Ensure admin_js is present in all files so toolbar works everywhere
        if 'function toggleAdminMode()' not in content:
            content = content.replace('</body>', admin_js + '\n</body>')
        else:
            # Update the script to the latest version (which redirects on login)
            content = re.sub(r'<!-- Admin Mode Script -->.*?</script>', admin_js, content, flags=re.DOTALL)

        # 4. If this is contact.html, add the hidden button!
        if 'contact.html' in filepath:
            # We add it as a completely invisible button in the bottom right corner
            # Only the owner knows to click the exact bottom right corner pixel!
            hidden_btn = """
            <button onclick="toggleAdminMode()" style="position: fixed; bottom: 0; right: 0; width: 30px; height: 30px; opacity: 0; cursor: default; z-index: 9999; border: none;"></button>
            """
            if 'toggleAdminMode()' not in content.split('</body>')[0].split('<footer')[-1]: # rough check
                content = content.replace('</body>', hidden_btn + '\n</body>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated logo and moved admin button to contact.html as a hidden trigger.")
