import numpy as np
from PIL import Image

def embed_message_bpcs(image_path, message, output_path):
    img = np.array(Image.open(image_path).convert('RGB'))

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    idx = 0
    height, width, _ = img.shape
    for i in range(height):
        for j in range(width):
            if idx < len(binary_message):
                for k in range(3): 
                    new_value = (img[i, j, k] & ~1) | int(binary_message[idx])
                    
                    if new_value < 0:
                        new_value = 0
                    elif new_value > 255:
                        new_value = 255
                    
                    img[i, j, k] = new_value
                    idx += 1
                    if idx >= len(binary_message):
                        break
            if idx >= len(binary_message):
                break
        if idx >= len(binary_message):
            break

    result_img = Image.fromarray(img)
    result_img.save(output_path)

embed_message_bpcs("ornek.jpeg", "Merhaba BPCS testi", "gizli_mesaj_bpcs.jpg")
