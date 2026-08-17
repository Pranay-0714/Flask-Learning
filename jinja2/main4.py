from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def sample():
    return render_template("sample.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/base")
def base_page():
    return render_template("base.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True)