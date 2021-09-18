import sys
import pandas as pd
from datetime import datetime, date as d
from forex_python.converter import CurrencyRates

# get filename from commandline argument
# read the CSV file given as argument
# create temporary dataFrame to collect statement information
# instantiate currency converter
filename = sys.argv[1]
csv = pd.DataFrame(pd.read_csv(filename))
df = pd.DataFrame(columns = ['Date', 'Contact', 'Description', 'Amount'])
c = CurrencyRates()

# add info from each row of the Wise statement to temporary dataFrame
# default currency is EUR, USD gets converted to EUR using the rate of the transaction day at 4pm
for i, row in csv.iterrows():
    contact = ''
    description = ''
    date = ''
    amount = 0.0
    if row['Currency'] == 'USD':
        dto = datetime.strptime(str(row['Date']) + " 16:00:00", '%d-%m-%Y %H:%M:%S')
        if row['Exchange From'] == 'USD' and row['Exchange To'] == 'EUR' and pd.notnull(row['Exchange Rate']):
            rate = row['Exchange Rate']
        else:
            rate = c.get_rate('USD', 'EUR', dto)
        amount = round(float(row['Amount']) * rate, 2)
    if row['Currency'] == 'EUR':
        amount = float(row['Amount'])
    date = row['Date']
    if pd.notnull(row['Merchant']):
        contact = row['Merchant']
    elif pd.notnull(row['Payer Name']):
            contact = row['Payer Name']
    elif pd.notnull(row['Payee Name']):
            contact = str(row['Payee Name']) + " " + str(row['Payee Account Number'])
    description = row['Description'] + " (" + row['TransferWise ID'] + ")"
    rowdata = [date, contact, description, amount]
    df = df.append(pd.Series(rowdata, index = df.columns), ignore_index=True)

# write CSV bank statement from dataFrame
now = datetime.now()
filename = "wise_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
df.to_csv (filename, index = None, header=True)