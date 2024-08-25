import pandas as pd

data = pd.read_csv('auditoria.csv')

# Check day that more than one transaction occurred
credit = data[data['Operação'] == 'Crédito']
debit = data[data['Operação'] == 'Débito']

creditPerDay = credit.groupby('Data').size()
debitPerDay = debit.groupby('Data').size()

moreThanOneCredit = creditPerDay[creditPerDay > 1]
moreThanOneDebit = debitPerDay[debitPerDay > 1]

print("Data onde são mais de 1 lançamento de Crédito:")
print(moreThanOneCredit)

print("\nData onde são mais de 1 lançamento de Débito:")
print(moreThanOneDebit)

# Check if month balance are ZERO
data['Data'] = pd.to_datetime(data['Data'], format='%d/%m/%Y')

data['Valor'] = pd.to_numeric(data['Valor'], errors='coerce')

data['Mes'] = data['Data'].dt.to_period('M')

data['Valor'] = data.apply(lambda x: x['Valor'] if x['Operação'] == 'Débito' else -x['Valor'], axis=1)
monthBalance = data.groupby('Mes')['Valor'].sum()

monthBalanceError = monthBalance[monthBalance != 0]

print("Meses com saldo não zerado:")
print(monthBalanceError)