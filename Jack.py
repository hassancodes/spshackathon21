import time
from urllib.request import urlopen
import pprint
from matplotlib import pyplot as plt
import numpy
import json

parameters = "ALLSKY_SFC_SW_DWN"
community = "RE"
long,lat = "-77.0720","38.8848"
start,end = "2020","2020"

url = "https://power.larc.nasa.gov/api/temporal/monthly/point?parameters={0}&community={1}&longitude={2}&latitude={3}&format=JSON&start={4}&end={5}".format(parameters,community,long,lat,start,end)
# store the response of URL
response = urlopen(url)
# from url in data
nasaData = json.loads(response.read())


# print the json response
HoursOfSun = nasaData["properties"]["parameter"][parameters]
monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul',
'Aug', 'Sep', 'Oct', 'Nov','Dec']
arr = numpy.array(range(12))
MonthlyCost = []
powerBill = []



# Logic part
def main():
    counter =0
    # data for solar panel
    print( "What is the Length and width of your solar panel in feet")
    Length = int(input())
    Width = int(input())

    #converting to Meter per sq for KWH/m^2/day
    panel_area = Length*Width/3.3/3.3
    MonthDays = 30
    pricePerKwh = 0.12
    for mon,Sunhours in HoursOfSun.items():
        counter +=1
        # Monthly watt hours
        if counter ==13:
            break
        else:
            # basic eq
            DollarPM = (panel_area * Sunhours * MonthDays * pricePerKwh) / 3

            powerCost =  DollarPM + 20
            MonthlyCost.append(DollarPM)
            powerBill.append(powerCost)


    pprint.pprint(list(zip(monthNames,MonthlyCost,powerBill )))


def makeGraph():
    plt.plot(monthNames,MonthlyCost,powerBill)
    plt.xlabel("Months")
    plt.ylabel("Dollar Per Month")
    plt.title(f'''Dollar Cost Saved Month {int(start)-1}-{end}''')
    plt.legend("$")
    plt.show()





# calling functions
main()
makeGraph()
