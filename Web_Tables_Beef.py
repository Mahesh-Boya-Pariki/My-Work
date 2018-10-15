from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyodbc

server='192.168.18.36'
db='HBK_Test'
User='maheshp'
pwd='Welcome123'
con = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db+';UID='+User+';PWD='+ pwd)
cursor = con.cursor()

CreateTable = 'CREATE TABLE BEEF_Mahesh (WeekEnding Date,WeeklyExports int,AccumulatedExports int,NetSales int,OutstandingSales int,NetSales2 int,OutstandingSales2 int)'
cursor.execute(CreateTable)


url='https://apps.fas.usda.gov/export-sales/h1701.htm'
page=urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
all_rows = soup.find_all('tr')
rows = all_rows[4:]
# print(rows)

def remove_comma(a):
    b=a.replace(',','')
    return b
# print(remove_comma('1,(2)'))
a=[]
for row in rows:
    all_columns = row.find_all('td')
    column= BeautifulSoup(str(all_columns),'html.parser').get_text().strip('[]')
    columns = remove_comma(column)
    a.append(columns.split(' '))

a.pop()

for i in a:
    j=i
    cursor.execute('INSERT INTO BEEF_Mahesh VALUES (?,?,?,?,?,?,?)',(j[0],int(j[1].strip('()')),int(j[2].strip('()')),int(j[3].strip('()')),int(j[4].strip('()')),int(j[5].strip('()')),int(j[6].strip('()'))))

con.commit()
cursor.close()
