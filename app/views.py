from flask import render_template

from app import app


@app.route("/")
@app.route("/home", methods=["POST", "GET"])
def home():
    app.logger.info("/ or /home loaded")

    return render_template("home.html")
