from flask import *
from ..model import students, code
from sqlalchemy.orm import sessionmaker
from ..DB import db

code_check_page = Blueprint('codeCheck_page', __name__)


@code_check_page.route('/codeCheck', methods=['get', 'post'])
def check_code():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/codeCheck.html')
    else:
        print('post_arrive')
        id = session.get('id')
        code_for_proof = request.form.get('code')

        user = code.query.filter(code_for_proof.id == id).first()
        if not user:
            return render_template("/login.html")
        user_code = user.code
        status = user.status
        if user_code == code:
            code.query.filter(code.id == id).update({'proof_num': '20'})

            if status == 0:
                students.query.filter(students.id == id).update({'status': '1'})
                return render_template('/inCampus.html')
            else:
                students.query.filter(students.id == id).update({'status': '0'})
                return render_template('/outCampus.html')
        else:
            return render_template('/codeCheck.html')
