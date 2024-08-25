import pandas as pd

data = pd.read_csv('auditoria.csv')

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