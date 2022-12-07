import random

def kayit():
    print("********************HESAP AÇMA EKRANI********************")
    username = random.randint(0,999999999)
    print("Hesap NO : {}".format(username))
    password = input("Şifrenizi Giriniz : ")
    file = open("veriler.txt","a")
    file.write(str(username))
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    print("Hesap Numaranız {} Bu numarayı kayıt etmenizi tavsiye ederiz.".format(username))
    guncelleme()

# def giris():
#     username = input("Hesap Numaranızı Giriniz :" )
#     password = input("Şifrenizi Gİriniz : ")
#     for line in open("veriler.txt","r").readlines():
#         giris_bilgisi = line.split()
#         if username == giris_bilgisi[0] and password == giris_bilgisi[1]:
#             print("Hoşgeldiniz {}".format(username))
#             return True
#     print("Hesap Numarası Veya Şifre Yanlış")
#     return False
    
def guncelleme():
    bakiye = 100
    username = input("Kullanıcı adını gir")
    for line in open("veriler.txt","r").readlines():
        kontrol = line.split()
        if username == kontrol[0]:
            print("Bulduğun isim {}".format(kontrol))
            file = open("veriler.txt","a")
            file.write(" ")
            file.write("Bakiye")
            file.close()
        
guncelleme()
