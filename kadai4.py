from flask import Flask, render_template

app = Flask(__name__)

data = []

@app.route("/user/<username>/")
def addUser(username):
    data.append(username)
    return render_template("kadai4.html", username=username)

@app.route("/list/")
def showList():
    return render_template("list.html", list=data)

if __name__=="__main__":
    app.debug = True
    app.run()