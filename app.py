from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST'])
def login():
    username=request.form.get('uname')
    password=request.form.get('psw')
    return "The Username is {} and the password is {}".format(username, password)

if __name__ == '__main__':
    app.run(debug=True)