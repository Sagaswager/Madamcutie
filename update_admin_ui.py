import re

html_files = [
    r"c:\Users\Dell\Desktop\Saurabh\index.html",
    r"c:\Users\Dell\Desktop\Saurabh\shop.html",
    r"c:\Users\Dell\Desktop\Saurabh\product.html",
    r"c:\Users\Dell\Desktop\Saurabh\about.html",
    r"c:\Users\Dell\Desktop\Saurabh\contact.html"
]

new_admin_js = """
<!-- Admin Mode Script -->
<script>
function toggleAdminMode() {
    const isActive = localStorage.getItem('adminMode') === 'true';
    localStorage.setItem('adminMode', !isActive);
    if (!isActive) {
        window.location.href = 'index.html';
    } else {
        location.reload();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('adminMode') === 'true') {
        const toolbar = document.createElement('div');
        toolbar.id = 'admin-toolbar';
        toolbar.style.cssText = 'position: fixed; top: 0; left: 0; width: 100%; background: #111; color: #fff; padding: 15px 20px; z-index: 10000; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 15px rgba(0,0,0,0.5); font-family: sans-serif; border-bottom: 3px solid #d4af37;';
        toolbar.innerHTML = `
            <div style="font-weight: bold; font-size: 16px; letter-spacing: 1px; color: #d4af37;">
                ⚙️ ADMIN MODE ACTIVE - Click directly on any highlighted text below to edit it!
            </div>
            <div>
                <button onclick="saveChanges()" style="background: #d4af37; color: #fff; border: none; padding: 8px 20px; margin-right: 10px; cursor: pointer; font-weight: bold; border-radius: 4px; font-size: 14px;">Save All Changes</button>
                <button onclick="toggleAdminMode()" style="background: #fff; color: #111; border: none; padding: 8px 20px; cursor: pointer; font-weight: bold; border-radius: 4px; font-size: 14px;">Exit Admin</button>
            </div>
        `;
        document.body.prepend(toolbar);
        
        // Add top padding to body so toolbar doesn't cover header
        document.body.style.paddingTop = '60px';

        const titles = document.querySelectorAll('.madam-card h3 a');
        const descriptions = document.querySelectorAll('.madam-card p:nth-of-type(2)');
        const prices = document.querySelectorAll('.madam-card span:last-child');

        [...titles, ...descriptions, ...prices].forEach(el => {
            el.contentEditable = "true";
            // Make them extremely obvious
            el.style.border = "2px dashed #ff0000";
            el.style.backgroundColor = "rgba(255, 255, 0, 0.2)";
            el.style.padding = "4px";
            el.style.borderRadius = "4px";
            el.style.outline = "none";
            el.style.cursor = "text";
            el.style.minHeight = "20px";
            el.style.display = "inline-block";
            
            el.addEventListener('focus', function() {
                this.style.backgroundColor = 'rgba(255, 255, 0, 0.5)';
            });
            el.addEventListener('blur', function() {
                this.style.backgroundColor = 'rgba(255, 255, 0, 0.2)';
            });
        });
    }
});

function saveChanges() {
    const btn = document.querySelector('#admin-toolbar button');
    btn.textContent = 'Saving...';
    const toolbar = document.getElementById('admin-toolbar');
    if (toolbar) toolbar.remove();
    
    document.body.style.paddingTop = '';
    
    document.querySelectorAll('[contenteditable="true"]').forEach(el => {
        el.removeAttribute('contenteditable');
        el.style.border = '';
        el.style.backgroundColor = '';
        el.style.padding = '';
        el.style.borderRadius = '';
        el.style.outline = '';
        el.style.cursor = '';
        el.style.minHeight = '';
        el.style.display = (el.tagName === 'A' || el.tagName === 'SPAN') ? '' : el.style.display;
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
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'<!-- Admin Mode Script -->.*?</script>', new_admin_js, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated admin script to be much more obvious.")
