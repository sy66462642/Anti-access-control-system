from flask import Flask
from application.DB import db
from application.views.login import login_page
from application.views.regist import regist_page
from application.views.show_info import show_info_page

import os

app = Flask('Anti access control system', template_folder='templetes', static_folder='static',static_url_path='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

app.secret_key = "lalskskskskksksjsj"

db.init_app(app)

db.create_all()

app.register_blueprint(login_page)
app.register_blueprint(regist_page)
app.register_blueprint(show_info_page)


