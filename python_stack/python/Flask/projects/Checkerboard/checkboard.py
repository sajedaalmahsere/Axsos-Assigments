from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def check():
    return render_template("index.html", rows=8, columns=8)


@app.route('/<x>')
def check2(x):
    return render_template("index.html", rows=int(x), columns=8)


@app.route('/<x>/<y>')
def check3(x, y):
    return render_template("index.html", rows=int(x), columns=int(y))


@app.route('/<x>/<y>/<color>/<color2>')
def check4(x, y, color, color2):
    return render_template(
        "index.html",
        rows=int(x),
        columns=int(y),
        color=color,
        color2=color2
    )


if __name__ == "__main__":
    app.run(debug=True)