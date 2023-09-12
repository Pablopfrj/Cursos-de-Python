# %%
import pandas as pd

# %%
idade = [31,33,2,29,60,58,31,45,24]
# %%

s_idade = pd.Series(idade)
s_idade
# %%

# Métodos das Séries

media = s_idade.mean()

variancia= s_idade.var()

des_pad = s_idade.std()

s_idade.describe().round(1)

# %%

filtro = s_idade >= 30
s_idade[~filtro]

# %%
