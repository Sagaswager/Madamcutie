import os

html_files = [
    r"c:\Users\Dell\Desktop\Saurabh\index.html",
    r"c:\Users\Dell\Desktop\Saurabh\shop.html",
    r"c:\Users\Dell\Desktop\Saurabh\product.html",
    r"c:\Users\Dell\Desktop\Saurabh\about.html",
    r"c:\Users\Dell\Desktop\Saurabh\contact.html"
]

bad_string = 'const currentHtml = "<!DOCTYPE html>\n" + document.documentElement.outerHTML;'
good_string = 'const currentHtml = "<!DOCTYPE html>\\n" + document.documentElement.outerHTML;'

for filepath in html_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if bad_string in content:
            content = content.replace(bad_string, good_string)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                print(f"Fixed syntax error in {filepath}")
