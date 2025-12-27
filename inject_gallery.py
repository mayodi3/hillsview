
import os

gallery_file = r"c:\Users\mayod\OneDrive\Desktop\hillsview\gallery.html"
grid_file = r"c:\Users\mayod\OneDrive\Desktop\hillsview\gallery_grid.html"

with open(gallery_file, "r", encoding="utf-8") as f:
    gallery_lines = f.readlines()

with open(grid_file, "r", encoding="utf-8") as f:
    grid_content = f.read()

# Find the injection range
start_index = -1
end_index = -1

for i, line in enumerate(gallery_lines):
    if 'id="galleryGrid"' in line:
        start_index = i + 1 # Insert after the opening div
    if start_index != -1 and i > start_index and line.strip() == "</div>":
        # We need to find the matching closing div for gallery-masonry
        # Based on indentation, gallery-masonry has 12 spaces (referenced from prev view)
        # But let's check indentation of the start line
        if len(gallery_lines[start_index-1]) - len(gallery_lines[start_index-1].lstrip()) == len(line) - len(line.lstrip()):
             end_index = i
             break

if start_index != -1 and end_index != -1:
    print(f"Found injection point: lines {start_index+1} to {end_index}")
    
    new_lines = gallery_lines[:start_index]
    new_lines.append(grid_content + "\n")
    new_lines.extend(gallery_lines[end_index:])
    
    with open(gallery_file, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("Successfully injected gallery grid.")
else:
    print("Could not find injection point.")
    print(f"Start: {start_index}, End: {end_index}")
