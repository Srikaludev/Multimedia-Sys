from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip, ImageClip
from PIL import Image, ImageDraw, ImageFont

# Function to create text image
def create_text_image(text, font_size, image_size, color="white", bgcolor="black"):
    img = Image.new("RGB", image_size, bgcolor)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Use a default font
    except:
        font = ImageFont.load_default()  # Fallback if font file isn't found

    text_size = draw.textbbox((0, 0), text, font=font)
    text_x = (image_size[0] - text_size[2]) // 2
    text_y = (image_size[1] - text_size[3]) // 2
    draw.text((text_x, text_y), text, font=font, fill=color)
    
    return img

# Create text overlays as images
text_overlay_img = create_text_image("Animal X Devara", 70, (920, 200))
caption_img = create_text_image("captions", 50, (920, 100))

# Save images temporarily
text_overlay_img.save("text_overlay.png")
caption_img.save("caption.png")

# Load the video and audio files
video = VideoFileClip("Devara.mp4")
audio = AudioFileClip("bgm.mp3")
video = video.set_audio(audio)

# Create text overlays as ImageClips
text_overlay = ImageClip("text_overlay.png").set_duration(5).set_position('center')
caption = ImageClip("caption.png").set_start(10).set_duration(5).set_position('bottom')

# Combine video with text overlays
video = CompositeVideoClip([video, text_overlay, caption])

# Save the video with new audio and text overlays
video.write_videofile("Devara_with_bgm.mp4", codec="libx264", audio_codec="aac")

# Load the videos to be merged
video1 = VideoFileClip("Devara_with_bgm.mp4")
video2 = VideoFileClip("Animal.mp4")

# Concatenate videos
final_video = concatenate_videoclips([video1, video2])

# Save the final merged video
final_video.write_videofile("Merged_Video.mp4", codec="libx264", audio_codec="aac")
