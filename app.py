from flask import Flask,render_template
app=Flask("app")

@app.route("/")
def hello():
    return"wellcom"

@app.route("/about")
def about():
    return"me live in shahrekord , me need job"

@app.route("/contact")
def contact():
    return render_template("index.html")
app.run()