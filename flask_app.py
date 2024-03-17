from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! This is Mustafa.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')




# set FLASK_APP=app.py
# python3 -m flask run
