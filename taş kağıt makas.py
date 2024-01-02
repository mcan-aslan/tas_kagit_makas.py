import random 

print("""

(0) çıkmak için
(1) taş için
(2) kağıt için
(3) makas için
""")

oyuncu = 0
bilgisayar = 0
sayilar = range(1,4)

while True:
    soru = int(input("Taş Kağıt Makas Seçim Yapın(1-3): "))
    bilgisayar_soru = random.choice(sayilar)

    if soru==0:
        print("çıkılıyor")
        break

    if soru==1:
        if bilgisayar_soru==1:
            print("ikiside taş yapar ve berabere")
            oyuncu+=1
            bilgisayar+=1
            print("Bilgisayarın Skoru: " , bilgisayar , " Oyuncunun Skoru: " , oyuncu)
        
        elif bilgisayar_soru==2:
            print("bilgisayar kazanır")
            bilgisayar +=1
            print("Bilgisayarın Skoru: " , bilgisayar , " Oyuncunun Skoru: " , oyuncu)

        else:
            print("oyuncu kazanır")
            oyuncu +=1
            print("Bilgisayarın Skoru: " , bilgisayar , " Oyuncunun Skoru: " , oyuncu)

    elif soru ==2:
        if bilgisayar_soru==1:
            print("Oyuncu Kazanır")
            oyuncu +=1
            print("Bilgisayarın Skoru: " , bilgisayar , " Oyuncunun Skoru: " , oyuncu)

        elif bilgisayar_soru==2:
            print("Berabere")
            print("Bilgisayarın Skoru: " , bilgisayar , " Oyuncunun Skoru: " , oyuncu)

        else:
            print("Bilgisayar Kazanır")
            print("Bilgisayarın Skoru: " , bilgisayar , " Oyuncunun Skoru: " , oyuncu)

    else:
        if bilgisayar_soru==1:
            print("Bilgisayar Kazanır")
            bilgisayar+=1
            print("Bilgisayarın Skoru: " , bilgisayar , " Oyuncunun Skoru: " , oyuncu)

        elif bilgisayar_soru==2:
            print("Oyuncu Kazanır")
            oyuncu += 1
            print("Bilgisayarın Skoru: " , bilgisayar , " Oyuncunun Skoru: " , oyuncu)
        
        else:
            print("berabere")
            print("Bilgisayarın Skoru: " , bilgisayar , " Oyuncunun Skoru: " , oyuncu)

