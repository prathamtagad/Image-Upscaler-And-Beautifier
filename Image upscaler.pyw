import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageEnhance

def enhance_and_upscale_image():
    input_image_path = input_path_entry.get()
    output_image_path = output_path_entry.get()
    sharpness_factor = float(sharpness_scale.get())
    color_factor = float(color_scale.get())
    scale_factor = float(scale_scale.get())

    # Open the image using Pillow
    image = Image.open(input_image_path)

    # Apply sharpness enhancement
    sharpness = ImageEnhance.Sharpness(image)
    image = sharpness.enhance(sharpness_factor)

    # Apply color enhancement
    color = ImageEnhance.Color(image)
    image = color.enhance(color_factor)

    # Calculate the new dimensions after upscaling
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)

    # Use the `resize` method to upscale the image
    image = image.resize((new_width, new_height), Image.LANCZOS)

    # Save the enhanced and upscaled image
    image.save(output_image_path)

    result_label.config(text="Image processed and saved!")

def browse_input_image():
    file_path = filedialog.askopenfilename()
    input_path_entry.delete(0, tk.END)
    input_path_entry.insert(0, file_path)

def browse_output_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, file_path)

# Create the main window
root = tk.Tk()
root.title("Upscaller and Beautifyer By Pratham")

# Input and output path entry widgets
input_label = tk.Label(root, text="Input Image:")
input_label.pack()
input_path_entry = tk.Entry(root)
input_path_entry.pack()
input_browse_button = tk.Button(root, text="Browse", command=browse_input_image)
input_browse_button.pack()

output_label = tk.Label(root, text="Output Image:")
output_label.pack()
output_path_entry = tk.Entry(root)
output_path_entry.pack()
output_browse_button = tk.Button(root, text="Browse", command=browse_output_image)
output_browse_button.pack()

# Enhancement parameters
sharpness_label = tk.Label(root, text="Sharpness Factor:")
sharpness_label.pack()
sharpness_scale = tk.Scale(root, from_=0.1, to=3.0, resolution=0.1, orient=tk.HORIZONTAL, length=200)
sharpness_scale.set(1.5)
sharpness_scale.pack()

color_label = tk.Label(root, text="Color Factor:")
color_label.pack()
color_scale = tk.Scale(root, from_=0.1, to=3.0, resolution=0.1, orient=tk.HORIZONTAL, length=200)
color_scale.set(1.5)
color_scale.pack()

# Upscaling factor
scale_label = tk.Label(root, text="Scale Factor:")
scale_label.pack()
scale_scale = tk.Scale(root, from_=1.0, to=4.0, resolution=0.1, orient=tk.HORIZONTAL, length=200)
scale_scale.set(2.0)
scale_scale.pack()

# Process button
process_button = tk.Button(root, text="Upscale", command=enhance_and_upscale_image)
process_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()

# Made by pratham tagad please do not user it for selling!!