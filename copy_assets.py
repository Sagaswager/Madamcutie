import os
import shutil
from PIL import Image
import json

def main():
    src_dir = r"C:\Users\Dell\Desktop\Saurabh\Madam-20260608T082228Z-3-001\Madam"
    dest_dir = r"C:\Users\Dell\Desktop\Saurabh\assets\images\products"
    logo_src = r"C:\Users\Dell\Desktop\Saurabh\Logo.jpeg"
    logo_dest = r"C:\Users\Dell\Desktop\Saurabh\assets\images\logo.jpg"
    
    # Create directories
    os.makedirs(dest_dir, exist_ok=True)
    os.makedirs(r"C:\Users\Dell\Desktop\Saurabh\assets\images", exist_ok=True)
    os.makedirs(r"C:\Users\Dell\Desktop\Saurabh\css", exist_ok=True)
    os.makedirs(r"C:\Users\Dell\Desktop\Saurabh\js", exist_ok=True)
    
    # Copy logo
    if os.path.exists(logo_src):
        shutil.copy(logo_src, logo_dest)
        print("Copied logo to", logo_dest)
        
    # Categories to distribute the 36 images into
    categories = ["Dresses", "Tops & Shirts", "Outerwear", "Bottoms", "Accessories"]
    
    # Let's inspect each image
    products = []
    files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    
    print(f"Found {len(files)} files to copy...")
    
    for i, filename in enumerate(files):
        src_path = os.path.join(src_dir, filename)
        dest_filename = filename.lower()
        dest_path = os.path.join(dest_dir, dest_filename)
        
        # Copy file
        shutil.copy(src_path, dest_path)
        
        # Open image to get size
        try:
            with Image.open(src_path) as img:
                width, height = img.size
                ratio = height / width
        except Exception as e:
            print(f"Error reading image {filename}: {e}")
            width, height = 0, 0
            ratio = 1.0
            
        # Distribute into categories and make up product names
        cat = categories[i % len(categories)]
        price = 29.99 + (i * 5) % 120
        rating = 4.0 + (i * 0.17) % 1.0
        reviews = 12 + (i * 7) % 140
        
        # Determine name based on category
        if cat == "Dresses":
            name = f"Elegant Floral Dress {100 + i}"
            desc = "A stunning elegant floral dress designed for special occasions, featuring premium light breathable fabric, detailed neckline, and a flattering waistline."
        elif cat == "Tops & Shirts":
            name = f"Classic Silk Blouse {200 + i}"
            desc = "Sophisticated silk blouse perfect for corporate wear or casual outings. Soft texture with custom stitching and button details."
        elif cat == "Outerwear":
            name = f"Premium Trench Coat {300 + i}"
            desc = "All-season premium trench coat designed for comfort and style. Water-resistant outer shell with elegant pocket designs."
        elif cat == "Bottoms":
            name = f"Tailored Slim-Fit Trousers {400 + i}"
            desc = "Perfectly tailored trousers with side pockets and a high rise. Made of high-quality stretchable fabric for maximum comfort."
        else: # Accessories
            name = f"Luxury Leather Handbag {500 + i}"
            desc = "Premium genuine leather bag with spacious compartments and a modern design. Adjustable strap and durable hardware."
            
        products.append({
            "id": f"p{i+1}",
            "name": name,
            "category": cat,
            "price": float(f"{price:.2f}"),
            "rating": float(f"{rating:.1f}"),
            "reviews": reviews,
            "description": desc,
            "image": f"assets/images/products/{dest_filename}",
            "width": width,
            "height": height,
            "ratio": ratio,
            "in_stock": True,
            "featured": (i % 6 == 0)
        })
        
    # Write products database to json file
    with open(r"C:\Users\Dell\Desktop\Saurabh\js\products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4)
        
    # Also write a script file JS to expose this data as a global variable
    with open(r"C:\Users\Dell\Desktop\Saurabh\js\products.js", "w", encoding="utf-8") as f:
        f.write("const PRODUCTS = ")
        json.dump(products, f, indent=4)
        f.write(";\n")
        
    print(f"Copied {len(products)} products and generated database.")

if __name__ == '__main__':
    main()
