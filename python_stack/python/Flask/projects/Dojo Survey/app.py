from flask import Flask , render_template , request, redirect
app = Flask (__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods = ['POST'])
def register():
    name = request.form['name']
    email = request.form ['email']
    dojolocation = request.form ['dojolocation']
    favoritelanguage = request.form ['favoritelanguage']
    return render_template("register.html", name = name, email =  email, dojolocation = dojolocation, favoritelanguage= favoritelanguage)
    # return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)