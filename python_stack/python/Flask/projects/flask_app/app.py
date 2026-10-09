from flask import Flask , render_template , redirect , request, session
app = Flask(__name__)
app.secret_key="asdghjkl;345"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user')
def index2():
    print(session["x"])
    return render_template("user.html")

@app.route('/register', methods = ['POST'])
def register():
    session["x"] = request.form['name']
    session['password'] = request.form['password']
    return redirect('/user')

if __name__ == "__main__":
    app.run(debug = True )
