#Kapsamli Sifre Uygulamasi Python 101

# ord("A) = ascı karakter karsiligini getir   chr(65) = bu no'lu karakteri getir

import string
import os

alfabe=string.ascii_lowercase
max_karakter=len(alfabe)


def secenekler():
    while True:
        secenek=input("Ne yapmak istersiniz : ").lower()
        if secenek in("sifrele","sifreleme","sifreleme yap","sifreleme yapmak","sifre","sifreleme yapmak isterim"):
            sifreleme()
        elif secenek in("sifre cöz","sifreyi cöz","sifreyi coz","sifre coz"):
            sifre_coz()
        else:
            print("Şifreleme yapmak için %s yazın, Sifre cözmek icin %s yazın" % ("sifrele","sifre cöz"))



def sifreleme():
    metin=input("Şifrelenecek metni girin : ").lower()
    sifreleme_anahtari=sifrelemeAnahtari()
    sifrelenmis_metin=""
    for karakter in metin:
        if karakter.isalpha():
            karakter_sira_no=ord(karakter)
            karakter_sira_no+=sifreleme_anahtari
            if karakter_sira_no>ord("z"):
                karakter_sira_no-=max_karakter

            elif karakter_sira_no<ord("a"):
                karakter_sira_no+=max_karakter

            sifreli_karakter=chr(karakter_sira_no)
            sifrelenmis_metin+=sifreli_karakter
        else:
            sifrelenmis_metin+=karakter
    print("%s kelimesinin %d anahtarı ile sifrelenmis hali = %s" % (metin,sifreleme_anahtari,sifrelenmis_metin))
    input("Devam etmek için bir tuşa basınız.")


def sifre_coz():
    sifreli_metin=input("Cozulecek Sifreli metni girin : ").lower()
    sifreleme_anahtari=sifrelemeAnahtari()
    cozulmus_metin=""
    for karakter in sifreli_metin:
        if karakter.isalpha():
            karakter_sira_no=ord(karakter)
            karakter_sira_no-=sifreleme_anahtari
            if karakter_sira_no>ord("z"):
                karakter_sira_no-=max_karakter

            elif karakter_sira_no<ord("a"):
                karakter_sira_no+=max_karakter

            cozulmus_karakter=chr(karakter_sira_no)
            cozulmus_metin+=cozulmus_karakter
        else:
            cozulmus_metin+=karakter
    print("%s sifreli metnin %d anahtarı ile cozulmus hali  =   %s" % (sifreli_metin,sifreleme_anahtari,cozulmus_metin))
    input("Devam etmek için bir tuşa basınız.")



def sifrelemeAnahtari():
    anahtar=int(input("Sifreleme anahtarı girin (1-%s) : "% max_karakter))
    if anahtar>=1 and anahtar<=max_karakter:
        return anahtar
    else:
        return 1




secenekler()