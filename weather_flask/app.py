import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    # url='api.openweathermap.org/data/2.5/weather?q={}&appid={your api key}'
    # city='Las Vegas'
    # r=requests.get(url.format(city)).json

    return render_template('weather.html')


if __name__=='__main__':
    app.run(debug=True)