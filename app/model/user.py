# -*- coding: utf-8 -*-

"""

    coin.model.user
    ~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app
from flask_security import UserMixin
from coin.model import db, roles_users


class User(db.Model, UserMixin):

    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    email = db.Column(db.String(255), unique=True, nullable=False, index=True)

    # password = db.Column(db.String(255), nullable=False)

    password_hash = db.Column(db.String(255))

    @property
    def password(self):

        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):

        self.password = generate_password_hash(password)

    def verify_password(self, password):

        return check_password_hash(self.password_hash, password)

    active = db.Column(db.Boolean(), default=False)

    # if current_app.config["SECURITY_CONFIRMABLE"]:
    #
    #     confirmed_at = db.Column(db.DateTime())
    #
    # if current_app.config["SECURITY_TRACKABLE"]:
    #
    #     login_count = db.Column(db.Integer())
    #
    #     last_login_at = db.Column(db.DateTime())
    #
    #     last_login_ip = db.Column(db.String(15))
    #
    #     current_login_at = db.Column(db.DateTime())
    #
    #     current_login_ip = db.Column(db.String(15))

    roles = db.relation("Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic"))

    def __init__(self, email="", password="", active=0, roles=[]):

        self.email = email

        self.roles = roles

        self.active = active

        self.password = password

    def __repr__(self):

        return self.email

    def to_json(self):

        user = dict()

        user["id"] = self.id

        user["email"] = self.email

        user["roles"] = self.roles

        user["active"] = self.active

        # if current_app.config["SECURITY_CONFIRMABLE"]:
        #
        #     user["confirmed_at"] = self.confirmed_at
        #
        # if current_app.config["SECURITY_TRACKABLE"]:
        #
        #     user["login_count"] = self.login_count
        #
        #     user["last_login_at"] = self.last_login_at
        #
        #     user["last_login_ip"] = self.last_login_ip
        #
        #     user["current_login_at"] = self.current_login_at
        #
        #     user["current_login_ip"] = self.current_login_ip

        return user
