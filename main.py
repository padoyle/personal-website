
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html.j2')

@app.route('/resume')
def resume_page():
    return render_template('resume.html.j2')
