import pandas as pd
# df = pd.read_csv("df_duas_palavras.csv")
#
#
# df = df.sort_values(by="rank_global_peso")
# df.reset_index(inplace=True, drop=True)
#
#
# df = df.drop(['forca_global', 'rank_global', 'forca_peso', 'rank_peso', 'forca_global_peso'], axis=1)
#
# print(df.head(10))
# df.to_csv("df_palavra_2.csv", index=False)
# print(df.shape)

df = pd.read_csv("df_palavra.csv")
df_filtro = df[df['rank_global_peso'] == 1 ]
right_arrow = ""
palavra = "TERMO"
resposta = ""
size_df_filtro = df_filtro.shape[0]
if size_df_filtro > 50:
    size_df_filtro = 50
for index in range(size_df_filtro):
    resposta += (f"| {df['palavras'].iloc[index]} {right_arrow}  {df['rank_global_peso'].iloc[index]}  | \n")
print(resposta)













#
