# %%
import pandas as pd

df = pd.read_csv("../data/pedido.csv")

df [['idPedido', 'flKetchup']]
# %%
df.head()
# %%
colunas = [	'idPedido',	'descUF',	'flKetchup'	,'txtRecado',	'dtPedido']


df[colunas]
# %%
