from flask import *
from ..model import students, code
from application.DB import db
from application.tools.gettime import getime
from sqlalchemy.orm import sessionmaker

login_page = Blueprint('login_page', __name__)


@login_page.route('/', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/login.html')
    else:
        print('post_arrive')
        Id = request.form.get('username')
        pwd = request.form.get('password')
        print(Id)
        print(type(Id))
        user = students.query.filter(Id==students.id).first()
        if user and (pwd == user.password):
            session['user_id'] = user.id
            status = user.status
            print(type(user.id))
            print((code.query.filter(int(Id) == code.id)))
            user_proof = code.query.filter(int(Id) == code.id).first()
            if not user_proof:
                """
                return render_template('/inCampus.html',user_name=user.name, user_age=user.age, user_gender=user.gender,
                               user_department=user.department, user_photo=user.selfie)"""
                return render_template('/login.html')
            user_proof_num = user_proof.proof_num
            if user_proof_num == 0:
                return render_template('/codeCheck.html')
            else:
                code.query.filter(Id == code.id).update({'proof_num': str(user_proof_num - 1)})
                db.session.commit()
                if status == 0:
                    students.query.filter(students.id == Id).update({'status': '1'})
                    db.session.commit()
                    return render_template("/outCampus.html",user_name=user.name, user_age=user.age, user_gender=user.gender,
                               user_department=user.department, user_photo=user.selfie,time=getime())
                else:
                    students.query.filter(students.id == Id).update({'status': '0'})
                    db.session.commit()
                    return render_template("/inCampus.html",user_name=user.name, user_age=user.age, user_gender=user.gender,
                               user_department=user.department, user_photo=user.selfie,time=getime())
        else:
            return render_template('/login.html')
