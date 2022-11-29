import pandas as pd

tabela1 = pd.read_excel('prof-data-2.xlsx', engine='openpyxl')

resposta = input("Nome da Área Principal: ")
filtroNome = tabela1.loc[tabela1["AREA1"] == f"{resposta}"]
tabelaDF = pd.DataFrame(tabela1)
filtro = tabelaDF.filter(["NOME"])
print(filtroNome)


