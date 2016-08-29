# -*- coding: utf-8 -*-

"""

    coin.app.model.user
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from werkzeug.security import check_password_hash, generate_password_hash
from flask_security import UserMixin
from app.model import db, roles_users


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    email = db.Column(db.String(255), unique=True, nullable=False, index=True)

    username = db.Column(db.String(255))

    password = db.Column(db.String(255), nullable=False)

    # password_hash = db.Column(db.String(255))

    # @property
    # def password(self):

    #     raise AttributeError("password is not a readable attribute")

    # @password.setter
    # def password(self, password):

    #     self.password_hash = generate_password_hash(password)

    # def verify_password(self, password):

    #     return check_password_hash(self.password_hash, password)

    active = db.Column(db.Boolean())

    confirmed_at = db.Column(db.DateTime())

    login_count = db.Column(db.Integer())

    last_login_at = db.Column(db.DateTime())

    last_login_ip = db.Column(db.String(15))

    current_login_at = db.Column(db.DateTime())

    current_login_ip = db.Column(db.String(15))

    roles = db.relationship("Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic"))

    # def __init__(self, email="", password=""):

    #     self.email = email

    #     self.password = password

    def __repr__(self):

        return self.email

    def to_json(self):

        user = dict()

        user["id"] = self.id

        user["email"] = self.email

        user["roles"] = self.roles

        user["active"] = self.active

        user["confirmed_at"] = self.confirmed_at

        user["login_count"] = self.login_count

        user["last_login_at"] = self.last_login_at

        user["last_login_ip"] = self.last_login_ip

        user["current_login_at"] = self.current_login_at

        user["current_login_ip"] = self.current_login_ip

        return user

    @staticmethod
    def generate_fake(count=47):

        from random import seed
        import forgery_py

        seed()

        for i in xrange(count):

            u = User(email=forgery_py.internet.email_address(),
                     username=forgery_py.internet.user_name(),
                     password=forgery_py.lorem_ipsum.word(),
                     active=True,
                     confirmed_at=forgery_py.date.date())

            db.session.add(u)

            try:

                db.session.commit()

            except:

                db.session.rollback()
