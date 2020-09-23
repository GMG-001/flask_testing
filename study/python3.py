from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

if __name__=='__main__':
    app.run(debug=True)