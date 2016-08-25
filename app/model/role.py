# -*- coding: utf-8 -*-

"""

    coin.app.model.role
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from flask_security import RoleMixin
from app.model import db


class Role(db.Model, RoleMixin):

    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    name = db.Column(db.String(255), unique=True, nullable=False)

    description = db.Column(db.String(255))

    def __init__(self, name="", description=""):

        self.name = name

        self.description = description

    def __repr__(self):

        return self.name

    def to_json(self):

        role = dict()

        role["id"] = self.id

        role["name"] = self.name

        role["description"] = self.description

        return role
