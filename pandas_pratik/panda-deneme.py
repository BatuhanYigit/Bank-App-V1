import pandas as pd

df = pd.read_excel('/home/batuhan/Documents/GitHub/Banka-Uygulamasi-V1/pandas_pratik/bilgiler1.xlsx')

new_df = pd.DataFrame(columns={"username","password"})

username = input("Kullanıcı adınızı giriniz!")
password = input("Şifre")
new_df = pd.DataFrame([[username,password]],columns=["username","password"])
print(new_df)
df = df.append(new_df)

kontrol_username = input("Kullanıcı adınızı girin : ")
kontrol_password = input("Şifre giriniz : ")

deneme = df[df["username"] == kontrol_username]
deneme2 = df[df["password"] == kontrol_password]

df.to_excel("/home/batuhan/Documents/GitHub/Banka-Uygulamasi-V1/pandas_pratik/bilgiler1.xlsx")

print(deneme["username"][0])
print(deneme2["password"][0])
if(kontrol_username == deneme["username"][0] and kontrol_password == deneme["password"][0]):
    print("Hoş geldiniz !!!")
else:
    print("KUllanıcı adı şifre hatalı")
