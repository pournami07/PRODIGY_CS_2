from PIL import Image
from tkinter import filedialog, Tk

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
           
            r ^= key
            g ^= key
            b ^= key
            encrypted_pixels.append((r, g, b))

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    width, height = img.size
    pixels = img.load()

    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            r ^= key
            g ^= key
            b ^= key
            decrypted_pixels.append((r, g, b))

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.show()
    print("Image decrypted successfully!")

def select_image():
    root = Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename(title="Select Image",
                                            filetypes=[("Image Files", "*.png; *.jpg; *.jpeg")])
    if file_path:
        return file_path
    else:
        print("No image selected.")
        return None

# Example usage
image_path = select_image()
if image_path:
    encryption_key = 123  
    encrypt_image(image_path, encryption_key)

    encrypted_image_path = "encrypted_image.png"
    decrypt_image(encrypted_image_path, encryption_key)
