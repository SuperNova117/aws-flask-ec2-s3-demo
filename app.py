from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from AWS EC2 + Flask!</h1><p>This is a demo project for Fiverr clients.</p>"
