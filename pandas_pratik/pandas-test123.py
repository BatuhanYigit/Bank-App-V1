import pandas as pd
df = pd.read_excel('/Users/batuhanyigit/Documents/GitHub/Banka-Uygulamasi-V1/output.xlsx')
username = input("KUllanıcı adınızı giriniz : ")
password = input("Şİfrenizi giriniz : ")

data1 = {
  "Username": [username],
  "Password": [password]
}
df1 = pd.DataFrame(data1)

kontrol_username = input("KUllanıcı adınızı giriniz : ")
kontrol_password = input("Şifrenizi giriniz : ")

# data2 = {
#   "Username": [username],
#   "Password": [password]
# }
# df2 = pd.DataFrame(data2)

# newdf = df1.append(df2)



df = df.append(df1)


df.to_excel("output.xlsx", index=False)
for a in df("Username"):
     print(df)

# if(kontrol_username == df["Username"][0]):
#      print("Merhaba HOşgeldiniz")
# else:
#      print("Yanlış")



