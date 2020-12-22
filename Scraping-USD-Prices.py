from requests import get
from bs4 import BeautifulSoup
import re
import datetime
import csv
Today = datetime.date.today().strftime("%d/%m/%Y")

URL = 'https://www.donitna.com/?p=1223'
Response = get(URL)
Soup = BeautifulSoup(Response.text,'html.parser')
RawerText = Soup.find("div", {'class': 'entry-content clearfix'}).get_text()
Data = RawerText.split()

Data.remove('=')
Data.remove('(adsbygoogle')
Data.remove('window.adsbygoogle')
Data.remove('||')
Data.remove('[]).push({});')

DateIndex = Data.index(Today)
BuyingIndex = Data.index('شراء')
CommSellIndex = Data.index('تجاري')
#MorningPrice = Data.index('ظهر')
NoonPrice = Data.index('بداية')

SellIndex = CommSellIndex + 4
PriceDate = Data[DateIndex]
BuyPrice = Data[BuyingIndex + 2]
CommSellPrice = Data[CommSellIndex + 2]
SellPrice = Data[SellIndex + 2]



CSVFile = open('DailyPrices.csv')
Reader = csv.reader(CSVFile)
Lines = len(list(Reader))
Index = Lines - 1


print('Price For ' + PriceDate)
print('Buying Price : ' + BuyPrice)
print('Commercial Selling Price : ' + CommSellPrice)
print('Selling Price : ' + SellPrice)

#To Avoid Duplicates
Duplicate = False
with open('DailyPrices.csv', 'r') as File:
    Data = File.readlines()
LastRow = Data[-1]
print(LastRow)
LastPrices = LastRow.split(', ')
print(LastPrices)



if(Duplicate == False):
    with open('DailyPrices.csv','a',newline = '') as file:
        Writer = csv.writer(file)
        Writer.writerow([PriceDate,BuyPrice, SellPrice, CommSellPrice])

    
    
