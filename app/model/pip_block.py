# -*- coding: utf-8 -*-

"""

    coin.app.model.pip_block
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Pip_block(db.Model):
    __tablename__ = "pip_block"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    name = db.Column(db.Text())

    content = db.Column(db.Text())

    def __init__(self, name="", content=""):
        self.name = name

        self.content = content

    def __repr__(self):
        return self.name

    def to_json(self):
        pip_block = dict()

        pip_block['id'] = self.id

        pip_block['name'] = self.name

        pip_block['content'] = self.content

        return pip_block
