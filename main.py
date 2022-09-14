from functools import total_ordering
import json
import matplotlib.pyplot as plt

from dateutil import parser
import numpy as np


headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token XXX'
        }
#requestResponse = requests.get("https://api.tiingo.com/tiingo/utilities/search/500",headers=headers)
#requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/RYSOX/prices?startDate=2020-1-1&endDate=2022-1-1 ",headers=headers)
#print(requestResponse.json())

dates = []
values = []
f = open('sp500-historic-data-2020-2022.json')
data = json.load(f)

# Hypothèse 1 : Achat en début de mois
def buying_start_of_the_month():
    previous_month = 0
    buying_amount = 100
    total_invested = 0
    for i in data:
        yourdate = parser.parse(i['date'])
        month = yourdate.month
        year = yourdate.year
        
        if month > previous_month or (month == 1 and previous_month == 12):
            #print('buying etf on month ', month,"Year", year)
            total_invested+=buying_amount
            previous_month = month
            dates.append(str(month) + "_" + str(year))
            amount_buyed = buying_amount / i['low']
            values.append(amount_buyed)

    total_stock_amount = 0
    for i in values:
        total_stock_amount += i

    actual_value_of_wallet = total_stock_amount*data[-1]['low']

    print('total investi', f'{total_invested:.2f}')
    print('number of stock :', f'{total_stock_amount:.2f}')
    print('value in the end :', f'{actual_value_of_wallet:.2f}')
    print('plus value', f'{actual_value_of_wallet-total_invested:.2f}')

# Hypothèse 2 : Achat en milieu de mois
def buying_mid_of_the_month():
    previous_month = 0
    buying_amount = 100
    total_invested = 0
    for i in data:
        yourdate = parser.parse(i['date'])
        month = yourdate.month
        year = yourdate.year
        day = yourdate.day
        
        if (day == 14 or day == 15 or day == 16) and (month > previous_month or (month == 1 and previous_month == 12)):
            #print('buying etf on month ', month,"Year", year)
            total_invested+=buying_amount
            previous_month = month
            dates.append(str(month) + "_" + str(year))
            amount_buyed = buying_amount / i['low']
            values.append(amount_buyed)

    total_stock_amount = 0
    for i in values:
        total_stock_amount += i

    actual_value_of_wallet = total_stock_amount*data[-1]['low']

    print('total investi', f'{total_invested:.2f}')
    print('number of stock :', f'{total_stock_amount:.2f}')
    print('value in the end :', f'{actual_value_of_wallet:.2f}')
    print('plus value', f'{actual_value_of_wallet-total_invested:.2f}')

# Hypothèse 3 : Achat en fin de mois
def buying_end_of_the_month():
    following_month = 0
    buying_amount = 100
    total_invested = 0
    total_len = len(data)
    index = 0
    
    for i in data:
        yourdate = parser.parse(i['date'])
        month = yourdate.month
        year = yourdate.year

        if index+1 >= total_len:
            following_month = 1
        else:
            following_date = parser.parse(data[index+1]['date'])
            following_month = following_date.month
        index += 1

        if (following_month > month or (month == 12 and following_month == 1)):
            #print('buying etf on month ', month,"Year", year)
            total_invested+=buying_amount
            dates.append(str(month) + "_" + str(year))
            amount_buyed = buying_amount / i['low']
            values.append(amount_buyed)

    total_stock_amount = 0
    for i in values:
        total_stock_amount += i

    actual_value_of_wallet = total_stock_amount*data[-1]['low']

    print('total investi', f'{total_invested:.2f}')
    print('number of stock :', f'{total_stock_amount:.2f}')
    print('value in the end :', f'{actual_value_of_wallet:.2f}')
    print('plus value', f'{actual_value_of_wallet-total_invested:.2f}')


# Hypothèse 4 : Optimisation
def buying_optimization():
    following_month = 0
    buying_amount = 100
    total_invested = 0
    index = 0
    previous_month = 0
    total_len = len(data)
    
    for i in data:
        yourdate = parser.parse(i['date'])
        month = yourdate.month
        year = yourdate.year
        day = yourdate.day

        if index+1 >= total_len:
            following_month = 1
        else:
            following_date = parser.parse(data[index+1]['date'])
            following_month = following_date.month

        if index >= 1 and ( month > previous_month or (month == 1 and previous_month == 12)):
            diff = ((i['low']/data[index-1]['low'])-1)*100
            if diff < -1 or (following_month > month or (month == 12 and following_month == 1)):
                    print('Achat d\'etf le', day, month, year, 'diff', f'{diff:.2f}')
                    total_invested+=buying_amount
                    previous_month = month
                    dates.append(str(month) + "_" + str(year))
                    amount_buyed = buying_amount / i['low']
                    values.append(amount_buyed)
        index+=1

    total_stock_amount = 0
    for i in values:
        total_stock_amount += i

    actual_value_of_wallet = total_stock_amount*data[-1]['low']

    print('total investi', f'{total_invested:.2f}')
    print('number of stock :', f'{total_stock_amount:.2f}')
    print('value in the end :', f'{actual_value_of_wallet:.2f}')
    print('plus value', f'{actual_value_of_wallet-total_invested:.2f}')


buying_start_of_the_month()
buying_mid_of_the_month()
buying_end_of_the_month()
buying_optimization()

#TODO: plot results in a single graph

#plt.plot(dates,values)
#plt.title('S&P 500 2020-2022')
#plt.xlabel('dates')
#plt.ylabel('values')
#plt.show()

