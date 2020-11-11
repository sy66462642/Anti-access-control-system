from application.DB import db
from application import Config

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    __tablename__ = "users"
    password = db.Column(db.String(16))
    name = db.Culumn(db.String(10))
    gender = db.Culumn(db.String(10))
    age = db.Column(db.Integer)
    department = db.Column(db.String(40))
    selfie = db.Column(db.String(100))
    reason_for_out = db.Column(db.String(100))
    status=db.Column(db.Integer)

    # 照片上传后实现加密处理

    def __init__(self, id, password, name, gender, age, department, selfie, reason_for_out,status):
        self.id = id  # 邀请码
        self.name = name
        self.password = password
        self.gender = gender
        self.age = age
        self.department = department
        self.selfie = selfie
        self.reason_for_out = reason_for_out
        self.status=status

    def __repr__(self):
       return '<Student_id:%r>' % self.id



