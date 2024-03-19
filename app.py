import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

load_dotenv()
MAILGUN_TOKEN = os.getenv("MAILGUN_TOKEN")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# Route for the contact form
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        send_simple_message(name, email, message)

    # Render the contact form template
    return render_template("index.html")


def send_simple_message(name, email, message):
    text = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    response = requests.post(
        "https://api.mailgun.net/v3/sandboxb9874d6129aa4baeb758076168db4af7.mailgun.org/messages",
        auth=("api", MAILGUN_TOKEN),
        data={
            "from": "Mailgun Sandbox <postmaster@sandboxb9874d6129aa4baeb758076168db4af7.mailgun.org>",
            "to": "Johnathan Wong <johnathanwong2001@gmail.com>",
            "subject": "Portfolio Contacted",
            "text": text,
        },
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)