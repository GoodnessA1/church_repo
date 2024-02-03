from flask import Flask
from model import db
from home.home import home_bp
from admin.admin import admin_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(admin_bp)

app.add_url_rule("/", endpoint='index')
if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True, host="0.0.0.0", port=3000)