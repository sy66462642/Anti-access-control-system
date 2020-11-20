from application.DB import db



class students(db.Model):
    __table_args__ = {"useexisting": True}
    id = db.Column('student_id', db.Integer, primary_key=True)
    __tablename__ = "students"
    password = db.Column(db.String(16))
    name = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    department = db.Column(db.String(40))
    selfie = db.Column(db.String(100))
    status = db.Column(db.Integer)

    # 照片上传后实现加密处理

    def __init__(self, id, password, name, gender, age, department, selfie, status):
        self.id = id  # 登录码
        self.name = name
        self.password = password
        self.gender = gender
        self.age = age
        self.department = department
        self.selfie = selfie
        self.status = status

    def __repr__(self):
        return '<Student_id:%r>' % self.id


class code(db.Model):
    __table_args__ = {"useexisting": True}
    __tablename__ = "codes"
    id = db.Column('id', db.Integer, primary_key=True)
    code = db.Column('code', db.String(16))
    proof_num = db.Column('proof', db.Integer)

    def __init__(self, codes, sid, proof_num):
        self.code = codes
        self.id = sid
        self.proof_num = proof_num

    def __repr__(self):
        return '<id:%r>' % self.id