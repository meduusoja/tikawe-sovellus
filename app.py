from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "tänne tehdään tumblrin tyylinen palsta"

