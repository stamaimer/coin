# -*- coding: utf-8 -*-
from flask.ext.security import RoleMixin
from coin.models import db


class Role(db.Model, RoleMixin):

    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), unique=True)

    description = db.Column(db.String(255))

    def __init__(self, name, description=""):

        self.name = name

        self.description = description

    def __repr__(self):

        return "<Role(id=%d, name='%s', description='%s')>" % (self.id, self.name, self.description)

