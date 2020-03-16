
# Dependencies and Setup

import pandas as pd
from weatherdata import weatherData
from matplotlib import pyplot as plt
from scipy.stats import linregress
from citipy import citipy

from citipy import citipy

'''
# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name

    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
print(len(cities))

'''
'''
Perform a weather check on each city using a series of successive API calls.
Include a print log of each city as it'sbeing processed (with the city number and city name).
'''


'''
responses = pd.DataFrame

print("running weather check on each city ")
for i in range(len(cities)):

    print("processing city number")
    print(i)
    print(cities[i])
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = cities[i]
    units = "metric"
    query_url = f"{url}appid={weather_api_key}&q={city}&units={units}"

# Get weather data
    weather_response = requests.get(query_url)
    weather_json = weather_response.json()
    responses.append(weather_json)

    time.sleep(1)

'''


d = weatherData

#get rid of empty cities
dfiltered = [x for x in d if not len(x)<10]
cloudiness = []
for i in range(len(dfiltered)):
    cloudiness.append((dfiltered[i]["clouds"]['all']))

#print(cloudiness)
dfiltered = pd.DataFrame(dfiltered)
filtered = pd.DataFrame()

filtered['City'] = dfiltered['name']
filtered['Date'] = dfiltered['dt']
filtered['Cloudiness'] = cloudiness
sys = pd.DataFrame(dfiltered['sys'])

countries = []
humidity = []
lat = []
lon = []
maxTemp = []
windSpeed = []
for index, row in dfiltered.iterrows():
    countries.append((row['sys']['country']))
    humidity.append((row['main']['humidity']))
    maxTemp.append((row['main']['temp_max']))
    windSpeed.append((row['wind']['speed']))
    lat.append((row['coord']['lat']))
    lon.append((row['coord']['lon']))



filtered['Countries'] = countries
filtered['humidity'] = humidity
filtered['lat'] = lat
filtered['lon'] = lon
filtered['maxTemp'] = maxTemp
filtered['windSpeed'] = windSpeed

north = filtered[filtered['lat'] >=0 ]
#print(north)
south = filtered[filtered['lat'] < 0]
#print(south)


lat =  filtered['lat'].tolist()
temp = filtered['maxTemp'].tolist()
hum = filtered['humidity'].tolist()
cl = filtered['Cloudiness'].tolist()
ws = filtered['windSpeed'].tolist()

nlat =  north['lat'].tolist()
ntemp = north['maxTemp'].tolist()
nhum = north['humidity'].tolist()
ncl = north['Cloudiness'].tolist()
nws = north['windSpeed'].tolist()

slat =  south['lat'].tolist()
stemp = south['maxTemp'].tolist()
shum = south['humidity'].tolist()
scl = south['Cloudiness'].tolist()
sws = south['windSpeed'].tolist()




# function that prints a lineplot or scatter plot

#arguments (x axis array [], y axis array[], x axis label string , y label string, title string , 1 to add regression  line )

def linearPlot(xList, yList, xlabel, ylabel, title, lineBool):
    t =""
    #if we want a regression line add it 
    if lineBool ==1:
        (slope, intercept, rvalue, pvalue, stderr) = linregress(xList, yList)
        print(f"The r-squared is: {rvalue}" " for " + xlabel + " / " + ylabel + "")
        #plt.show()
        regress_values = []

        for i in xList:

            regress_values.append ( i * slope + intercept )

        plt.plot(xList,regress_values,"r-")
       # plt.annotate('annotate', xy=(2, 1), xytext=(3, 4),
        #        arrowprops=dict(facecolor='black', shrink=0.05))
        t = 'y={:.2f}x+{:.2f}'.format(slope,intercept)
        #plt.annotate(t , xy=(0,0), xytext =(0,0), color="r")

    plt.scatter(xList,yList)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if lineBool == 1:
        plt.title(title + '\n regression line: ' + t)
    else:
        plt.title(title)

    plt.show()



linearPlot(lat,temp,"latitude","temperature (f)", "City Latitude vs Max Temp (3/10/19)",0)
linearPlot(lat,hum,"latitude","humidity %", "City Latitude vs Humidity (3/10/19)",0)
linearPlot(lat,cl,"latitude","cloudiness %", "City Latitude vs Cloudiness(3/10/19)",0)
linearPlot(lat,ws,"latitude","windspeed (mph", "City Latitude vs WindSpeed (3/10/19)",0)


# convert to csv and display dataframe

filtered.to_csv(r'data.csv', index = None)
#print(filtered )



'''
Your next objective is to run linear regression on each relationship, only this time separating them into Northern Hemisphere (greater than or equal to 0 degrees latitude) and Southern Hemisphere (less than 0 degrees latitude):

'''

#Northern Hemisphere - Temperature (F) vs. Latitude
#Southern Hemisphere - Temperature (F) vs. Latitude
linearPlot(nlat,ntemp,"latitude","temperature (f)", "North HemCity Latitude vs Max Temp (3/10/19)",1)
linearPlot(slat,stemp,"latitude","temperature (f)", "South Hem City Latitude vs Max Temp (3/10/19)",1)

#Northern Hemisphere - Humidity (%) vs. Latitude
#Southern Hemisphere - Humidity (%) vs. Latitude
linearPlot(nlat,nhum,"latitude","humidity %", "North Hem City Latitude vs Humidity (3/10/19)",1)
linearPlot(slat,shum,"latitude","humidity %", "South Hem City Latitude vs Humidity (3/10/1)9",1)

#Northern Hemisphere - Cloudiness (%) vs. Latitude
#Southern Hemisphere - Cloudiness (%) vs. Latitude
linearPlot(nlat,ncl,"latitude","cloudiness %", "North Hem City Latitude vs Cloudiness(3/10/19)",1)
linearPlot(slat,scl,"latitude","cloudiness %", "South Hem City Latitude vs Cloudiness(3/10/19)",1)

#Northern Hemisphere - Wind Speed (mph) vs. Latitude
#Southern Hemisphere - Wind Speed (mph) vs. Latitude
linearPlot(nlat,nws,"latitude","windspeed (mph", "North Hem City Latitude vs WindSpeed (3/10/19)",1)
linearPlot(slat,sws,"latitude","windspeed (mph", "South Hem City Latitude vs WindSpeed (3/10/19)",1)




