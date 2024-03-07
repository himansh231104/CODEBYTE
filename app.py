from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/base')
def about():
    return render_template('base.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio-details.html')

@app.route('/user-profile')
def user_profile():
    return render_template('user-profile.html')

@app.route('/python')
def python():
    return render_template('Courses/python.html')

@app.route('/java')
def java():
    return render_template('Courses/java.html')

@app.route('/c')
def c():
    return render_template('Courses/c.html')

@app.route('/cpp')
def cpp():
    return render_template('Courses/cpp.html')





app.run(debug=True)