import requests
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/home")
def home():
    if request.method == "POST":
        input_title = request.form.get('title')
        input_abstract = request.form.get('abstract')
        output = predict_category(input_title, input_abstract)
        print(output)
        return render_template("index.html", title="Home", output_text=output['data'][0]['label'])
    else:
        return render_template("index.html", title="Home")


def predict_category(title, abstract):
    url = "https://abir0-manuscript-matcher.hf.space/run/predict"
    text = title + ". \n" + abstract
    data = {
        "data": [
            text
        ],
    }
    response = requests.post(url, json=data)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
