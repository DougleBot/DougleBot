from flask import Blueprint, render_template, request, redirect, url_for, flash
import smtplib

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html", title="Home - DougleBot")

@main.route("/about")
def about():
    return render_template("about.html", title="About DougleBot")

@main.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        try:
            send_email(name, email, message)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash(f"Error sending message: {e}", "danger")
        return redirect(url_for("main.contact"))
    return render_template("contact.html", title="Contact DougleBot")

def send_email(name, email, message):
    # Simple SMTP setup (adjust with your email server settings)
    sender_email = "your-email@gmail.com"
    sender_password = "your-email-password"
    recipient_email = "douglas.weiss@gmail.com"
    subject = f"Contact Form Submission from {name}"

    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, f"Subject: {subject}\n\n{body}")
