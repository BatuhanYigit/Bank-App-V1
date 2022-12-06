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
    giris()

def giris():
    username = input("Hesap Numaranızı Giriniz :" )
    password = input("Şifrenizi Gİriniz : ")
    for line in open("veriler.txt","r").readlines():
        giris_bilgisi = line.split()
        if username == giris_bilgisi[0] and password == giris_bilgisi[1]:
            
            print("""
            ****************************BANKA UYGULAMASI****************************
                                            
                                            HOŞGELDİNİZ
            HESAP NO : {}

            1- PARA YÜKLE
            2- PARA ÇEKME
            3- HESAPTAN HESABA PARA AKTARMA
            4- İŞLEM GEÇMİŞİ GÖRÜNTÜLEME

            
            
            """.format(username))
            # islem()
    print("Hesap Numarası Veya Şifre Yanlış")
    return False
    
# def islem(giris):
#     print("merhaba".format(giris.username))


print("""
************************BANKA UYGULAMASI************************
Lütfen Öncelikle Giriş Yapınız!!!!!!!

1- Hesap Girişi

2- Hesap Açma

****************************************************************


""")

islem = input("Yapmak İstediğiniz İşlemi Seçiniz : ")
if(islem == "1"):
    giris()
elif(islem == "2"):
    kayit()
else:
    print("Yanlış bir tuşlama yaptınız!!!!")

