import requests
import json
import matplotlib.pyplot as plt

headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token XXX'
        }
#requestResponse = requests.get("https://api.tiingo.com/tiingo/utilities/search/500",headers=headers)
#requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/RYSOX/prices?startDate=2020-1-1&endDate=2022-1-1 ",headers=headers)
#print(requestResponse.json())

dates = []
values = []
index = 0

f = open('sp500-historic-data-2020-2022.json')
data = json.load(f)
for i in data:
    #print(i['date'])
    dates.append(i['date'])
    #print(i['low'])
    values.append(i['low'])
    if index >= 1:
        diff = ((values[index]/values[index-1])-1)*100
        if diff < -1.5:
                print(i['date'])
                print('Différence from previous day < 1.5', diff)
    index+=1 




#plt.plot(dates,values)
#plt.title('S&P 500 2020-2022')
#plt.xlabel('dates')
#plt.ylabel('values')
#plt.show()

