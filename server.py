"""
CPSC 254L Open Sources
Jeffrey Nong
Group: Earth, Wind, Fire
This file is made to connect the frontend and backend of the project to put everything together.
"""
import json
from flask import Flask, render_template, request
from ieee import IEEE

app = Flask(__name__)

@app.route('/')
def index():
    """Function renders website homepage"""
    return render_template('index.html')

@app.route("/GetData", methods=["POST", "GET"])
def get_data():
    """Function gets search dictionary from ieee module and saves as json"""
    if request.method == "POST":
        search = IEEE(request.get_data().decode()).search()
        with open("static/data.json", "w", encoding="utf-8") as out:
            out.write(json.dumps(search))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
