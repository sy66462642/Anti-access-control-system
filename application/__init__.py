from flask import Flask
from application.DB import db
from application.views.login import login_page
from application.views.regist import regist_page
from application.views.show_info import show_info_page
from application.views.code_check import code_check_page
from application.model import students,code
import os

app = Flask('Anti access control system')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

app.secret_key = "lalskskskskksksjsj"


app.register_blueprint(login_page)
app.register_blueprint(regist_page)
app.register_blueprint(show_info_page)
app.register_blueprint(code_check_page)

db.init_app(app)
db.create_all(app=app)

if __name__=='main':
    app.run()


