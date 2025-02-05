import random
import os
sayaç=0
print("Sayı Tahmin Etme Oyununa Hoşgeldiniz\n")
def ccls():
    os.system("cls" if os.name=="nt" else "clear")
while True:
    try:
        eh=input("Bilgilendirme için (e) giriniz: ")
        if eh  not in  ("", "e","h"):
            raise ValueError
    except (ValueError,TypeError) as e:
        print("Lütfen yalnızca e ya da h kullanın.")
    else:
        if eh=="e":
            print("\n1) Oyunda 1-100 arası bir sayı tahmin edeceksiniz.\n2) Oyunda maksimum 10 tahmin hakkı alabilirsiniz.\n3) Oyunda kolaylık olsun diye ilk turda yukarı-aşağı denilecek\n4) Oyunda uzaklaşma ve yaklaşma komutları sadece BİR ÖNCEKİ tahmine göre verilir!\n")
            break
        else:
            ccls()
            break
input("\nHazır olduğunuz zaman herhangi bir tuşa basın! ")
ccls()
oynanmasayısı=0
while True:
    if oynanmasayısı>0:
        try:
            eh=input("\nTekrar oynamak için e giriniz çıkmak için h giriniz: ")
            if eh not in ("","h","e"):
                raise ValueError
        except (ValueError,TypeError) as e:
            print("\nLütfen yalnızca e ya da h giriniz!")
        else:
            if eh=="e":
                pass
            else:
                ccls()
                print("İyi günler dilerim!")
                break
    oynanmasayısı=1
    while True:
        try:
            hak=int(input("İstediğinizi hak miktarı: "))
            if hak>10:
                print("\nMaksimum alınacak hak sayısı 10'dan fazla olamaz.")
                raise ValueError
            elif hak<=0:
                print("Hak sayısı 0 veya daha az bir sayı olamaz.")
                raise ValueError
        except (ValueError,TypeError) as e:
            print("\nYalnızca sayısal ifade giriniz.")
        else:
            ccls()
            break
    soru=random.randint(1,100)
    sayaç=0
    fark=None
    eskifark=None
    while hak>=0:
        if hak==1:
            input("\nDikkat bu son hakkın! Devam etmek için bir tuş gir. ")
        if hak==0:
            ccls()
            print(f"Oyunu kazanamadınız! :( Bulmanız gereken sayı: {soru})")
            break
        print("\n")
        try:
            tahmin=int(input("Tahmininiz: "))
            if tahmin>100:
                input("Aradığınız sayı yüzden fazla olamaz. Devam etmek için entera basın!")
                raise ValueError
            elif tahmin<0:
                input("Aradığınız sayı sıfırdan az olamaz. Devam etmek için entera basın!")
                raise ValueError
        except (ValueError,TypeError) as e:
            print("Yalnızca sayısal ifade girin!")
        else:
            sayaç+=1
            fark=abs(soru-tahmin)
            if fark==0:
                ccls()
                print(f"Tebrikler!!!!! Oyunuz kazandınız! Bulunan sayı {soru}, kaçıncı tahminde buldunuz: {sayaç}")
                break
            elif eskifark is None:
                if tahmin<soru:
                    print("\nGüzel deneme! Şimdi yukarı doğru git!")
                    eskifark=fark
                else:
                    print("\nGüzel deneme! Şimdi aşağı git!")
                    eskifark=fark
            elif fark>eskifark:
                print(f"Uzaklaşıyorsun! Kalan hak: {hak-1}")
            elif fark<eskifark:
                print(f"Yaklaşıyorsun! Kalan hak: {hak-1}")
            elif fark==eskifark:
                print(f"Aynı uzaklık ☠️ Kalan hak: {hak-1}")
            eskifark=fark
            hak-=1
