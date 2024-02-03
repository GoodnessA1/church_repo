from flask import (Blueprint, render_template, url_for, request, redirect)
from model import load_all

admin_bp = Blueprint('admin_bp', __name__, url_prefix="/admin",
                     static_folder='static', template_folder='templates')

@admin_bp.route('/home')
def index():
    data = load_all()
    for d in data:
        print("Name: ", d.name)
        print("Email: ", d.email)
        print("phone number: ", d.phone_number)
        print("Prayer Request: ", d.prayer_request)
    return render_template('home.html', data=data)

@admin_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin_name = request.form['admin_name']
        password = request.form['password']

        if (admin_name == 'Abisoye Joshua') & (password == 'goodness1234'):
            return (redirect(url_for('admin_bp.index')))
        
        else:
            return (redirect(url_for('admin_bp.login')))
    return render_template('login.html')