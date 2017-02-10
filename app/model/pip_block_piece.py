# -*- coding: utf-8 -*-

"""

    coin.app.model.cv
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Pip_block_piece(db.Model):
    __tablename__ = "pip_block_piece"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    keyword = db.Column(db.String())

    description = db.Column(db.Text())

    position = db.Column(db.Enum('left-top', 'left-bottom', 'right-top', 'right-bottom'), default='left-top')

    owner_pip_block_id = db.Column(db.Integer(), db.ForeignKey("pip_block.id"))

    def __init__(self, keyword=None, description=None, position=None):
        self.keyword = keyword

        self.description = description

        self.position = position

    def __repr__(self):

        return self.keyword

    def to_json(self):
        piece = dict()

        piece['id'] = self.id

        piece['keyword'] = self.keyword

        piece['description'] = self.description

        piece['position'] = self.position

        return piece
