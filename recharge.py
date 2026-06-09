from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/recharge')
def recharge():
    return render_template('recharge.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/balance')
def balance():
    return render_template('balance.html')

if __name__ == '__main__':
    app.run()
