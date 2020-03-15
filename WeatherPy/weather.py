
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
for index, row in dfiltered.iterrows():
    countries.append((row['sys']['country']))
    humidity.append((row['main']['humidity']))


filtered['Countries'] = countries

'''
Convert Raw Data to DataFrame
Export the city data into a .csv.
Display the DataFrame



pData.to_csv(r'data.csv', index = None)
print(pData)
'''


