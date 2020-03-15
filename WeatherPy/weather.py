
# Dependencies and Setup
import numpy as np
import requests
import json
import time
import pandas as pd
import pprint as pprint
import pandas.io.json as pd_json
from weatherdata import weatherData
from weatherdata import flatten_json
# Import API key
from api_keys import weather_api_key
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import scipy.stats as st
from matplotlib import pyplot as plt
from scipy.stats import linregress
import numpy as np
#from sklearn import datasets


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


#print(filtered)

lat =  filtered['lat'].tolist()
temp = filtered['maxTemp'].tolist()
hum = filtered['humidity'].tolist()
cl = filtered['Cloudiness'].tolist()
ws = filtered['windSpeed'].tolist()








def linearPlot(xList, yList, xlabel, ylabel, title):


    (slope, intercept, rvalue, pvalue, stderr) = linregress(xList, yList)
    print(f"The r-squared is: {rvalue}")
    #plt.show()
    regress_values = []

    for i in xList:

        regress_values.append ( i * slope + intercept )

    plt.plot(xList,regress_values,"r-")
   # plt.annotate('annotate', xy=(2, 1), xytext=(3, 4),
    #        arrowprops=dict(facecolor='black', shrink=0.05))
    t = 'y={:.2f}x+{:.2f}'.format(slope,intercept)
    plt.annotate(t , xy=(0,0), color="r")
    plt.scatter(xList,yList)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.show()



linearPlot(lat,temp,"latitude","temperature (f)", "City Latitude vs Max Temp (3/10/19")
linearPlot(lat,hum,"latitude","humidity %", "City Latitude vs Humidity (3/10/19")
linearPlot(lat,cl,"latitude","cloudiness %", "City Latitude vs Cloudiness(3/10/19")
linearPlot(lat,ws,"latitude","windspeed (mph", "City Latitude vs WindSpeed (3/10/19")




# convert to csv and display dataframe

filtered.to_csv(r'data.csv', index = None)
print(filtered )



