from PIL import Image, ImageDraw, ImageFont
from stegano import lsb


def Visible_Watermark(path, data):
  
  image_path = path
  text = data

  # Load the original image
  image = Image.open(image_path)

  # Define the font size, font color, and opacity of the watermark
  font_size = 500
  font_color = (255, 255, 255) # white
  opacity = 100

  # Create a new image for the watermark
  watermark = Image.new("RGBA", image.size, (0, 0, 0, 0))

  # Create a drawing context for the watermark image
  draw = ImageDraw.Draw(watermark)

  # Define the font for the watermark text
  font = ImageFont.load_default()

  # Get the size of the watermark text
  text_width, text_height = draw.textsize(text, font)

  # Calculate the position of the watermark text
  x_pos = image.size[0] - text_width - 10
  y_pos = image.size[1] - text_height - 10

  # Draw the watermark text on the watermark image
  draw.text((x_pos, y_pos), text, font=font, fill=(font_color[0], font_color[1], font_color[2], opacity))

  # Combine the original image and the watermark image
  watermarked_image = Image.alpha_composite(image.convert("RGBA"), watermark)

  # Save the watermarked image
  watermarked_image.save("watermark_img.png")
  print(f"Watermark Added Successfully 100% \non: watermark_img.png")


def Invisible_Watermark(path, data):

  image_path = path

  # Hide the secret message in the image using LSB steganography and save the result as a new image
  secret = lsb.hide(image_path, data)
  
  secret.save("Steganography_img.png")
  print(f"Secret Message Added Successfully 100% \non: Steganography_img.png")

  # Extract the hidden secret message from the steganographic image
  reveal_secret = lsb.reveal("Steganography_img.png")

  print("\nExtracted Secret Message: ", reveal_secret)  
