from flask import Flask, render_template, request, redirect, url_for,jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("form.html")


@app.route("/index")
def index():
    return "Hi everyone, I am Hemraj Singh"


@app.route("/success/<float:score>")
def success(score):
    return f"The person has passed and the score is: {score:.2f}"


@app.route("/fail/<float:score>")
def fail(score):
    return f"The person has failed and the score is: {score:.2f}"


@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "GET":
        return render_template("form.html")

    history = float(request.form["history"])
    hindi = float(request.form["hindi"])
    science = float(request.form["science"])

    average_marks = (history + hindi + science) / 3

    if average_marks >= 40:
        return redirect(url_for("success", score=average_marks))
    else:
        return redirect(url_for("fail", score=average_marks))

@app.route('/api',methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_value=(dict(data)['a'])
    b_value=(dict(data)['b'])
    return jsonify(a_value+b_value)
    


if __name__ == "__main__":
    app.run(debug=True)