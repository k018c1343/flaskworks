from flask import Flask
import datetime
import calendar

dt1 = datetime.date.today()
dt2 = datetime.datetime.now

app = Flask(__name__)

@app.route('/')


def hello_date():
    dt = datetime.datetime.now()
    strdt = dt.strftime('%m/%d%H:%M')
    return strdt

if __name__=='__main__':
    app.debug = True
    app.run()