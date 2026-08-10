from flask import Flask, render_template, Response, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods = ['POST'])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    valid_user = {
        "Neil" : "123",
        "Dubban" : "456",
        "Dubbu" : "789"
    }
    if(username in valid_user and password == valid_user[username]):
        return render_template("welcome.html", name = username)
    else:
        f'''Invalid Username or Password'''

app.run(debug=True)