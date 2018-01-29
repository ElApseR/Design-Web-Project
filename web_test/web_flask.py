from flask import Flask, render_template, request
import pandas as pd
from bokeh.charts import Bar, output_file, show
from bokeh.embed import components

app = Flask(__name__)

df = pd.read_csv('data.csv', encoding='utf-8')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/select')
def select():
    table = df.to_html()
    return render_template('select.html', table=table)

if __name__ == '__main__':
    app.run(port=5000, debug=True)