from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/base')
def about():
    return render_template('base.html')

@app.route('/portfolio')
def contact():
    return render_template('portfolio-details.html')

@app.route('/course')
def course():
    return render_template('course.html')





app.run(debug=True)