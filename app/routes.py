from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/templates")
def index():
    return render_template("index.html", title="DougleBot")
