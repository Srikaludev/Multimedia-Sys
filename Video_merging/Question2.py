import cv2
import numpy as np
from moviepy.editor import (
    VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip, ImageClip
)
from PIL import Image, ImageDraw, ImageFont

def resize_frame(frame, newsize):
    return cv2.resize(frame, newsize, interpolation=cv2.INTER_LINEAR)

# Function to resize the entire clip
def resize_clip(clip, newsize):
    return clip.fl_image(lambda frame: resize_frame(frame, newsize))

# Load and trim video clips
clip1 = VideoFileClip("sample1.mp4").subclip(0, 10)  # First 10 seconds of sample1.mp4
clip2 = VideoFileClip("sample2.mp4").subclip(0, 10)  # First 10 seconds of sample2.mp4

# Define resolution
desired_resolution = (1920, 1080)

# Resize clips
clip1 = resize_clip(clip1, desired_resolution)
clip2 = resize_clip(clip2, desired_resolution)

# Merge both clips into a 20s video
merged_video = concatenate_videoclips([clip1, clip2])

# Load background audio (first 10s only)
background_audio = AudioFileClip("background.mp3").subclip(0, 10)

# Apply background audio only to the first 10 seconds of the merged video
merged_video = merged_video.set_audio(background_audio.set_duration(10))

# Function to create text image using PIL
def create_text_image(text, fontsize, size, color):
    img = Image.new("RGBA", size, (0, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(img)

    # Load font (ensure Arial or another .ttf font is available)
    font = ImageFont.truetype("arial.ttf", fontsize)

    # Calculate text position (centered)
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)

    # Draw text
    draw.text(position, text, font=font, fill=color)
    
    return img

# Function to create text clip
def create_text_clip(text, fontsize, size, color, duration):
    img = create_text_image(text, fontsize, size, color)
    return ImageClip(np.array(img)).set_duration(duration)

# Create text overlay (first 2 seconds)
intro_text = create_text_clip("Welcome to My Remix! ->Srikar", 70, desired_resolution, "white", 2)

# Create caption at the 10th second
caption_text = create_text_clip("Enjoy the Video->Devara X RRR!", 50, desired_resolution, "yellow", 5)
caption_text = caption_text.set_position(('center', 'bottom')).set_start(10)

# Overlay text and caption on the final video
final_video = CompositeVideoClip([merged_video, intro_text.set_start(0), caption_text])

# Write final video file (20 seconds total)
final_video.write_videofile("final_video.mp4", codec='libx264', bitrate='2000k', fps=24)
