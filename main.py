
# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as
# parameter for urlopen
parameters = "PS"
community = "RE"
long = "-77.0720"
lat = "38.8848"
start = "2019"
end = "2020"
print= ("What is your Solar panel Wattage?")


url = "https://power.larc.nasa.gov/api/temporal/monthly/point?parameters={0}&community={1}&longitude={2}&latitude={3}&format=JSON&start={4}&end={5}".format(parameters,community,long,lat,start,end)

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
nasa = json.loads(response.read())

# print the json response

print(url)
Location = (nasa["geometry"]["coordinates"])
 Months = (nasa["properties"]["parameter"]["PS"])
sum = 0
 noofmon = 0
for months,surfacepress in Months.items():
     noofmon+=1
    sum += surfacepress

 average = sum/noofmon


 print("Average of SP in ", start, "is: ", int(average))


#get("https://www.power.larc.nasa.gov/api/temporal/monthly/point?parameters={0}&community={1}&longitude={2}&latitude={3}&format=JSON&start={4}&end={5}"
#.format(parameters,community,long,lat,start,end)
