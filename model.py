from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import Config

app=Config.create_app()
db = SQLAlchemy(app)

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

    # 照片上传后实现加密处理

    def __init__(self, id, password, name, gender, age, department, selfie, reason_for_out):
        self.id = id  # 邀请码
        self.name = name
        self.password = password
        self.gender = gender
        self.age = age
        self.department = department
        self.selfie = selfie
        self.reason_for_out = reason_for_out

        db.create_all()



