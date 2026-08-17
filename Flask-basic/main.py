from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def form():
    if (request.method=='POST'):
        return 'You Sent Something'
    else:
        return 'You are just Looking'

app.run(debug=True)