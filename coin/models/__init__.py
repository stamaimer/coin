# -*- coding: utf-8 -*-

"""
    coin.models
    ~~~~~~~~~~~


"""
from flask.ext.sqlalchemy import SQLAlchemy
from coin import coin

db = SQLAlchemy(coin)

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

