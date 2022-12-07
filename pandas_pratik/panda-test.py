import pandas as pd
df = pd.read_excel('/home/batuhan/Documents/GitHub/Banka-Uygulamasi-V1/output.xlsx')
print(df)

username = (input("KUllanıcı Adınız : "))
password = (input("Şifre : "))



df1 = pd.DataFrame([[username, password],],
                   columns=['col 1', 'col 2'])

new_df = df.append(df1)

print(new_df)

username = (input("KUllanıcı adı"))
password = (input("Şifre : "))

df2 = pd.DataFrame([[username, password]],
                   columns=['col 1', 'col 2'])

new_df = df.append(df2)

print(new_df)

new_df.to_excel("output.xlsx")  


# df = pd.DataFrame(columns=['A'])
# for i in range(5):
#     df = df.append({'A': i}, ignore_index=True)
# df
#    A
# 0  0
# 1  1
# 2  2
# 3  3
# 4  4