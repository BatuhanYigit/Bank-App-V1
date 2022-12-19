import pandas as pd

df = pd.read_csv("./store/user-table.csv")
df_bakiye = pd.read_csv("./store/bakiye.csv")

hesap = input("Hesap NO Giriniz : ")


# test = df_bakiye[df_bakiye["AccountID"].isin([int(hesap)])]


a = 3

# df_bakiye.loc[a, 'Balance'] = '200'

aa = df_bakiye.index[df_bakiye["AccountID"].isin([int(hesap)])].tolist()

df_bakiye.loc[aa, 'Balance'] = '200'
print(aa)


print(df_bakiye)