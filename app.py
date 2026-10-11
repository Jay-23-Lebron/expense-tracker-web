from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/home')
def home():
    return "This is the /home page"

@app.route('/about')
def about():
    return "This is the /about page"

@app.route('/user/<username>')
def user_profile(username):
    return f"Welcome, user: {username}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)