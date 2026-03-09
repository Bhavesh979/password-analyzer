from flask import Flask, render_template, request
import analyzer
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    strength=None
    feedback=[]
    suggestion=None
    crack_time=None
    score=0

    if request.method=="POST":

        password=request.form["password"]

        strength,feedback,score=analyzer.check_password_strength(password)

        crack_time=analyzer.estimate_crack_time(score)

        suggestion=analyzer.generate_strong_password()

    return render_template(
        "index.html",
        strength=strength,
        feedback=feedback,
        suggestion=suggestion,
        crack_time=crack_time,
        score=score
    )

if __name__=="__main__":
    port=int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
