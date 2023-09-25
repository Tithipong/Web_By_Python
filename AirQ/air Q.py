import urllib, json, requests
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    # ระบุเเป้าหมายข้อมูล json และ API
    api = requests.get("http://air4thai.pcd.go.th/services/getNewAQI_JSON.php?region=2")

    # ดึงข้อมูล
    data = {
    'PM25': str(api.json()['stations'][9]['LastUpdate']['PM25']['value']),
    'PM10': str(api.json()['stations'][9]['LastUpdate']['PM10']['value']),
    'Co': str(api.json()['stations'][9]['LastUpdate']['CO']['value']),
    'AQI': str(api.json()['stations'][9]['LastUpdate']['AQI']['aqi']),
    'Level': str(api.json()['stations'][9]['LastUpdate']['AQI']['Level']),

    }

    # แสดงโค้ด
    print(data)
    # แสดงข้อข้อมูลผ่าน covid19.html และใช้ข้อมูลของ DATA
    return render_template('index.html', data = data) 
    #str(response.json()['Confirmed'])

if __name__ == "__main__":
    app.run(host="127.0.1.3", port=5000, debug=True)
    
    