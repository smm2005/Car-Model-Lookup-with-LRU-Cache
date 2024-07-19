from flask import Flask, render_template, jsonify, request
from finder import CarModelFinder

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/result", methods=["POST"])
def result():
    data = request.get_json()
    cmf = CarModelFinder(data['makeValue'].strip(), data['yearValue'].strip())
    cmf.find()
    string = cmf.getString()
    return string


if __name__ == '__main__':
    app.run(debug=True)