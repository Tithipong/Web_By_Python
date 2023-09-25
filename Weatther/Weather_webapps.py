from flask import Flask, render_template, request 
import sys,time
from datetime import datetime

# import json to load JSON data to a python dictionary 
import json  
# urllib.request to make a request to api 
import urllib.request 
  
  
app = Flask(__name__) 
  
@app.route('/', methods =['POST', 'GET']) 
def weather(): 
    if request.method == 'POST': 
        city = request.form['city']
    else: 
        # for default name mathura 
        city = 'lamphun'
     # API คีย์
    api = '6f88aab69682afcc30f4c72ec4d9df9f'
    exclude = 'hourly' # ช่วงเวลา
    lat = '18.57'
    lon = '99.00'
     # รวม API URL
    source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/onecall?' + 'lat=' + lat +'&lon=' + lon + '&exclude=' 
    + exclude + '&appid=' + api).read()

     # converting JSON data to a dictionary
    list_of_data = json.loads(source)
    

    
    data = { 
        # สภาพอากาศ
        "country_code": str(list_of_data['current']['temp']), 
        "temp_min": str(int(list_of_data['daily'][0]['temp']['min']) - int(273)),
        "temp_max": str(int(list_of_data['daily'][0]['temp']['max']) - int(273)),
        "temp": str(int(list_of_data['current']['temp']) - int(273)), 
        "pressure": str(list_of_data['current']['pressure']), 
        "humidity": str(list_of_data['current']['humidity']),
        # "rain_per": str(int(list_of_data['daily'][0]['rain']) ),
        "sunrise": str(datetime.fromtimestamp(list_of_data['daily'][0]["sunrise"]).strftime('%H:%M:%S')),
        "sunset": str(datetime.fromtimestamp(list_of_data['daily'][0]["sunset"]).strftime('%H:%M:%S'))
    } 
    print(data) 
    return render_template('index.html', data = data) 
  
  
if __name__ == '__main__': 
    app.run(host="127.0.1.4", port=5000, debug=True)
