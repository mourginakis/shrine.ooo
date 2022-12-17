from flask import Flask
app = Flask(__name__)

@app.route('/')
def shrine():
    return "Shrine.ooo"
