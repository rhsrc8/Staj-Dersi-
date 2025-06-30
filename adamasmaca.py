import random
import os

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
--------"""]

kelimeler = ["elma", "karanfil", "gül", "armut", "şans", "çikolata", "pamuk", "türkiye", "şampiyon", "mobilya",
             "avustralya", "cezayir", "tarçin", "saglik", "kakao"]

flag = True
while flag:
    os.system("cls")
    kelime = random.choice(kelimeler)  # Rastgele bir kelime seç.
    tahmin = 6
    bulunanharfler = []  # Bulunan harflerin tutulduğu yer.
    yanlisharfler = []  # Yanlış bulunan harflerin tutulduğu yer.
    harfsayisi = len(kelime)
    x = list('_' * harfsayisi)
    print(resim[0])
    print(' '.join(x), end='\n')
    while tahmin > 0:
        if x == list(kelime):
            print("OYUNU KAZANDIN!!!")
            break
        char = input("Bir harfi veya kelimeyi tahmin edin : ").replace("İ", "i").replace("I", "ı").lower()



        if len(char) == 1:
            if char in bulunanharfler:
                os.system("cls")
                print(resim[6 - tahmin])
                print(' '.join(x), end='\n')
                print("Yanlış bulunan harfler : {}".format(yanlisharfler))
                print("Bu harfi zaten buldun!")


            elif char not in kelime:  
                tahmin -= 1
                os.system("cls")
                print(resim[6 - tahmin])
                print(' '.join(x), end='\n')
                yanlisharfler.append(char)
                print("Yanlış bulunan harfler : {}".format(yanlisharfler))
                print("\nYANLIŞ TAHMİN!!! Kalan hakkın : {}".format(tahmin))

            else:
                for i in range(len(kelime)):
                    if char == kelime[i]:
                        os.system("cls")
                        print(resim[6 - tahmin])

                        x[i] = char
                        bulunanharfler.append(char)
                print(' '.join(x), end='\n')
                print("Yanlış bulunan harfler : {}".format(yanlisharfler))
                print("\nDOĞRU TAHMİN!!! Kalan hakkın : {}".format(tahmin))


        elif len(char) > 0:
            if char == kelime:
                print("\nTEBRİKLER!!! Kelimeyi buldunuz.")
                devam = input("Tekrar oynamak ister misiniz? [e/h]")
                if devam == "e" or devam == "E":
                    flag = True
                    break
                else:
                    flag = False
                    break

            else:
                tahmin -= 1
                os.system("cls")
                print(resim[6 - tahmin])
                print(' '.join(x), end='\n')
                print("Yanlış bulunan harfler : {}".format(yanlisharfler))
                print("\nYANLIŞ TAHMİN!!! Kalan hakkın : {}".format(tahmin))



        if tahmin== 0:
            print("\nTahmin hakkiniz kalmadi. Kaybettiniz! Adam Asildi.")
            print(f"Doğru kelime : {kelime}")
            devam = input("Tekrar oynamak ister misiniz? [e/h]")
            if devam == "e" or devam == "E":
                flag = True
            else:
                flag = False