from flask import *
from ..model import students, code
from sqlalchemy.exc import *
from sqlalchemy.orm import sessionmaker
from ..DB import db
from application.tools.regist_error_check import regist_error_check
from application.tools.code_generator import code_generator
from application.tools.conf import user_num
regist_page = Blueprint('regist_page', __name__)


@regist_page.route('/regist', methods=['get', 'post'])
def regist():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/regist.html')
    else:
        print('post_arrive')
        Id = request.form.get('username')
        pwd = request.form.get('password')
        gender = request.form.get('sex')
        name = request.form.get('studentname')
        age = request.form.get('age')
        department = request.form.get('department')
        photo = request.files.get('file')
        rgst_str = regist_error_check(Id, pwd, gender, age, photo)
        if rgst_str != '1':
            return render_template('/error.html', error=rgst_str)
        path = "static/photos"
        file_name = path + '/' + str(Id) + '.jpg'
        photo.save(file_name)
        selfie = './photos/' + str(Id) + '.jpg'
        ST = students(Id, pwd, name, gender, age, department, selfie, 0)
        try:
            db.session.add(ST)
            db.session.commit()
        except SQLAlchemyError:
            return render_template('/regist.html')
        limit = code.query.count()
        if limit > user_num:
            return render_template("/off.html")
        codestr = code_generator(int(Id))
        cod = code(codestr, int(Id), 0)
        db.session.add(cod)
        db.session.commit()
        return render_template('/codeget.html', code=codestr)
