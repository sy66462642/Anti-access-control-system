from flask import *
from ..model import students
from sqlalchemy.orm import sessionmaker

show_info_page = Blueprint('show_info_page', __name__)

"""@show_info_page.route('/inCampus', methods=['get', 'post'])
def show_in_info():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/inCampus.html')
    else:
        user_id = session.get("user_id")
        user = students.query.filter(id == user_id).first()
        user_name = user.name
        user_age = user.age
        user_gender = user.gender
        user_department = user.department
        user_photo = user.selfie
        return render_template('/inCampus.html', user_name=user_name, user_age=user_age, user_gender=user_gender,
                               user_department=user_department, user_photo=user_photo)


@show_info_page.route('/outCampus', methods=['get', 'post'])
def show_out_info():
    if request.method == 'GET':
        print('get_arrive')
        return render_template('/outCampus.html')
    else:
        user_id = session.get("user_id")
        user = students.query.filter(id == user_id).first()
        user_name = user.name
        user_age = user.age
        user_gender = user.gender
        user_department = user.department
        user_photo = user.selfie
        return render_template('/outCampus.html', user_name=user_name, user_age=user_age, user_gender=user_gender,
                               user_department=user_department, user_photo=user_photo)
"""
