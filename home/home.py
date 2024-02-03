from flask import (Blueprint, render_template, request, url_for, redirect)
from model import insert_all
home_bp = Blueprint('home_bp', __name__, template_folder='templates',
                    static_folder='static')

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['uname']
        email = request.form['email']
        phone_number = request.form['phone_number']
        prayer_request = request.form['prayer_request']
        inpt = [name, email, phone_number, prayer_request]
        insert_all(inpt)
        return render_template('successful.html')
    return render_template('index.html')