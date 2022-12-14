from bs4 import BeautifulSoup
import requests 

# #while(True):
file1 = open('athletics1.txt', 'w')
# file2 = open('menu.txt', 'w')

#get data
data = requests.get('https://www.peddie.org/athletics/traditions/blair-rivalry')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

table = soup.find('section', {'id':'fsEl_37420'}).find('tbody').find_all('tr')
#table = soup.find('section', {'id':'fsEl_37421'}).find('tbody').find_all('tr') #testing

for row in table:
    if row.find('span', {'class':'fsAthleticsStatusCancelled'}) is None:
        item = {}
        item["team"] = row.find('td', {'class':'fsTitle'}).text.replace('\n',"").replace('\t',"")
        item["location"] = row.find('td', {'class':'fsAthleticsLocations'}).text.replace('\n',"").replace('\t',"")
        item["time"] = row.find('time', {'class':'fsTime'}).get("datetime").split("T")[1]
        item["time"] = str(int(item["time"].split(":")[0])%12) +":"+ item["time"].split(":")[1] #read and set correct time from datetime attribute
        result = row.find('td', {'class':'fsAthleticsResult'}).text.replace('\n',"").replace('\t',"")
        result = ("Peddie" if (result=="Win") else "Blair" if (result=="Loss") else result)
        score = row.find('td', {'class':'fsAthleticsScore'}).text.replace('\n',"").replace('\t',"")
        item["score"] = result + " " + score

        file1.write(item["team"] +'\\'+ item["location"] +'\\'+ item["time"] + "\\" + item["score"] + "\n")
# file2.write(menu2)
file1.close()
# file2.close()

#debugging:
print(__file__)