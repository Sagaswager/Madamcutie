import os
import shutil

dir_to_remove = r"c:\Users\Dell\Desktop\Saurabh\assets\images\products"

if os.path.exists(dir_to_remove):
    shutil.rmtree(dir_to_remove)
    print("Removed all old photos in assets/images/products.")
else:
    print("Directory already removed.")
