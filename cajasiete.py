import sys
import os
import subprocess
import pandas as pd
import time
from datetime import datetime, date as d

# get filename from commandline argument and convert to CSV using LibreOffice
# Cajasiete uses a corrupt xls format, so could not use pandas to convert it
# wait for 2 seconds until the CSV file is ready
filename = sys.argv[1]
command = "& 'C:\Program Files\LibreOffice\program\soffice.exe' --headless --convert-to csv " + filename
subprocess.call(["powershell", "-Command", command])
time.sleep(2)

# read the temporary CSV file and ignore the first row, then delete it
# create temporary dataFrame to collect statement information
csv = pd.DataFrame(pd.read_csv('caja.csv', skiprows=1))
os.remove("caja.csv")
df = pd.DataFrame(columns = ['Date', 'Contact', 'Description', 'Amount'])

# add info from each row of the Cajasiete statement to temporary dataFrame
for i, row in csv.iterrows():
    contact = ''
    description = ''
    date = ''
    amount = 0.0
    amount = float(row['Importe'].replace(',', '.'))
    date = row['Fecha Valor'].replace("'", "")
    description = row['Descripci�n']
    rowdata = [date, contact, description, amount]
    df = df.append(pd.Series(rowdata, index = df.columns), ignore_index=True)

# write CSV bank statement from dataFrame
now = datetime.now()
filename = "cajasiete_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
df.to_csv (filename, index = None, header=True)

