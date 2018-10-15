from urllib.request import urlopen
from bs4 import BeautifulSoup

import csv

url = 'https://www.imdb.com/chart/top?sort=rk,asc&mode=simple&page=1'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
all_rows = soup.find_all('tr')
all_headers = soup.find_all('th')
headers = ((BeautifulSoup(str(all_headers), 'html.parser').get_text()).strip('[,')).strip(', ]')


filename = 'imdbratings.csv'
f = open(filename, 'w+')
f.write(headers + '\n')
# i = 1
# Numbers =[]
# while (i <= 250):
#     Numbers.append(i)
#     i += 1
# print(Numbers)
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
        f.write( Titles + years + ',' + ratings.strip('\n') + '\n')
        # print(i)
    # i+=1




    # for all_links in all_columns :
    #     link= all_links.find_all('a')
    #     titles=(BeautifulSoup(str(link), 'html.parser').get_text()).strip('[]')
    #     Titles = titles.replace(',', '')


            # f.write(set(str(N)+','+Titles+years+','+ratings.strip('\n')+'\n'))
        # print(years)
        # print(ratings)

    # for years in all_years:
    #     year = BeautifulSoup(str(years),'html.parser').get_text()
    #     print(year)

    # print(ratings)
    # print(titles)
    # h=years+ ','+ratings
    # h.replace('\n',' ')
    # print(h)
    # print(Titles+'\t'+ratings)
    # f.write(h+'\n')


    # f[0].write(Titles)
    # print(ratings)
# print(headers + '\n')

f.close()




    #for titles in links:
        #print(titles.find_all('href'))



#for row in all_rows:



