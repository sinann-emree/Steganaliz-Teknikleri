import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_stego(original_path, stego_path):
    original = cv2.imread(original_path)
    stego = cv2.imread(stego_path)

    if original is None or stego is None:
        print("Görseller yüklenemedi.")
        return

    diff = cv2.absdiff(original, stego)

    orig_hist = cv2.calcHist([original], [0], None, [256], [0, 256])
    stego_hist = cv2.calcHist([stego], [0], None, [256], [0, 256])

    orig_lsb = original & 1
    stego_lsb = stego & 1
    lsb_diff = np.abs(orig_lsb - stego_lsb)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.title("Orijinal Görsel")
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.title("Gizli Mesajlı Görsel")
    plt.imshow(cv2.cvtColor(stego, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.title("Fark Görüntüsü")
    plt.imshow(diff)
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.title("LSB Farkı Sayısı")
    plt.hist(lsb_diff.ravel(), bins=2, range=(0, 2), color='gray', edgecolor='black')
    plt.xticks([0, 1])
    plt.xlabel("LSB Değeri Farkı")
    plt.ylabel("Piksel Sayısı")

    plt.tight_layout()
    plt.show()

analyze_stego("ornek.jpeg", "gizli_mesaj_maskeli.jpg")
