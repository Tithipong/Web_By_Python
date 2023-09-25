from flask import Flask, render_template, request
import sys, time, array,  requests
from datetime import datetime
# ดึงข้อมูล json / แปลข้อมูล json ให้ใช้ร่วมกับภาษา Pyton ได้
import json 
# urllib.request to make a request to api 
import urllib.request 
from json import dump
app = Flask(__name__) 
@app.route('/', methods =['POST', 'GET']) 
def weather(): 
    if request.method == 'POST': 
        city = request.form['city']
    else:
        city = 'lamphun'
     # API คีย์
    api = '6f88aab69682afcc30f4c72ec4d9df9f'
    exclude = 'hourly' # ช่วงเวลา
    lat = '18.57'
    lon = '99.00'
     # รวม API URL ของสภาพอากาศ
    source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/onecall?' + 'lat=' + lat +'&lon=' + lon + '&exclude=' 
    + exclude + '&appid=' + api).read()
     # API สำหรับ Covid19
    api = requests.get("https://covid19.th-stat.com/api/open/today")
     # API2 สำหรับค่าฝุ่น
    api2 = requests.get("http://air4thai.pcd.go.th/services/getNewAQI_JSON.php?region=2")
     # นำข้อมูลของ json ไปแปลให้ PY ใช้งานได้
    list_of_data = json.loads(source) 
    data = { 
        # สภาพอากาศ
        "country_code": str(list_of_data['current']['temp']), 
        "temp_min": str(int(list_of_data['daily'][0]['temp']['min']) - int(273)),
        "temp_max": str(int(list_of_data['daily'][0]['temp']['max']) - int(273)),
        "temp": str(int(list_of_data['current']['temp']) - int(273)), 
        "pressure": str(list_of_data['current']['pressure']), 
        "humidity": str(list_of_data['current']['humidity']),
        # "rain_per": str(int(list_of_data['daily'][0]['rain']) * int(2) ),
        "sunrise": str(datetime.fromtimestamp(list_of_data['daily'][0]["sunrise"]).strftime('%H:%M:%S')),
        "sunset": str(datetime.fromtimestamp(list_of_data['daily'][0]["sunset"]).strftime('%H:%M:%S')),
        # covid19
        'confirmed': str(api.json()['Confirmed']),
        'recovered': str(api.json()['Recovered']),
        'hospitalized': str(api.json()['Hospitalized']),
        'death': str(api.json()['Deaths']),
        # PM2.5
        'PM25': str(api2.json()['stations'][9]['LastUpdate']['PM25']['value']),
        'PM10': str(api2.json()['stations'][9]['LastUpdate']['PM10']['value']),
        'Co': str(api2.json()['stations'][9]['LastUpdate']['CO']['value']),
        'AQI': str(api2.json()['stations'][9]['LastUpdate']['AQI']['aqi']),
        'Level': str(api2.json()['stations'][9]['LastUpdate']['AQI']['Level'])
    } 
    print(data)
    return render_template('try.html', data = data) 
if __name__ == '__main__': 
    app.run(host="127.0.1.1", port=5000, debug=True)

        