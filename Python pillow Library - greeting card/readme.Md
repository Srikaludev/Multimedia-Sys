# Greeting Card Creation with PIL

This script generates a customized Diwali greeting card using Python's (PIL) library.Please run the file as "python .\S20220010207_assign2.py" to get the output.
## Features & Steps Used

# 1. *Load and Convert Images*
- The main image (`celebration.jpg`) is loaded and converted to RGB.
- Additional images (`ganesh.jpeg` and `college.png`) are loaded and converted to RGBA.

# 2. *Image Resizing & Placement*
- The `ganesh.jpeg` image is resized to 150x150 and placed in the top-left corner.
- The `college.png` image is resized to 100x100 and placed in the top-right corner.

# 3. *Adding Text with Shadow*
- The main greeting text **"Happy Diwali!"** is added in a yellow font with a black shadow.
- The secondary text **"Have a safe and prosperous Diwali"** is added at the bottom in a similar style.

# 4. *Applying Filters*
- An **elevation effect** is created by adding a border and applying an `EMBOSS` filter.
