from flask import Flask, render_template, request
from ieee import IEEE
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/GetData", methods=["POST", "GET"])
def GetData():
    if request.method == "POST":
        search = IEEE(request.get_data().decode()).search()
        with open("static/data.json", "w") as out:
            out.write(json.dumps(search))
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)