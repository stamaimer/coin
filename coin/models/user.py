# -*- coding: utf-8 -*-
from flask.ext.security import UserMixin
from coin.models import coin, db, roles_users


class User(db.Model, UserMixin):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), unique=True)

    active = db.Column(db.Boolean)

    password = db.Column(db.String(255))

    if coin.config["SECURITY_CONFIRMABLE"]:

        confirmed_at = db.Column(db.DateTime)

    if coin.config["SECURITY_TRACKABLE"]:

        login_count = db.Column(db.Integer)

        last_login_at = db.Column(db.DateTime)

        last_login_ip = db.Column(db.String(255))

        current_login_at = db.Column(db.DateTime)

        current_login_ip = db.Column(db.String(255))

    roles = db.relationship("Role", secondary=roles_users, backref=db.backref("user", lazy="dynamic"))

    def __init__(self, email, password, active=False, roles=[]):

        self.email = email

        self.roles = roles

        self.active = active

        self.password = password

    def __repr__(self):

        return "<User(id=%d, email='%s', password='%s')>" % (self.id, self.email, self.password)