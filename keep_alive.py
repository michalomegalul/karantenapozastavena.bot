from flask import Flask
from threading import Thread
import datetime
datetime.datetime.now()
datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
app = Flask('')

@app.route('/')
def home():
  return "ey"
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()