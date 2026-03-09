from flask import Flask, render_template, request
import analyzer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    strength = None
    feedback = []
    suggestion = None

    if request.method == "POST":

        password = request.form["password"]

        strength, feedback = analyzer.check_password_strength(password)
        suggestion = analyzer.generate_strong_password()

    return render_template(
        "index.html",
        strength=strength,
        feedback=feedback,
        suggestion=suggestion
    )

if __name__ == "__main__":
    app.run(debug=True)
