# -*- coding: utf-8 -*-

"""

    coin.app.model.resource
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Resource(db.Model):
    __tablename__ = "resource"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    path = db.Column(db.String(255))

    name = db.Column(db.String(255), unique=True)

    type = db.Column(db.String(255))

    def __init__(self, path="", name="", type=""):
        self.path = path

        self.name = name

        self.type = type

    def __repr__(self):
        return self.name

    def to_json(self):
        resource = dict()

        resource['id'] = self.id

        resource['name'] = self.name

        resource['path'] = self.path

        resource['type'] = self.type

        return resource
