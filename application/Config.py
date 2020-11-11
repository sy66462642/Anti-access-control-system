from flask import Flask


def create_app(port=5000, ip='127.0.0.1', debug=False):
    app = Flask(__name__, template_folder='templetes', static_folder='static', static_url_path='../static')
    app.config['SQLALCHEMY_DATABASE_URI'] = ""
    app.run(debug=debug, port=port, host=ip)
    return app
