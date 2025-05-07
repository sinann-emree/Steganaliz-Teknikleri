import numpy as np
import cv2
from scipy.fftpack import dct, idct

def embed_message(image_path, message, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    dct_img = dct(dct(img.T, norm='ortho').T, norm='ortho')

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    if len(binary_message) > dct_img.size:
        raise ValueError("Mesaj görselin kapasitesini aşıyor!")
    
    idx = 0
    for i in range(dct_img.shape[0]):
        for j in range(dct_img.shape[1]):
            if idx < len(binary_message):
                dct_img[i][j] = int(dct_img[i][j]) & ~1 | int(binary_message[idx])
                idx += 1

    idct_img = idct(idct(dct_img.T, norm='ortho').T, norm='ortho')

    idct_img = np.uint8(np.clip(idct_img, 0, 255))

    cv2.imwrite(output_path, idct_img)

embed_message("ornek.jpg", "Merhaba bu bir testtir", "gizli_mesaj.jpg")
