import re
import os

admin_js = """
<!-- Admin Mode Script -->
<script>
function toggleAdminMode() {
    const isActive = localStorage.getItem('adminMode') === 'true';
    localStorage.setItem('adminMode', !isActive);
    location.reload();
}

document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('adminMode') === 'true') {
        // Create Admin Toolbar
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

        // Make elements editable
        const titles = document.querySelectorAll('.madam-card h3 a');
        const descriptions = document.querySelectorAll('.madam-card p:nth-of-type(2)'); // The description
        const prices = document.querySelectorAll('.madam-card span:last-child'); // The price

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
    
    // Clean up DOM before saving
    const toolbar = document.getElementById('admin-toolbar');
    if (toolbar) toolbar.remove();
    
    // Remove editable styles
    const editables = document.querySelectorAll('[contenteditable="true"]');
    editables.forEach(el => {
        el.removeAttribute('contenteditable');
        el.style.border = '';
        el.style.padding = '';
        el.style.outline = '';
        el.style.background = '';
    });
    
    // Remove pagination inline display styles if on shop page
    document.querySelectorAll('.page-item').forEach(el => {
        if(el.style.display === 'block' || el.style.display === 'none') {
            el.style.removeProperty('display');
        }
    });

    const currentHtml = "<!DOCTYPE html>\\n" + document.documentElement.outerHTML;
    
    // Re-enable admin mode UI
    localStorage.setItem('adminMode', 'true');
    
    const filename = location.pathname.split('/').pop() || 'index.html';
    
    fetch('/save_html', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            file: filename,
            content: currentHtml
        })
    })
    .then(res => res.json())
    .then(data => {
        if(data.status === 'success') {
            alert('Changes saved successfully!');
            location.reload();
        } else {
            alert('Error saving changes: ' + (data.message || 'Unknown error'));
            location.reload();
        }
    })
    .catch(err => {
        alert('Failed to connect to Admin Server. Make sure server.py is running instead of http.server.');
        console.error(err);
        location.reload();
    });
}
</script>
"""

def add_admin(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "toggleAdminMode()" in content:
        print(f"Admin mode already exists in {filepath}")
        return

    # Add script before </body>
    content = content.replace("</body>", admin_js + "\n</body>")
    
    # Add link to footer
    footer_text = "madamcutie1995@gmail.com</p>"
    admin_link = "<br><a href=\"javascript:toggleAdminMode()\" style=\"color: #666; text-decoration: none; font-size: 0.8rem; margin-top: 10px; display: inline-block;\">Admin Login</a>"
    content = content.replace(footer_text, footer_text + admin_link)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Admin mode added to {filepath}")

add_admin(r"c:\Users\Dell\Desktop\Saurabh\shop.html")
add_admin(r"c:\Users\Dell\Desktop\Saurabh\index.html")
