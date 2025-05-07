import numpy as np
from PIL import Image

# Mesajı gizleme fonksiyonu
def embed_message_bpcs(image_path, message, output_path):
    # Görseli aç
    img = np.array(Image.open(image_path).convert('RGB'))

    # Mesajı ikili (binary) formata çevir
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    idx = 0
    height, width, _ = img.shape
    for i in range(height):
        for j in range(width):
            if idx < len(binary_message):
                # R, G, B bileşenlerini ayrı ayrı işleyelim
                for k in range(3):  # R, G, B
                    # LSB'yi değiştir
                    new_value = (img[i, j, k] & ~1) | int(binary_message[idx])
                    
                    # Piksel değerini 0 ile 255 arasında tutmak için sınırlandırma yap
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

    # Sonuç görselini kaydet
    result_img = Image.fromarray(img)
    result_img.save(output_path)

# Örnek kullanım
embed_message_bpcs("ornek.jpeg", "Merhaba BPCS testi", "gizli_mesaj_bpcs.jpg")
