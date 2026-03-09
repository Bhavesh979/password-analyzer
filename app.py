from flask import Flask, render_template, request
import analyzer
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    strength=None
    feedback=[]
    suggestion=None
    score=0
    password=""   # keep password value

    if request.method=="POST":

        password=request.form["password"]

        strength,feedback,score=analyzer.check_password_strength(password)

        # Only show suggestion if password is not strong
        if strength != "Strong":
            suggestion=analyzer.generate_strong_password()

    return render_template(
        "index.html",
        strength=strength,
        feedback=feedback,
        suggestion=suggestion,
        score=score,
        password=password
    )

if __name__=="__main__":

    port=int(os.environ.get("PORT",10000))

    app.run(host="0.0.0.0",port=port)
