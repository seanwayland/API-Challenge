from citipy import citipy

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
Perform a weather check on each city using a series of successive API calls.
Include a print log of each city as it'sbeing processed (with the city number and city name).
'''
#print(cities[2])

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

print(cities[9])
print(responses[9])

with open('data.txt', 'w') as outfile:
    json.dump(responses, outfile)

'''
#print(len(d))

'''
with open('data.txt') as json_file:
    weather_data = json.load(json_file)

print(weather_data[3])
'''
