import random
import pandas as pd




def kayit():
    print("********************HESAP AÇMA EKRANI********************")
    username = random.randint(0,999999999)
    print("Hesap NO : {}".format(username))
    password = input("Şifrenizi Giriniz : ")
    fullname = input("İsim Soyisminizi Boşluk Bırakarak giriniz : ")
    df = pd.read_csv("./store/user-table.csv")
    df_bakiye = pd.read_csv("./store/bakiye.csv")

    if df.empty:
        lastid = 0

    else:
       lastid = df['ID'].iloc[-1]

    userinfo = {
        'ID' : lastid +1,
        'AccountID' : username,
        'Password' : password,
        'FullName' : fullname,
    }
    balanceinfo = {
        'ID' : lastid +1,
        'AccountID' : username,
        'Balance' : 100,

    }
    
    df = df.append(userinfo, ignore_index=True)
    df_bakiye = df_bakiye.append(balanceinfo, ignore_index=True)

    df.to_csv('./store/user-table.csv', index=False)
    df_bakiye.to_csv('./store/bakiye.csv', index=False)
    print("Hesap Numaranız {} Bu numarayı kayıt etmenizi tavsiye ederiz.".format(username))
    giris()

def giris():
    df = pd.read_csv("./store/user-table.csv")
    df_bakiye = pd.read_csv('./store/bakiye.csv')
    username = input("Hesap Numaranızı Giriniz :" )
    password = input("Şifrenizi Gİriniz : ")
    userinfo = df[df["AccountID"].isin([int(username)])]
    userinfo = userinfo.append(userinfo, ignore_index=True)
    bakiyeinfo = df_bakiye[df_bakiye["AccountID"].isin([int(username)])]
    if len(userinfo["AccountID"]) > 1 or userinfo.empty:
        print("Böyle Bir kullanıcı bulunamadı")
        print(userinfo)

    else:
        print("ELSE")
        print(userinfo)
        while True:
            if int(password) == userinfo["Password"][0]:
                print("Hoşgeldiniz {}".format(userinfo["FullName"]))
                break

            else:
                print("Şifreniz Hatalı")
            
    print("""
                     ****************************BANKA UYGULAMASI****************************
                                            
                                             HOŞGELDİNİZ
             HESAP NO : {}
             Bakiye : {}
             İsim Soyisim : {}
             1- PARA YÜKLE
             2- PARA ÇEKME
             3- HESAPTAN HESABA PARA AKTARMA
             4- İŞLEM GEÇMİŞİ GÖRÜNTÜLEME

            
            
             """.format(username,bakiyeinfo["Balance"].to_string(index=False),userinfo["FullName"][0]))

    islem1 = input("Yapılacak işlemi seçiniz : ")
    if(islem1 == "1"):
        parayukle()
    else:
        print("Yanlış İşlem")
            
            
def parayukle():
    username = input("Para yüklenecek hesap no giriniz : ")
    df = pd.read_csv("./store/user-table.csv")
    df_bakiye = pd.read_csv('./store/bakiye.csv')
    miktar = input("Hesaba Yüklenecek Miktarı Giriniz : ")
    
    bakiyeinfo = df_bakiye[df_bakiye["AccountID"].isin([int(username)])]
    
    
    islem = int(bakiyeinfo["Balance"]) + int(miktar)
    islem = str(islem)
    bakiyeinfo = bakiyeinfo.append(bakiyeinfo, ignore_index=True)
    
    print(islem)
    # data.loc[3] = ['PineApple','Yellow','48']
    bakiyeinfo.loc[0, 'Balance'] = [islem]
    bakiyeinfo = bakiyeinfo.append(bakiyeinfo, ignore_index=True)
    print(bakiyeinfo.loc[0])

    
    
    # print(islem)
    # print(bakiyeinfo)

    

    
    


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




