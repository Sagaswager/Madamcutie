import os
import shutil

src_dir = r"c:\Users\Dell\Desktop\Saurabh\MC UPDATED-20260612T080747Z-3-001\MC UPDATED"
dest_dir = r"c:\Users\Dell\Desktop\Saurabh\assets\images\madam"

# Clear destination directory
if os.path.exists(dest_dir):
    for f in os.listdir(dest_dir):
        os.remove(os.path.join(dest_dir, f))
os.makedirs(dest_dir, exist_ok=True)

# Copy new files
images = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
for i, img in enumerate(images):
    src_path = os.path.join(src_dir, img)
    # The original script saved as .jpg, but we should preserve extension or force .jpg.
    # To keep html links working, we should rename all to .jpg or keep original and update HTML.
    # HTML has look-01.jpg etc. Let's just name them look-XX.jpg to not break HTML.
    dest_path = os.path.join(dest_dir, f"look-{i+1:02d}.jpg")
    shutil.copy2(src_path, dest_path)
    print(f"Copied {img} to {dest_path}")
