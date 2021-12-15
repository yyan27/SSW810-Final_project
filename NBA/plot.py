from flask import Flask
from  flask import render_template
import os

app = Flask(__name__)
@app.route('/')
def index():
    abs_dir = os.path.abspath(__file__).replace('plot.py', '')
    pic1 = '/static/threeTeam.png'
    return render_template('plot.html', pic1 = pic1)
@app.route('/2018-19')
def pic1():
    abs_dir = os.path.abspath(__file__).replace('plot.py', '')
    pic1 = '/static/2018-19.png'
    return render_template('plot.html', pic1 = pic1)
@app.route('/2019-20')
def pic2():
    abs_dir = os.path.abspath(__file__).replace('plot.py', '')
    pic1 = '/static/2019-20.png'
    return render_template('plot.html', pic1 = pic1)
@app.route('/2020-21')
def pic3():
    abs_dir = os.path.abspath(__file__).replace('plot.py', '')
    pic1 = '/static/2020-21.png'
    return render_template('plot.html', pic1 = pic1)
if __name__ == '__main__':
    app.debug = True
    app.run()