from flask import *
from ..model import students
from sqlalchemy.exc import *
from sqlalchemy.orm import sessionmaker
from ..DB import db


regist_page = Blueprint('regist_page', __name__)



@regist_page.route('/regist', methods=['get', 'post'])
def regist():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/regist.html')
    else:
        print('post_arrive')
        id = request.form.get('username')
        pwd = request.form.get('password')
        gender = request.form.get('sex')
        name = request.form.get('studentname')
        age = request.form.get('age')
        department = request.form.get('department')
        photo = request.files.get('file')
        print(type(photo))
        print(photo.name)
        path = "static/photos"
        file_name = path + '/' + str(id) + '.jpg'
        photo.save(file_name)
        ST = students(id, pwd, name, gender, age, department, file_name, 0)
        try:
            db.session.add(ST)
            db.session.commit()
        except SQLAlchemyError:
            return render_template('/regist.html')
    return render_template('/login.html')
