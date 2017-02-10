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

    name = db.Column(db.Text())

    portfolio_piece = db.relationship('Portfolio_piece', backref='owner_portfolio', lazy='dynamic')

    owner_user = db.relationship('Pip_user', backref='portfolio', lazy='dynamic')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return self.name

    def to_json(self):
        portfolio = dict()

        portfolio['id'] = self.id

        portfolio['name'] = self.name

        portfolio['portfolio_piece'] = list()

        for piece in self.portfolio_piece:

            portfolio['portfolio_piece'].append(piece.to_json())

        return portfolio
