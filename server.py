import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return ""


@app.route("/status")
def status():
    return {
        'status': True,
        'time': datetime.datetime.now().strftime('%H:%M:%S')
    }


app.run()