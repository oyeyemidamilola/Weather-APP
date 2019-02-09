from app import app
from flask import render_template ,request, url_for, redirect, jsonify
import requests
from flask_simple_geoip import SimpleGeoIP

simple_geoip = SimpleGeoIP(app)

# API URLS

APIKEY = '8e6a9576af3486999768f6f77eab5e1f'
API_URL_CITY = 'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apikey}'
API_URL = 'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={apikey}'
GEO_LOC_API = 'https://geoipify.whoisxmlapi.com/api/v1?apiKey=at_e5iOhjDwvsfyYOvROlgnO4uMmJVm6&ipAddress={}'

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

# this route has the uses a geolocation api to query the location of the client
@app.route('/weather_forecast', methods=['GET','POST'])
def share_location():
	if request.method == "POST":
		data = request.form['permission']
		print(data)
		if data == "YES":
			try:
				# get the IP address of the user
				geo_ip = simple_geoip.get_geoip_data()
				ip_add = str(geo_ip['ip'])
				print(ip_add)
				# IP address for United States is being used to allow deployment on a local serves
				# note - change to get other country's result
				location = requests.get(GEO_LOC_API.format('197.210.53.141'))
				location_json = location.json()	
				response = requests.get(API_URL_CITY.format(cityname=location_json['location']['city'],apikey=APIKEY))
				return render_results(response.json())
			except KeyError:
				return "Sorry, Your location can't be found"
			except TypeError:
				return "No Internet Connection "
			
		else:
			return redirect(url_for('zipcode'))	
	return render_template('weather_forecast.html')

# this route has the uses a zipcode to query the client's weather status
# note - the api used only queries US weather status
@app.route('/zipcode', methods=['GET','POST'])
def zipcode():
	if request.method == "POST":
		try:
			data = request.form['zipcode']
			response = requests.get(API_URL.format(zipcode=data,apikey=APIKEY))
			return render_results(response.json())
		except KeyError:
			return "Location not found\n Specify a correct ZipCode in the US"		
		
	return render_template('zipcode.html')



def convert_to_celcius(temperature):
	return temperature - 273.15

# render weather status 
def render_results(response_json):
	weather_condition = response_json['weather'][0]['description']
	weather_temperature = convert_to_celcius(float(response_json['main']['temp']))
	location = (response_json['name'],response_json['sys']['country'])
	return render_template('display_status.html',weather_condition=weather_condition,weather_temperature=weather_temperature,location=location)

