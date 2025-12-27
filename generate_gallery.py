
import os
import json

gallery_dir = r"c:\Users\mayod\OneDrive\Desktop\hillsview\assets\gallery"
output_file = r"c:\Users\mayod\OneDrive\Desktop\hillsview\gallery_grid.html"

categories = {
    "pool": ["pool", "umbrella", "swim", "water"],
    "restaurant": ["restaurant", "bar", "food", "kitchen", "dining", "cooking", "utensil", "spoon", "jar", "mug", "table", "chair", "seating"],
    "events": ["conference", "reception", "party", "wedding", "event", "setup", "hall"],
    "nature": ["garden", "flower", "exterior", "view", "landscape", "tree", "bush", "pathway", "gate", "signage", "gazebo"],
    "rooms": ["bedroom", "bed", "bathroom", "toilet", "shower", "sink", "mirror", "wardrobe", "desk", "interior", "accommodation", "cottage", "room", "towel", "living"]
}

html_output = []

files = sorted(os.listdir(gallery_dir))
# Filter only images
files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

for filename in files:
    name_lower = filename.lower()
    category = "nature" # Default
    
    # Simple keyword matching
    found = False
    for cat, keywords in categories.items():
        if any(k in name_lower for k in keywords):
            category = cat
            found = True
            break
            
    # Priority adjustments
    if "reception" in name_lower and category == "rooms": category = "events" # Reception fits events/public more? Or maybe "all"?
    if "cottage" in name_lower and "exterior" in name_lower: category = "nature" # Cottage exterior is nature/exterior
    
    # Generate Alt Text from filename
    alt_text = filename.replace("_", " ").replace(".jpg", "").replace(".jpeg", "").title()
    
    item_html = f'''            <div class="gallery-item reveal" data-category="{category}">
                <img src="assets/gallery/{filename}" alt="{alt_text}" loading="lazy">
                <div class="gallery-item-overlay"><span>+</span></div>
            </div>'''
    html_output.append(item_html)

full_html = "\n".join(html_output)

with open(output_file, "w") as f:
    f.write(full_html)

print(f"Generated {len(files)} gallery items.")
