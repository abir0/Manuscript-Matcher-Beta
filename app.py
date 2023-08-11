from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/home")
def home():
    if request.method == "POST":
        input_title = request.form.get('title')
        input_abstract = request.form.get('abstract')
        print(input_title, input_abstract)
    return render_template("index.html", title="Home")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
