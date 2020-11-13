from flask import *
from ..model import students, code
from application.DB import db
from sqlalchemy.orm import sessionmaker

login_page = Blueprint('login_page', __name__)


@login_page.route('/', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/.html')
    else:
        print('post_arrive')
        id = request.form.get('id')
        pwd = request.form.get('password')

        user = students.query.filter(students.id == id).first()
        status = user.status
        if user and pwd == students.query.filter_by(students.id == id):
            session['user_id'] = user.id
            user_proof = code.query.filter_by(id == user.id).first()
            user_proof_num = user_proof.proof_num
            if user_proof_num == 0:
                return render_template('/codeCheck.html')
            else:
                code.query.filter_by(id == user.id).update({'proof_num', str(user_proof_num - 1)})
                db.session.commit()
                if status == 0:
                    students.query.filter(students.id == id).update({'status': '1'})
                    db.session.commit()
                    return render_template("/outCampus.html")
                else:
                    students.query.filter(students.id == id).update({'status': '0'})
                    db.session.commit()
                    return render_template("/inCampus.html")
        else:
            return render_template('/.html')
