from flask import Flask, render_template, request, redirect
import requests 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'shaurya' and password == 'k':
        result =requests.get("https://as-apia.coolkit.cc/v2/smartscene2/webhooks/execute?id=8aa93b36c62b4e1bb27080847e873bdf")
        print(result)
        return redirect('/home')
    else:
        return 'Invalid username/password'
    
@app.route('/home')
def home():
    return 'light turned on/off'
if __name__ == '__main__':
    app.run()


