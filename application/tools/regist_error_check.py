def fnd(strs):
    target = ['jpg', 'JPG', 'png', 'PNG']
    for i in target:
        if i == str:
            return True
    return False


def regist_error_check(userid, password, gender, age, photo):
    if not userid.isdigit():
        return "学号只能用数字"
    if len(password) < 4 and len(password) > 16:
        return "密码太短或太长"
    if not (gender == '男' or gender == '女'):
        return "性别只能为男或女"
    if not age.isdigit():
        return "年龄只能用数字"
    if not photo:
        return "请上传照片"
    return "1"
