from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the homepage!"

@app.route("/hello")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)