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
    
def giris():
    df = pd.read_csv("./store/user-table.csv")
    df_bakiye = pd.read_csv('./store/bakiye.csv')
    # username = input("Hesap Numaranızı Giriniz :" )
    # password = input("Şifrenizi Gİriniz : ")
    userinfo = df[df["AccountID"].isin([int(username)])]
    userinfo = userinfo.append(userinfo, ignore_index=True)
    bakiyeinfo = df_bakiye[df_bakiye["AccountID"].isin([int(username)])]
    

    control = df[df["AccountID"].isin([int(username)])]

    accountid = control["AccountID"]
    accountpass = control["Password"]

    
    if(accountid.empty and accountpass.empty):
        print("Kullanıcı adı şifre yanlış")
    
    while True:
        if(username == str(accountid.values[0]) and password == str(accountpass.values[0])):      
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
                            5- ÇIKIŞ

                
                
                """.format(username,bakiyeinfo["Balance"].to_string(index=False),userinfo["FullName"][0]))
            islem1 = input("Yapılacak işlemi seçiniz : ")
            if(islem1 == "1"):
                parayukle()
            elif(islem1 == "2"):
                paracekme()
            elif(islem1 == "3"):
                paragonderme()
            elif(islem1=="4"):
                islemgecmisi()
            elif(islem1=="5"):
                break
            else:
                print("Yanlış İşlem")
            
        else:
            print("Kullanıcı adı Şİfre yanlışşş")
                                
def parayukle():


    operation = "Para Yükleme"
    df = pd.read_csv("./store/user-table.csv")
    df_bakiye = pd.read_csv('./store/bakiye.csv')
    df_islem_gecmisi = pd.read_csv('./store/islem-gecmisi.csv')
    miktar = input("Hesaba Yüklenecek Miktarı Giriniz : ")
    
    index_control  = df_bakiye.index[df_bakiye["AccountID"].isin([int(username)])].tolist()

    bakiyeinfo = df_bakiye[df_bakiye["AccountID"].isin([int(username)])]
    
    
    if int(miktar) > 0:

        islem = int(bakiyeinfo["Balance"]) + int(miktar)
        islem = str(islem)
        balance = int(bakiyeinfo["Balance"]) + 0
        balance = str(balance)
        bakiyeinfo = bakiyeinfo.append(bakiyeinfo, ignore_index=True)
        
        print("Güncel Bakiyeniz = {}".format(islem))

        
        

        transactioninfo = {

            'AccountID' : username,
            'Balance' : balance,
            'Quantity' : miktar,
            'Operation' : operation,
            'CurrentBalance' : islem,
            'ForeignCurrency' : "TL",

        }
        df_bakiye.loc[index_control, 'Balance'] = islem
        df_bakiye.to_csv('./store/bakiye.csv', index=False)
        df_islem_gecmisi = df_islem_gecmisi.append(transactioninfo, ignore_index=True)
        
        df_islem_gecmisi.to_csv('./store/islem-gecmisi.csv', index=False)
    else:
        print("Lütfen 0 tl den büyük bir rakam giriniz ")
    giris()

def paracekme():
    operation = "Para Çekme"
    df = pd.read_csv("./store/user-table.csv")
    df_bakiye = pd.read_csv('./store/bakiye.csv')
    miktar = input("Çekmek İstediğiniz Miktarı Giriniz : ")
    df_islem_gecmisi = pd.read_csv('./store/islem-gecmisi.csv')
    
    index_control  = df_bakiye.index[df_bakiye["AccountID"].isin([int(username)])].tolist()

    bakiyeinfo = df_bakiye[df_bakiye["AccountID"].isin([int(username)])]
    bakiye = int(bakiyeinfo["Balance"])
    balance = int(bakiyeinfo["Balance"]) + 0
    balance = str(balance)
    if(int(bakiye) < int(miktar)):
        print("Bakiyeniz Yetersiz")
    
    else:
    
        if miktar > 0:
            islem = int(bakiyeinfo["Balance"]) - int(miktar)
            islem = str(islem)
            bakiyeinfo = bakiyeinfo.append(bakiyeinfo, ignore_index=True)
            
            print("Güncel Bakiyeniz = {}".format(islem))
            transactioninfo = {

                    'AccountID' : username,
                    'Balance' : balance,
                    'Quantity' : miktar,
                    'Operation' : operation,
                    'CurrentBalance' : islem,

                    }
            
            df_islem_gecmisi = df_islem_gecmisi.append(transactioninfo, ignore_index=True)
            df_bakiye.loc[index_control, 'Balance'] = islem
            df_islem_gecmisi.to_csv('./store/islem-gecmisi.csv', index=False)
            df_bakiye.to_csv('./store/bakiye.csv', index=False)
        else:
            print("Lütfen 0 tl den büyük bir rakam giriniz ")
        giris()
       
def paragonderme():
    alici = input("Para gönderilecek Hesap Numarasını Giriniz : ")
    miktar = input("Gönderilecek Miktarı Gİriniz : ")
    df = pd.read_csv("./store/user-table.csv")
    df_bakiye = pd.read_csv('./store/bakiye.csv')
    df_islem_gecmisi = pd.read_csv('./store/islem-gecmisi.csv')
    
    index_control  = df_bakiye.index[df_bakiye["AccountID"].isin([int(username)])].tolist()
    index_control2 = df_bakiye.index[df_bakiye["AccountID"].isin([int(alici)])].tolist()
    bakiyeinfo = df_bakiye[df_bakiye["AccountID"].isin([int(username)])]
    bakiyeinfo2 = df_bakiye[df_bakiye["AccountID"].isin([int(alici)])]
    dfinfo = df[df["AccountID"].isin([int(alici)])]
    dfinfoalici = df[df["AccountID"].isin([int(username)])]
    sender_name = dfinfoalici["FullName"]
    recipience_name = dfinfo["FullName"]
    bakiye2 = int(bakiyeinfo["Balance"])
    bakiye = int(bakiyeinfo["Balance"])
    balance = int(bakiyeinfo["Balance"]) + 0
    balance = str(balance)
    balance2 = int(bakiyeinfo2["Balance"]) + 0
    balance2 = str(balance2)
    

    if(int(bakiye) < int(miktar)):
        print("Bakiyeniz Yetersiz")
    else:
        if int(miktar) > 0:

            operation = "Para Gönderme"
            operation2 = "Gelen Para"
            islem = int(bakiyeinfo["Balance"]) - int(miktar)
            islem = str(islem)
            islem2 = int(bakiyeinfo2["Balance"]) + int(miktar)
            islem2 = str(islem2)
            bakiyeinfo = bakiyeinfo.append(bakiyeinfo, ignore_index=True)
            bakiyeinfo2 = bakiyeinfo2.append(bakiyeinfo2, ignore_index=True)
            print("Güncel Bakiyeniz = {}".format(islem))
            transactioninfo = {

                    'AccountID' : username,
                    'Balance' : balance,
                    'Quantity' : miktar,
                    'Operation' : operation,
                    'CurrentBalance' : islem,
                    'Recipience' : recipience_name.values[0],
                    'ForeignCurrency' : "TL",

                    }
            transactioninfo2 = {

                    'AccountID' : alici,
                    'Balance' : balance2,
                    'Quantity' : miktar,
                    'Operation' : operation2,
                    'CurrentBalance' : islem2,
                    'Recipience' : sender_name.values[0],
                    'ForeignCurrency' : "TL",

                    }     
            df_bakiye.loc[index_control, 'Balance'] = islem
            df_bakiye.loc[index_control2, 'Balance'] = islem2
            df_islem_gecmisi = df_islem_gecmisi.append(transactioninfo, ignore_index=True)
            df_islem_gecmisi = df_islem_gecmisi.append(transactioninfo2, ignore_index=True)
            df_islem_gecmisi.to_csv('./store/islem-gecmisi.csv', index=False)
            df_bakiye.to_csv('./store/bakiye.csv', index=False)

        else:

                print("0 Tl den büyük göndermeniz gerekmektedir.")

    giris()
def islemgecmisi():
    df_islemgecmisi = pd.read_csv("./store/islem-gecmisi.csv")
    info = df_islemgecmisi[df_islemgecmisi["AccountID"].isin([int(username)])]
    print(info)
    giris()

    

print("""
************************BANKA UYGULAMASI************************
Lütfen Öncelikle Giriş Yapınız!!!!!!!

1- Hesap Girişi

2- Hesap Açma

****************************************************************


""")

islem = input("Yapmak İstediğiniz İşlemi Seçiniz : ")
if(islem == "1"):
    username = input("Hesap Numaranızı Giriniz : ")
    password = input("Şifrenizi Giriniz : ")
    giris()
elif(islem == "2"):
    kayit()
else:
    print("Yanlış bir tuşlama yaptınız!!!!")




