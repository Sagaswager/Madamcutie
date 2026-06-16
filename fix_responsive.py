import re

def update_css():
    with open('css/style.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # Layout Utilities
    css = re.sub(
        r'\.container\s*\{\s*max-width:\s*var\(--container-width\);\s*margin:\s*0\s*auto;\s*padding:\s*0\s*40px;\s*\}\s*@media\s*\(max-width:\s*768px\)\s*\{\s*\.container\s*\{\s*padding:\s*0\s*20px;\s*\}\s*\}',
        '.container {\n    width: 100%;\n    max-width: var(--container-width);\n    margin: 0 auto;\n    padding: 0 20px;\n}\n\n@media (min-width: 768px) {\n    .container {\n        padding: 0 40px;\n    }\n}',
        css
    )

    css = re.sub(
        r'\.section\s*\{\s*padding:\s*var\(--spacing-xl\)\s*0;\s*\}\s*@media\s*\(max-width:\s*768px\)\s*\{\s*\.section\s*\{\s*padding:\s*var\(--spacing-lg\)\s*0;\s*\}\s*\}',
        '.section {\n    padding: var(--spacing-lg) 0;\n}\n\n@media (min-width: 768px) {\n    .section {\n        padding: var(--spacing-xl) 0;\n    }\n}',
        css
    )

    css = re.sub(
        r'\.grid-2\s*\{\s*grid-template-columns:\s*repeat\(2,\s*1fr\);\s*\}\s*\.grid-3\s*\{\s*grid-template-columns:\s*repeat\(3,\s*1fr\);\s*\}\s*\.grid-4\s*\{\s*grid-template-columns:\s*repeat\(4,\s*1fr\);\s*\}\s*@media\s*\(max-width:\s*1024px\)\s*\{\s*\.grid-4\s*\{\s*grid-template-columns:\s*repeat\(2,\s*1fr\);\s*\}\s*\.grid-3\s*\{\s*grid-template-columns:\s*repeat\(2,\s*1fr\);\s*\}\s*\}\s*@media\s*\(max-width:\s*600px\)\s*\{\s*\.grid-2,\s*\.grid-3,\s*\.grid-4\s*\{\s*grid-template-columns:\s*repeat\(2,\s*1fr\);\s*gap:\s*10px;\s*\}\s*\}',
        '.grid-2, .grid-3, .grid-4 {\n    grid-template-columns: 1fr;\n}\n@media (min-width: 600px) {\n    .grid-2, .grid-3, .grid-4 {\n        grid-template-columns: repeat(2, 1fr);\n    }\n}\n@media (min-width: 1024px) {\n    .grid-3 {\n        grid-template-columns: repeat(3, 1fr);\n    }\n    .grid-4 {\n        grid-template-columns: repeat(4, 1fr);\n    }\n}',
        css
    )

    # Categories
    css = re.sub(
        r'\.categories-grid\s*\{\s*display:\s*grid;\s*grid-template-columns:\s*repeat\(4,\s*1fr\);\s*gap:\s*var\(--spacing-md\);\s*margin-top:\s*var\(--spacing-lg\);\s*\}\s*@media\s*\(max-width:\s*1024px\)\s*\{\s*\.categories-grid\s*\{\s*grid-template-columns:\s*repeat\(2,\s*1fr\);\s*\}\s*\}\s*@media\s*\(max-width:\s*600px\)\s*\{\s*\.categories-grid\s*\{\s*grid-template-columns:\s*1fr;\s*\}\s*\}',
        '.categories-grid {\n    display: grid;\n    grid-template-columns: 1fr;\n    gap: var(--spacing-md);\n    margin-top: var(--spacing-lg);\n}\n@media (min-width: 600px) {\n    .categories-grid {\n        grid-template-columns: repeat(2, 1fr);\n    }\n}\n@media (min-width: 1024px) {\n    .categories-grid {\n        grid-template-columns: repeat(4, 1fr);\n    }\n}',
        css
    )

    # Search bar absolute fix
    css += "\n\n@media (max-width: 768px) {\n    #search-bar-container form {\n        flex-direction: column;\n    }\n    #search-bar-container input {\n        width: 100%;\n    }\n    #search-bar-container button {\n        width: 100%;\n    }\n}\n"
    
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix hero inline styles
    html = html.replace('width: 400px; height: 400px;', 'width: 40vw; height: 40vw; max-width: 400px; max-height: 400px; min-width: 250px; min-height: 250px;')
    html = html.replace('width: 600px; height: 600px;', 'width: 60vw; height: 60vw; max-width: 600px; max-height: 600px; min-width: 300px; min-height: 300px;')
    
    # Overlay width
    html = re.sub(
        r'width:\s*50%;',
        r'width: 100%; max-width: 600px;',
        html,
        count=1
    )
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    update_css()
    update_html()
    print("Done")
