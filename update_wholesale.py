import os, glob
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('<a href="wholesale.html">For Wholesale</a>', '<a href="https://wa.me/919911852113" target="_blank">For Wholesale</a>')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
