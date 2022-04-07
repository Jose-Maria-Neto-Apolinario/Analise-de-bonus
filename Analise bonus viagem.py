from twilio.rest import Client
import pandas as pd

# Your Account SID from twilio.com/console
account_sid = "AC8b6d28cb196e5955ce17916698ccd16d"
# Your Auth Token from twilio.com/console
auth_token = "f178b8a9ceaea6c987b534947ab87d01"
client = Client(account_sid, auth_token)


# Abrir 6 arquivos em exel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        print(
            f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')


message = client.messages.create(
    to="+5534984010545",
    from_="+17579607099",
    body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
print(message.sid)


# Para cada arquivo

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55,000

# Se for maior do que 55,000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55,000 não quero fazer nada
