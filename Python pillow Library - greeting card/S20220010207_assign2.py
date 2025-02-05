from PIL import Image, ImageDraw, ImageFont
import numpy as np

input_image = Image.open("celebration.jpg").convert("RGB")
width, height = input_image.size

ganesh_image = Image.open("ganesh.jpeg").convert("RGBA")
ganesh_image_resized = ganesh_image.resize((150, 150))

input_image = input_image.convert("RGBA")
input_image.paste(ganesh_image_resized, (0, 0), ganesh_image_resized)

college_image = Image.open("college.png").convert("RGBA")
college_image_resized = college_image.resize((100, 100))

input_image.paste(college_image_resized, (width - 100, 0), college_image_resized)
input_image = input_image.convert("RGB")
text = "Happy Diwali !"
font_path = "DancingScript-VariableFont_wght.ttf"
font = ImageFont.truetype(font_path, 50)

draw = ImageDraw.Draw(input_image)
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
position = (width // 2 + (width // 2 - text_width) // 2, (height - text_height) // 2 + 50)

draw.text((position[0] + 5, position[1] + 5), text, font=font, fill="black")
draw.text(position, text, font=font, fill="yellow")

additional_text = "Have a safe and prosperous Diwali"
additional_font = ImageFont.truetype("comic.ttf", 30)

additional_text_bbox = draw.textbbox((0, 0), additional_text, font=additional_font)
additional_text_width, additional_text_height = (
    additional_text_bbox[2] - additional_text_bbox[0],
    additional_text_bbox[3] - additional_text_bbox[1],
)
additional_position = ((width - additional_text_width) // 2, height - additional_text_height - 20)

draw.text(additional_position, additional_text, font=additional_font, fill="orange")

input_image.show()

output_path = "S20220010207_diwali.png"
input_image.save(output_path, dpi=(300, 300))
