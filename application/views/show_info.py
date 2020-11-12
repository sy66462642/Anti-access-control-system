from flask import *
from ..model import students
from sqlalchemy.orm import sessionmaker
show_info_page = Blueprint('show_info_page', __name__)
