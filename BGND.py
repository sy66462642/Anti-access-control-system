from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

import Config
import model
app=Config.create_app()



@app.route('/register',method=['get','post'])
def register():
    return


@app.route('/login',method=['get','post'])
def login():
    return


@app.route('/showinfo',method=['get','post'])
def showinfo(sts):

    return



