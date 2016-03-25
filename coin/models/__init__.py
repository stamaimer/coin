# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from coin import coin

db = SQLAlchemy(coin)

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

from role import Role
from user import User
from task import Task


def init_db():

    if coin.debug:

        coin.logger.info(coin.config["SQLALCHEMY_DATABASE_URI"])

        db.drop_all()

    db.create_all()

    admin_role = Role("admin")
    guest_role = Role("guest")

    db.session.add(admin_role)
    db.session.add(guest_role)

    test = User("test@example.com", "test", True, [guest_role])
    admin = User("admin@example.com", "admin", True, [admin_role])
    guest = User("guest@example.com", "guest", False, [guest_role])

    db.session.add(test)
    db.session.add(admin)
    db.session.add(guest)

    db.session.add(Task("task", "The First Task", admin))

    db.session.commit()
