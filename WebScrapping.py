from urllib.request import urlopen as urlrequest
from bs4 import BeautifulSoup
import csv
url = 'http://www.hubertiming.com/results/2017GPTR10K'
page = urlrequest(url)
soup=BeautifulSoup(page, "html.parser")
title=soup.title.text
all_links=soup.find_all('a')
for link in all_links:
    hyperlinks=link.get('href')
all_rows=soup.find_all('tr')
for row in all_rows:
    all_columns=row.find('td')
    column_string=str(all_columns)
column=BeautifulSoup(column_string, 'html.parser').get_text()
filename='sample.csv'
f=open(filename, 'w')
header='Column \n'
f.write(header)
f.write(column)
f.close()





