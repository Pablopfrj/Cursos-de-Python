# %%
import pandas as pd

data = {
    "nome": ["Téo", "Nah", "Maria", "José", "Jessica", "Robson", "InfoSlack"],
    "idade": [30, 33, 2, 45, 65, 43, 40],  
    "cor": ["Preto", "Verde", "Azul", "Vermelho", "Verde", "Roxo", "Branco"],
    'renda': [3566,1345,0,6576,4325,5326,10244]
}

df = pd.DataFrame(data)
df
# %%
df["idade"]
# %%
df[['idade','renda']].mean()

# %%
df.describe().round(2)

# %%
