from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

taro_ki_link = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(taro_ki_link)

soup = bs(page.text,'html.parser')

taro_ki_table = soup.find('table')

temp_list= []
table_rows = taro_ki_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Taro_ke_nam = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Taro_ke_nam.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
df2 = pd.DataFrame(list(zip(Taro_ke_nam,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')