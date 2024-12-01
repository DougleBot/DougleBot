from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("/templates/index.html", title="DougleBot")
