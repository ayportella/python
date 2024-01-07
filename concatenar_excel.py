import os
import pandas as pd

data_arquivo_folder = 'data'

df = []

for file in os.listdir(data_arquivo_folder):
    if file.endswith('.xlsx'):
        print('Loading file {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(data_arquivo_folder, file)))
print(len(df))

df_principal = pd.concat(df, axis=0)
df_principal.to_excel('data/master_store.xlsx', index=False)
