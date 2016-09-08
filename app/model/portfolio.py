# -*- coding: utf-8 -*-

"""

    coin.app.model.portfolio
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Portfolio(db.Model):
    __tablename__ = "portfolio"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    content = db.Column(db.Text())

    def __init__(self, content=""):
        self.content = content

    def to_json(self):
        portfolio = dict()

        portfolio['id'] = self.id

        portfolio['content'] = self.content

        return portfolio
