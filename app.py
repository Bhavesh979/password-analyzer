from flask import Flask, render_template, request, jsonify
import analyzer
import firebase_admin
from firebase_admin import credentials, firestore
import os
import time

app = Flask(__name__)

# Firebase initialization
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    password = request.json["password"]

    result = analyzer.check_password_strength(password)

    entry_id = "PASS_" + str(int(time.time()*1000))

    db.collection("password_analysis").add({

        "EntryID": entry_id,
        "Strength": result["strength"],
        "Score": result["score"],
        "Length": result["length"],
        "Uppercase": result["has_upper"],
        "Lowercase": result["has_lower"],
        "Numbers": result["has_number"],
        "SpecialChar": result["has_special"],
        "CreatedAt": firestore.SERVER_TIMESTAMP

    })

    result["EntryID"] = entry_id

    return jsonify(result)


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)
