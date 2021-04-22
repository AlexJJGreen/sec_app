from flask import render_template, url_for
from flask import current_app as app


@app.route("/")
@app.route("/index", methods=["GET"])
def home():
    return render_template("index.html")