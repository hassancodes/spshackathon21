import time
from urllib.request import urlopen
import pprint
from matplotlib import pyplot as plt
import numpy
import json
# fetching the form
def PlantCall():
    par0 = "ALLSKY_SFC_PAR_TOT"
    par1 = "GWETTOP"
    par2 = "QV2M"
    par3 = "T2M"
    community = "AG"
    long,lat = "-77.0720","38.8848"
    start,end = "20210101","20210201"

    url = "https://power.larc.nasa.gov/api/temporal/daily/point?parameters={0},{1},{2},{3}&community={4}&longitude={5}&latitude={6}&start={7}&end={8}&format=JSON".format(par0,par1,par2,par3,community,long,lat,start,end)
    # store the response of URL
    response = urlopen(url)
    # from url in data
    nasaData = json.loads(response.read())
    return nasaData

# PlantCall()

# PAR = nasaData["properties"]["parameter"]["ALLSKY_SFC_PAR_TOT"]
PAR = PlantCall()["properties"]["parameter"]["ALLSKY_SFC_PAR_TOT"]
SW =  PlantCall()["properties"]["parameter"]["GWETTOP"]
HUM = PlantCall()["properties"]["parameter"]["QV2M"]
T2M = PlantCall()["properties"]["parameter"]["T2M"]




avgLs = []
perCorn = [125.3112, 0.635, 13.9082, 23.558]
SDCorn = [27.94, 0.063349049, 2.815557138, 2.27043734]

perTomato = [139.5850649, 0.282532468, 6.108181818, 24.01474026]
SDTomato = [28.78263706,0.174867127, 1.225825828, 7.559249297]

perCarrots = [82.10695, 0.3131,4.55505,16.79365]
SDCarrots = [24.29066802, 0.1351061, 2.100275885, 5.630375192]

perPotatos = [107.2421333, 0.471866667,3.943466667,3.376]
SDPotatos = [26.23319731,0.042543883,1.383359105,5.521522998]







# 2nd function
def parAvg():
    counter=0
    totalPAR = 0
    for key,val in PAR.items():
        counter+=1
        totalPAR+=val

    averagePAR = totalPAR/counter

    avgLs.append(averagePAR)



# soil wetness
def swAvg():
    counter=0
    totalSW = 0
    for key,val in SW.items():
        counter+=1
        totalSW+=val

    averageSW = totalSW/counter

    avgLs.append(averageSW)



def humAvg():
    counter=0
    totalHUM = 0
    for key,val in HUM.items():
        counter+=1
        totalHUM+=val

    averageHUM = totalHUM/counter

    avgLs.append(averageHUM)




def tempAvg():
    counter=0
    totalt2m = 0
    for key,val in T2M.items():
        counter+=1
        totalt2m+=val

    averaget2m = totalt2m/counter

    avgLs.append(averaget2m)


parAvg()
swAvg()
humAvg()
tempAvg()

Zcorn =0
for avgls,percorn,sdcorn in zip(avgLs,perCorn,SDCorn):
    perfInput = avgls - percorn
    Z = perfInput / sdcorn
    Zcorn += abs(Z)


Ztomato =0
for avgls,pertomato,sdtomato in zip(avgLs,perTomato,SDTomato):
    perfInput = avgls - pertomato
    Z = perfInput / sdtomato
    Ztomato += abs(Z)

# zcarrot
Zcarrot = 0
for avgls,percarrot,sdcarrot in zip(avgLs,perCarrots,SDCarrots):
    perfInput = avgls - percarrot
    Z = perfInput / sdcarrot
    Zcarrot += abs(Z)


Zpotatos = 0
for avgls,perpotatos,sdpotato in zip(avgLs,perPotatos,SDPotatos):
    perfInput = avgls - perpotatos
    Z = perfInput / sdpotato
    Zpotatos += abs(Z)


vegetableNames = ["Corn", "Tomato", "Carrot", "Potatos"]
fruits = [Zcorn,Ztomato,Zcarrot, Zpotatos]
a = sorted(list(zip(fruits,vegetableNames)))
for k,v in a:
    print(v)


# print(a)
# print("carrot: ", min([Zcorn,Ztomato,Zcarrot, Zpotatos],"have the best condition to grow! ")

#print(list(map(lambda x: round(x,5),avgLs)))


# print(avgLs)






# def call():
#     parameters = "ALLSKY_SFC_SW_DWN"
#     community = "RE"
#     long,lat = "-77.0720","38.8848"
#     start,end = "2020","2020"
#
#     url = "https://power.larc.nasa.gov/api/temporal/monthly/point?parameters={0}&community={1}&longitude={2}&latitude={3}&format=JSON&start={4}&end={5}".format(parameters,community,long,lat,start,end)
#     # store the response of URL
#     response = urlopen(url)
#     # from url in data
#     nasaData = json.loads(response.read())
#
#     HoursOfSun = nasaData["properties"]["parameter"][parameters]
#     return HoursOfSun
#
# # print(call())
#
# monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul',
# 'Aug', 'Sep', 'Oct', 'Nov','Dec']
# arr = numpy.array(range(12))
# MonthlyCost = []
# powerBill = []







































# # Logic part
# def main(len,wid):
#
# # assigning one function to another
#     HoursOfSun = call()
#     counter =0
#     # data for solar panel
#     print( "What is the Length and width of your solar panel in feet")
#     Length = int(input())
#     Width = int(input())
#
#     #converting to Meter per sq for KWH/m^2/day
#     panel_area = Length*Width/3.3/3.3
#     MonthDays = 30
#     pricePerKwh = 0.12
#     for mon,Sunhours in HoursOfSun.items():
#         counter +=1
#         # Monthly watt hours
#         if counter ==13:
#             break
#         else:
#             # basic eq
#             DollarPM = (panel_area * Sunhours * MonthDays * pricePerKwh) / 3
#
#             powerCost =  DollarPM + 20
#             MonthlyCost.append(DollarPM)
#             powerBill.append(powerCost)
#
#
#     pprint.pprint(list(zip(monthNames,MonthlyCost,powerBill )))
#
#
# def makeGraph():
#     plt.plot(monthNames,MonthlyCost,powerBill)
#     plt.xlabel("Months")
#     plt.ylabel("Dollar Per Month")
#     plt.title(f'''Dollar Cost Saved Month {int(start)-1}-{end}''')
#     plt.legend("$")
#     plt.show()
#
#



# calling functions

# makeGraph()
