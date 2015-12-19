from flask import Flask, jsonify,render_template, request, make_response
import requests
from datetime import datetime,date,timedelta,time
import urllib2
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    print '6N1C_2k2WfAx9A6aS18a'
    import requests.packages.urllib3

    return render_template('index.html')

@app.route('/result', methods=['POST'])
def home():
    try:
        symbol = request.form['symbol']
        checklist = request.form.getlist('check')
        data = json.load(urllib2.urlopen('https://www.quandl.com/api/v3/datasets/WIKI/'+symbol+'.json?api_key=6N1C_2k2WfAx9A6aS18a'))[u'dataset']
        values =data['data']
        column_name = data['column_names']
        date = []
        Open = "1"
        High = "2"
        Low = "3"
        Close = "4"
        open_price = []
        close_price = []
        high_price = []
        low_price = []
        for i in values[0:15]:
            one = datetime.strptime(i[0],'%Y-%m-%d').strftime('%b %d')
            date.append(str(one))
        min_val = []
        max_val = []
        if Open in checklist:
            for i in values[0:15]:
                open_price.append(i[1])
            min_val.append(min(open_price))
            max_val.append(max(open_price))
        if High in checklist:
            for i in values[0:15]:
                high_price.append(i[2])
            min_val.append(min(high_price))
            max_val.append(max(high_price))
        if Low in checklist:
            for i in values[0:15]:
                low_price.append(i[3])
            min_val.append(min(low_price))
            max_val.append(max(low_price))
        if Close in checklist:
            for i in values[0:15]:
                close_price.append(i[4])
            min_val.append(min(close_price))
            max_val.append(max(close_price))
        Minimum = min(min_val)
        Maximum= max(max_val)
        val1  = Maximum - Minimum
        if val1 < 10:
            Steps = 1
        else:
            Steps = 10
        return render_template('result.html',Maximum=int(Maximum),Steps=Steps,Date=date,row1=open_price,row2=close_price,row3=high_price,row4=low_price,Minimum=int(Minimum),symbol=symbol)
    except Exception as e:
        return render_template('Error.html')


if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify,render_template, request, make_response
import requests
from datetime import datetime,date,timedelta,time
import urllib2
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def home():
    try:
        symbol = request.form['symbol']
        checklist = request.form.getlist('check')
        data = json.load(urllib2.urlopen('https://www.quandl.com/api/v3/datasets/WIKI/'+symbol+'.json?api_key=YOURAPIKEYHERE'))[u'dataset']
        values =data['data']
        column_name = data['column_names']
        date = []
        Open = "1"
        High = "2"
        Low = "3"
        Close = "4"
        open_price = []
        close_price = []
        high_price = []
        low_price = []
        for i in values[0:15]:
            one = datetime.strptime(i[0],'%Y-%m-%d').strftime('%b %d')
            date.append(str(one))
        min_val = []
        max_val = []
        if Open in checklist:
            for i in values[0:15]:
                open_price.append(i[1])
            min_val.append(min(open_price))
            max_val.append(max(open_price))
        if High in checklist:
            for i in values[0:15]:
                high_price.append(i[2])
            min_val.append(min(high_price))
            max_val.append(max(high_price))
        if Low in checklist:
            for i in values[0:15]:
                low_price.append(i[3])
            min_val.append(min(low_price))
            max_val.append(max(low_price))
        if Close in checklist:
            for i in values[0:15]:
                close_price.append(i[4])
            min_val.append(min(close_price))
            max_val.append(max(close_price))
        Minimum = min(min_val)
        Maximum= max(max_val)
        val1  = Maximum - Minimum
        if val1 < 10:
            Steps = 1
        else:
            Steps = 10
        return render_template('result.html',Maximum=int(Maximum),Steps=Steps,Date=date,row1=open_price,row2=close_price,row3=high_price,row4=low_price,Minimum=int(Minimum),symbol=symbol)
    except Exception as e:
        return render_template('Error.html')


if __name__ == '__main__':
    app.run()
