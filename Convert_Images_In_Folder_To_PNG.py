import os
import time
from PIL import Image

# Prompt the user to enter the input folder path
input_folder_path = input("Enter the path to the folder containing the images to convert: ")

# Prompt the user to enter the output folder path
output_folder_path = input("Enter the path to the folder to save the converted images: ")

# Get the list of image files to convert
image_files = [filename for filename in os.listdir(input_folder_path) if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".bmp")]
num_images = len(image_files)

# Define the progress bar colors and animation frames
colors = ["\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m"]
frames = ["░", "▒", "▓", "█"]

# Initialize the progress bar
progress_bar_width = 50
print("Converting images:")
print("[" + " " * progress_bar_width + "] 0%  ", end="")

# Loop through all the image files and convert them
for i, filename in enumerate(image_files):
    # Open the image and convert it to PNG
    image = Image.open(os.path.join(input_folder_path, filename))
    png_filename = os.path.splitext(filename)[0] + ".png"
    png_filepath = os.path.join(output_folder_path, png_filename)
    image.save(png_filepath, "png")
    
    # Update the progress bar
    progress = (i + 1) / num_images
    num_filled = int(progress * progress_bar_width)
    num_empty = progress_bar_width - num_filled
    color = colors[i % len(colors)]
    frame = frames[i % len(frames)]
    print("\r" + color + "[" + frame * num_filled + " " * num_empty + "]" + "\033[0m" + " {:.0%}  ".format(progress), end="")
    time.sleep(0.1)  # Add a delay to make the animation more visible

# Display a smiley face with sunglasses when the conversion is complete
print("\n\nImage conversion complete! 😎😎😎\n")

