from flask import Flask, render_template, request
from analyzer import check_password_strength, generate_strong_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    strength = None
    feedback = []
    suggestion = None

    if request.method == "POST":
        password = request.form["password"]

        strength, feedback = check_password_strength(password)

        if feedback:
            suggestion = generate_strong_password()

    return render_template(
        "index.html",
        strength=strength,
        feedback=feedback,
        suggestion=suggestion
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
