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
        Id = session.get('user_id')
        code_for_proof = request.form.get('code')
        #print(type(Id))
        user = code.query.filter(code.id == int(Id)).first()
        if not user:
            return render_template("/login.html")
        user_code = user.code
        St=students.query.filter(students.id==Id).first()
        status = St.status
        #print(user_code)
        #print(code_for_proof)
        if user_code == code_for_proof:
            code.query.filter(code.id == code_for_proof).update({'proof_num': '2000'})
            db.session.commit()
            if status == 0:
                students.query.filter(students.id == Id).update({'status': '1'})
                db.session.commit()
                return render_template('/inCampus.html',user_name=St.name, user_age=St.age, user_gender=St.gender,
                               user_department=St.department, user_photo=St.selfie)
            else:
                students.query.filter(students.id == Id).update({'status': '0'})
                db.session.commit()
                return render_template('/outCampus.html',user_name=St.name, user_age=St.age, user_gender=St.gender,
                               user_department=St.department, user_photo=St.selfie)
        else:
            return render_template('/codeCheck.html')
