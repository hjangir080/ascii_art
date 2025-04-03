import time
from PIL import Image

# ASCII characters used for the ASCII art, arranged in increasing intensity
ASCII_CHARS = "@%#+=.- "

def resize_image(image, new_width):
    """Resize image while adjusting for ASCII character proportions."""
    width, height = image.size
    # ASCII characters have a typical height-to-width ratio of approximately 2. Adjust accordingly
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.5)  # Scaling height down for proper proportions
    return image.resize((new_width, new_height))

def image_to_ascii(image, width=100):
    """Convert an image to ASCII art."""
    # Resize the image
    image = resize_image(image, width)

    # Convert the image to grayscale
    gray_image = image.convert("L")
    pixels = gray_image.getdata()

    # Map each pixel to an ASCII character
    ascii_str = ""
    for pixel in pixels:
        index = min(len(ASCII_CHARS) - 1, pixel // 25)
        ascii_str += ASCII_CHARS[index]

    # Format the ASCII string into the same dimensions as the resized image
    ascii_art = ""
    for i in range(0, len(ascii_str), width):
        ascii_art += ascii_str[i:i + width] + "\n"

    return ascii_art

def main():
    path = 'Lenna.png'
    try:
        start_time = time.time()  # Start time
        image = Image.open(path)
        ascii_art = image_to_ascii(image)
        end_time = time.time()  # End time
        print(ascii_art)
        print(f"Execution time: {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
