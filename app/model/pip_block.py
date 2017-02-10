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

    pip_block_piece = db.relationship('Pip_block_piece', backref='owner_pip_block', lazy='dynamic')

    owner_user = db.relationship('Pip_user', backref='pip_block', lazy='dynamic')

    def __init__(self, name=""):
        self.name = name

    def __repr__(self):
        return self.name

    def to_json(self):
        pip_block = dict()

        pip_block['id'] = self.id

        pip_block['name'] = self.name

        pip_block['pip_block_piece'] = list()

        for piece in self.pip_block_piece:

            pip_block['pip_block_piece'].append(piece.to_json())

        return pip_block
