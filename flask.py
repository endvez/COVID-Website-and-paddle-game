from flask import Flask
from flask import render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')

def website_access():

  

  return render_template("covidwebsite.html")
@app.route('/result') #scrapper

def get_result():

  source = requests.get("https://www.worldometers.info/coronavirus/").text

  return source
@app.route('/game')

def paddle():

  return render_template("paddlegame.html")
@app.route('/image')

def get_image():

  source = requests.get("https://specials-images.forbesimg.com/imageserve/5e6b201b7d6f2600068f59ea/960x0.jpg?fit=scale/").text

  return source
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089)
