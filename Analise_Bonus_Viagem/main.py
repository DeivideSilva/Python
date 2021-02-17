import pandas as pd
import os
from twilio.rest import Client

# Download the helper library from https://www.twilio.com/docs/python/install
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = "AC62414231660af0f68b86ff8324c7869c"
auth_token = "c093b10452a6af17df32ebef00dfc0d7"
client = Client(account_sid, auth_token)


# Importação das bibliotecas

# pandas -> É a integração do python com o Excel

# openpyxl -> É a integração do python com o Excel

# twilio -> Serve para enviar SMS

# Passo a passo de solução


# Abrir os 6 arquivos em Excel.
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

#Para cada arquivo:

# Verificar se algum valor na coluna vendas naquele arquivo é maior que 55.000.

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor.

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'Analise_Bonus_Viagem\\{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas: {vendas}')
        message = client.messages .create(
                     body=f'No mês {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas: {vendas}',
                     from_="+14087419461",
                     to="+5511950881271")
        print(message.sid)






