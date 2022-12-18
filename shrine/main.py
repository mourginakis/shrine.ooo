from flask import Flask, render_template

import json
import pandas as pd

from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.sampledata.iris import flowers



app = Flask(__name__)

@app.route('/')
def shrine():
    return render_template('index.html', name='Shrine.ooo', bokeh_resources=CDN.render())



colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

def make_plot(x, y):
    p = figure(title = "Iris Morphology", sizing_mode="fixed", width=400, height=400)
    p.xaxis.axis_label = x
    p.yaxis.axis_label = y
    p.circle(flowers[x], flowers[y], color=colors, fill_alpha=0.2, size=10)
    return p


@app.route('/plot')
def plot():
    p = make_plot('petal_width', 'petal_length')
    return json.dumps(json_item(p, "myplot"))

@app.route('/plot2')
def plot2():
    p = make_plot('sepal_width', 'sepal_length')
    return json.dumps(json_item(p))



