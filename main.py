
from flask import Flask, render_template, request
app = Flask(__name__)
template_folder = '../templates'
app.debug = True

def render_active_page(template, name=''):
    return render_template(template, active=name)

@app.route('/')
def main_page():
    return render_active_page('index.html')

@app.route('/resume')
def resume_page():
    return render_active_page('resume.html', 'resume')

@app.route('/resume2')
def resume_page2():
    return render_active_page('resume2.html', 'resume2')
