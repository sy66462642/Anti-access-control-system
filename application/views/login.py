from flask import *
from ..model import students
from sqlalchemy.orm import sessionmaker
login_page = Blueprint('login_page', __name__)


@login_page.route('/login', methods=['get', 'post'])
def login():

    if request.method == 'GET':
        print('get_arrive')
        return render_template('/login.html')
    else:
        print('post_arrive')
        id = request.form.get('id')
        pwd = request.form.get('password')

        user = students.query.filter(students.id == id).first()

        if user and pwd==students.query.filter_by(students.id==id):
            session['user_id'] = user.id
            item=students.query.filter(students.id==id).first
            checkout=item.status
            if checkout==0:
                res = students.query.filter(students.id == id).update({"status": "1"})

                return render_template('/inCampus.html')
        else:
            return render_template('/login.html')
