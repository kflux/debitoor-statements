# Bank Statement Converter Scripts for Debitoor

I am using the excellent bookkeeping and invoicing serive [Debitoor](https://debitoor.com). Unfortunately its third party bank connection API provider [FintechSystems](https://fintecsystems.com) does not support synchronisation of bank transfer statements for neither of my business bank accounts. I have a multi-currency account at [Wise](https://wise.com) and a local Spanish autónomo account at [Cajasiete](https://www.cajasiete.com/). Fortunately you can also upload CSV files at [Debitoor](https://debitoor.com) if direct synchronisation doesn't work.

 Wise provides CSV files but with way more columns than Debitoor can process and also separately for each of the currencies. Cajasiete only provides their statements as a semi corrupt XML file.
 
 Here are two Python scripts that 
 * convert Wise statements into a more Debitoor friendly format converting USD amounts into EUR
 * brute force convert Cajasiete xls files into a friendlier csv format using LibreOffice and some data juggling

## Wise Bank Statements

1. Login to Wise account
2. Go to EUR or USD account
3. Click `Accounting`, then `Statements`
4. On the `Export statement` overlay, select the desired date range and tick the `Accounting` radio button
5. In the dropdown menu below select `CSV (Comma Separated Values)` and hit `Download`
6. run `python wise.py` and provide the path to the downloaded file as argument
7. you should get a new bank statement csv file in your working directory

## Cajasiete Bank Statements

1. Login to your Cajasiete account
2. In the side menu under `Operaciones Frecuentes` select `Movimientos`
3. Under the blue filter and search settings box click `Ampliar Búsqueda y Exportar Resultados`
4. Select the desired date range and click `Aceptar`
5. After the page refreshes you should see an Excel document icon next to the print icon at the top right
5. Click it to download the bank statements
6. run `python cajasiete.py` and provide the path to the downloaded file as argument
7. you should get a new bank statement csv file in your working directory