# -*- coding: utf-8 -*-

"""

    coin.app.model.cv
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db


class Portfolio_piece(db.Model):
    __tablename__ = "portfolio_piece"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    #
    # photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    title = db.Column(db.String())

    summary = db.Column(db.String())

    detail = db.Column(db.Text())

    pic_id = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    pic = db.relationship('Resource', foreign_keys=pic_id)

    owner_portfolio_id = db.Column(db.Integer(), db.ForeignKey("portfolio.id"))

    def __init__(self, title=None, summary=None, detail=None, pic=None):
        self.title = title

        self.summary = summary

        self.detail = detail

        self.pic = pic

    def __repr__(self):

        return self.title

    def to_json(self):
        piece = dict()

        piece['id'] = self.id

        piece['title'] = self.title

        piece['summary'] = self.summary

        piece['detail'] = self.detail

        piece['pic'] = self.pic.to_json()

        return piece
