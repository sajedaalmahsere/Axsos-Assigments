from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/champion')
def champion():
    return "Champion!"

@app.route('/say/<name>')
def hi(name):
    return f"Hi {name}"

@app.route('/repeat/<num>/<name>')
def times(num,name):
    return f"{name} " * int(num)

if __name__ == "__main__":
    app.run(debug=True)