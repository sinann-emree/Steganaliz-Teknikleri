import cv2
import numpy as np

def embed_message_masking_filtering(image_path, message, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Görsel yüklenemedi. Dosya adını ve uzantısını kontrol edin.")
        return

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    msg_len = len(binary_message)

    height, width, _ = img.shape
    max_capacity = height * width * 3

    if msg_len > max_capacity:
        print("Mesaj görsele sığmıyor!")
        return

    idx = 0
    mask = np.uint8(~1)  

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)  

    for i in range(height):
        for j in range(width):
            if edges[i, j] != 0:  
                for k in range(3):  
                    if idx < msg_len:
                        bit = int(binary_message[idx])
                        img[i, j, k] = (img[i, j, k] & mask) | bit
                        idx += 1

    cv2.imwrite(output_path, img)
    print("Mesaj başarıyla gizlendi:", output_path)

embed_message_masking_filtering("ornek.jpeg", "Merhaba bu kenarlarda!", "gizli_mesaj_maskeli.jpg")
