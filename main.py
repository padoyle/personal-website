
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
