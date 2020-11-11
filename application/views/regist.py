from flask import *
from ..model import students
from sqlalchemy.orm import sessionmaker
import os

regist_page = Blueprint('regist_page', __name__)

@regist_page.route('/codeCheck',method=['get','post'])
def codecheck():

@regist_page.route('/regist', method=['get', 'post'])
def regist():

    return render_template('/codeCheck.html')
