import urllib, json, requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # get json api data from web naja
    api = requests.get("https://covid19.th-stat.com/api/open/today")

    # Get DATA List from api variable
    data = {
    'confirmed': str(api.json()['Confirmed']),
    'recovered': str(api.json()['Recovered']),
    'hospitalized': str(api.json()['Hospitalized']),
    'death': str(api.json()['Deaths'])
    }

    # print list of data in to console
    print(data)
    # return data to covid19.html page and define data with data variable
    return render_template('covid.html', data = data) 
    #str(response.json()['Confirmed'])

if __name__ == "__main__":
    app.run(host="127.0.1.2", port=5000, debug=True)

    