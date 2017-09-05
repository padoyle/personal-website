
from flask import Flask, render_template, request
app = Flask(__name__)
template_folder = '../templates'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/resume')
def resume_page():
    return render_template('resume.html')

@app.rout('/about')
def about_page():
    return render_template('about.html')
