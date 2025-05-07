import random
import time
import os
import sys
import math
import ctypes
import matplotlib.pyplot as plt
import colorama
from colorama import Fore, Back, Style
from time import sleep

# Konsolu gizleme fonksiyonu
def gizle_konsol():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Konsolu geri açma fonksiyonu
def ac_konsol():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

# Renkli yazı için RGB fonksiyonu
def rgb_yazi(text, r, g, b):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

# Felsefi, ilham verici cümleler
animasyon_yazilari = [
    "🎲 Zarlar yuvarlanıyor...",
    "🪙 Yazı tura atılıyor...",
    "👶 Cinsiyet belirleniyor...",
    "📊 Sonuçlar hesaplanıyor...",
    "⏳ Sabır da bir bilimdir...",
    "💭 Geçmişin keşkeleri ve geleceğin endişeleri şu anımızı çalan iki hırsızdır.",
    "🌟 Hayallerinin peşinden koşan bir insan için hayat farklı bir anlama sahiptir.",
    "🧠 Doğru kararlar tecrübeden gelir; tecrübe kötü kararlardan oluşur.",
    "🕊️ Mevlana: 'Ne olursan ol yine gel!'",
    "🌀 Mevlana: 'Dert, insanı yokluğa götüren rahmettir.'",
    "🔑 Einstein: 'Hayal gücü bilgiden daha önemlidir.'",
    "🔥 Nietzsche: 'Beni öldürmeyen şey güçlendirir.'",
    "🛤️ Gandhi: 'Dünyada görmek istediğin değişimin kendisi ol.'",
    "🌌 Carl Sagan: 'Bir şeyi gerçekten anlamak istiyorsan, onu basitleştir.'",
    "📚 Konfüçyüs: 'Nereye gittiğini bilmiyorsan, vardığın yerin önemi yoktur.'"
]

# Karışık sıraya dizme
random.shuffle(animasyon_yazilari)

yazi_sayilari = []
tura_sayilari = []
kiz_sayilari = []
erkek_sayilari = []
zar_sayilari = [[] for _ in range(6)]
yazi = tura = kiz = erkek = 0
zar = [0]*6

# Ascii art logo
ascii_art = """
 ██╗ █████╗ ██╗  ██╗ █████╗ 
███║██╔══██╗██║  ██║██╔══██╗
╚██║╚██████║███████║╚█████╔╝
 ██║ ╚═══██║╚════██║██╔══██╗
 ██║ █████╔╝     ██║╚█████╔╝
 ╚═╝ ╚════╝      ╚═╝ ╚════╝ Sunar.
"""

# Simülasyon başlıyor mesajı
print(ascii_art)
print("\033[95mDeneme Sayısı Seçiniz.\033[0m")
time.sleep(1)

bar_uzunluk = 40

# Kullanıcıdan deneme sayısını alma (1000-10000 arasında)
while True:
    print(rgb_yazi("\nSeçim yapın:\n1. 1000\n2. 2000\n3. 3000\n4. 4000\n5. 5000\n6. 6000\n7. 7000\n8. 8000\n9. 9000\n10. 10000", 255, 0, 0))
    try:
        deneme_sayisi = int(input("\033[92mBir sayı girin (1-10 arası): \033[0m"))
        if 1 <= deneme_sayisi <= 10:
            deneme_sayisi = deneme_sayisi * 1000
            break
        else:
            print("\033[91mLütfen 1 ile 10 arasında bir değer girin.\033[0m")
    except ValueError:
        print("\033[91mGeçersiz giriş! Lütfen geçerli bir sayı girin.\033[0m")

# Simülasyon ve ilerleme çubuğu
for step in range(1, deneme_sayisi + 1):
    if step % 500 == 0 and animasyon_yazilari:  # Her 500 adımda bir yeni söz
        yaz = animasyon_yazilari.pop(0)  # İlk sıradaki sözü alır ve listeden çıkarır
        print("\n" + rgb_yazi(yaz, 0, 255, 255))
        time.sleep(0.4)

    # Yazı Tura
    if random.choice(["Y", "T"]) == "Y":
        yazi += 1
    else:
        tura += 1
    yazi_sayilari.append(yazi / step * 100)
    tura_sayilari.append(tura / step * 100)

    # Cinsiyet
    if random.choice(["XX", "XY"]) == "XX":
        kiz += 1
    else:
        erkek += 1
    kiz_sayilari.append(kiz / step * 100)
    erkek_sayilari.append(erkek / step * 100)

    # Zar
    gelen = random.randint(0, 5)
    zar[gelen] += 1
    for i in range(6):
        oran = zar[i] / step * 100
        if len(zar_sayilari[i]) < step:
            zar_sayilari[i].append(oran)

    # Renk geçişli bar için RGB hesaplama
    r = int((math.sin(step/50) + 1) * 127)
    g = int((math.sin(step/50 + 2) + 1) * 127)
    b = int((math.sin(step/50 + 4) + 1) * 127)

    dolu = int(bar_uzunluk * step / deneme_sayisi)
    bar = "█" * dolu + "-" * (bar_uzunluk - dolu)
    yuzde = round(step / deneme_sayisi * 100)

    sys.stdout.write(f"\r{rgb_yazi(f'|{bar}| {step}/{deneme_sayisi}  %{yuzde}', r, g, b)}")
    sys.stdout.flush()
    time.sleep(0.005 + 0.005 * math.sin(step / 100))  # yavaş-hızlı-yavaş

# Simülasyon tamamlandıktan sonra kullanıcıdan onay al
input("\n\n\033[92mSimülasyon tamamlandı. Grafiklerin açılması için 'Enter' tuşuna basın...\033[0m")

# Konsolu gizleme
gizle_konsol()

# Grafik çizimi
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Yazı-Tura Grafiği
axs[0].plot(yazi_sayilari, label=f"Yazı: %{yazi_sayilari[-1]:.2f}")
axs[0].plot(tura_sayilari, label=f"Tura: %{tura_sayilari[-1]:.2f}")
axs[0].axhline(50, color='gray', linestyle='--', label="Beklenen %50")
axs[0].set_title("Yazı Tura")
axs[0].set_xlabel("Deneme Sayısı")
axs[0].set_ylabel("Yüzde (%)")
axs[0].legend()
axs[0].grid(True)

# Zar Grafiği
renkler = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
for i in range(6):
    axs[1].plot(zar_sayilari[i], label=f"{i+1}: %{zar_sayilari[i][-1]:.2f}", color=renkler[i])
axs[1].axhline(100/6, color='gray', linestyle='--', label="Beklenen %16.67")
axs[1].set_title("Zar")
axs[1].set_xlabel("Deneme Sayısı")
axs[1].set_ylabel("Yüzde (%)")
axs[1].legend()
axs[1].grid(True)

# Cinsiyet Grafiği
axs[2].plot(kiz_sayilari, label=f"Kız: %{kiz_sayilari[-1]:.2f}")
axs[2].plot(erkek_sayilari, label=f"Erkek: %{erkek_sayilari[-1]:.2f}")
axs[2].axhline(50, color='gray', linestyle='--', label="Beklenen %50")
axs[2].set_title("Cinsiyet")
axs[2].set_xlabel("Deneme Sayısı")
axs[2].set_ylabel("Yüzde (%)")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()

# Konsolu geri açma
ac_konsol()

print("\033[92mGrafikler başarıyla oluşturuldu.\033[0m")
