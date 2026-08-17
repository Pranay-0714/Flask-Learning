from flask import Flask, redirect, Response, request, url_for, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods = ["GET", "POST"])
def login():
    if(request.method == "POST"):
        username = request.form.get("username")
        password = request.form.get("password")

        if(username =="admin" and password == "123"):
            session["user"] = username # store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Ivalid Input Try Again!!", mimetype="Text/plain") 
        
    return '''
        <h1>LOGIN PAGE</h1>
        <form method="POST">
        username : <input type="text" name="username"><br>
        password : <input type="text" name="password"><br>
        <input type ="submit" value = "login">
        </form> '''

# After Login User will go here :-

@app.route("/welcome")
def welcome():
    if("user" in session):  # This means if user is inside session 
        return f'''
            <h1>Wellcome {session["user"]} </h1>
            <a href={url_for('logout')}>LogOut</a>
        '''
        return redirect(url_for("login"))


# LogOut 

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

app.run(debug=True)