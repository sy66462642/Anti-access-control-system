
from flask import *
from ..model import students,code
from sqlalchemy.orm import sessionmaker
from ..DB import db

code_check_page = Blueprint('codeCheck_page', __name__)


@code_check_page.route('/codeCheck', method=['get', 'post'])
def check_code():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/codeCheck.html')
    else:
        print('post_arrive')
        id=request.form.get('id')
        code=request.form.get('code')

        user=code.query.filter(code.id==id).first()
        user_code=user.code
        status=user.status
        if user_code == code:
            code.query.filter_by(code.id==id).update('proof_num':'20')
            return render_template('/')
        else:
            if status==0:
                students.query.filter_by(students.id==id).update('status':'1')
                return render_template('/inCampus.html')
            else:
                students.query.filter_by(students.id==id).update('status':'0')
                return render_template('/outCampus.html')

    return render_template('/regist.html')