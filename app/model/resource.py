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

    url = db.Column(db.String(255), unique=True)

    type = db.Column(db.String(255))

    def __init__(self, url="", type=""):
        self.url = url

        self.type = type

    def to_json(self):
        resource = dict()

        resource['id'] = self.id

        resource['url'] = self.url

        resource['type'] = self.type

        return resource
