import glob
import os

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('href="css/', 'href="/css/')
    content = content.replace('src="assets/', 'src="/assets/')
    content = content.replace('src="js/', 'src="/js/')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated paths in HTML files.")
