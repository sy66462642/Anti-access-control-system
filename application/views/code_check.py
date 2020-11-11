
from flask import *
from ..model import students
from sqlalchemy.orm import sessionmaker
from ..DB import db

code_check_page = Blueprint('codeCheck_page', __name__)


@code_check_page.route('/codeCheck', method=['get', 'post'])
def check_code():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/codeCheck.html')
    else:

    return render_template('/regist.html')