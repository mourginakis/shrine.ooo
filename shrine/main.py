from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def shrine():
    return render_template('hello.html', name='Shrine.ooo')
