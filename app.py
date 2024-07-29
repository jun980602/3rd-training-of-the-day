from flask import Flask, render_template, request, flash
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "JUNHAo98"

@app.route("/")
def index():
    flash(random_greeting())
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    user_name = request.form.get('name_input', 'Stranger')
    current_time = datetime.now().strftime("%H:%M:%S")
    flash(f"Hi {user_name}, great to see you! I'm Jun Hao Current time is {current_time}.")
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

def random_greeting():
    greetings = [
        "What's your name?",
        "Hello there!",
        "Welcome to our website!",
        "Glad to have you here!",
        "Hope you're having a great day!"
    ]
    return random.choice(greetings)

if __name__ == "__main__":
    app.run(debug=True)
