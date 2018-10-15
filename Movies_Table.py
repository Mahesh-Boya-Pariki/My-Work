import pyodbc as db
from urllib.request import urlopen
from bs4 import BeautifulSoup

server = '192.168.18.36'
database = 'HBK_Test'
username = 'maheshp'
password = 'Welcome123'
cnxn = db.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
Createtable = 'Create Table IMDB_Movies_Mahesh(Rank int identity,Title Nvarchar(250),[IMDb Rating] Nvarchar(250))'
# cursor.execute(Createtable)
# cursor.commit()

url = 'https://www.imdb.com/chart/top?sort=rk,asc&mode=simple&page=1'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
all_headers = soup.find_all('th')
all_rows = soup.find_all('tr')

for row in all_rows:
    all_columns = row.find_all('td', {'class': 'titleColumn'})

    all_span = row.find_all('span', {'class': 'secondaryInfo'})
    all_years = BeautifulSoup(str(all_span),'html.parser').get_text()
    years=all_years.strip('[]')
    all_ratings = row.find_all('td', {'class': 'ratingColumn imdbRating'})
    ratings = (BeautifulSoup(str(all_ratings), 'html.parser').get_text()).strip('[]')


    # Title = (BeautifulSoup(str(all_columns), 'html.parser').get_text()).strip('[]')
    # print(Title)
# i=1
# while(i<=250):
    for all_links in all_columns:
        link = all_links.find_all('a')
        titles=(BeautifulSoup(str(link), 'html.parser').get_text()).strip('[]')
        Titles = titles.replace(',', '')
        Title= Titles+years
        # print(Title)
        cursor.execute("INSERT INTO IMDB_Movies_Mahesh (Title,[IMDb Rating]) Values (?,?) ", (Title,ratings))
        cursor.commit()


cursor.close()
        # print(Titles+years,ratings)


