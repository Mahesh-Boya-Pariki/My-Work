from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyodbc

server='192.168.18.36'
db='HBK_Test'
User='maheshp'
pwd='Welcome123'
con = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db+';UID='+User+';PWD='+ pwd)
cursor = con.cursor()



url='https://apps.fas.usda.gov/export-sales/h1702.htm'
page = urlopen(url)
soup = BeautifulSoup(page,'html.parser')
Heading = (soup.find('p')).text

Title=(Heading+'_Mahesh').replace(' ','')



CreateTable = 'CREATE TABLE '+Title+'(WeekEnding Date,WeeklyExports int,AccumulatedExports int,NetSales int,OutstandingSales int,NetSales2 int,OutstandingSales2 int)'
cursor.execute(CreateTable)

# print(str(soup)+'\n')
all_rows = soup.find_all('tr')
rows=all_rows[4:]
def remove_comma(a):
    return a.replace(',','')

a=[]

for row in rows:
    all_columns = row.find_all('td')

    columns=((BeautifulSoup(str(all_columns),'html.parser').get_text()).strip('[]'))
    column=remove_comma(columns).split(' ')
    a.append(column)

# print(a)
a.pop()

for i in a:
    j=i
    # print(j[5])
    cursor.execute('INSERT INTO ' + Title + ' Values (?,?,?,?,?,?,?)', (j[0],float(j[1]),float(j[2]),float(j[3]),float(j[4]),float(j[5].strip('()')),float(j[6])))

con.commit()
cursor.close()
