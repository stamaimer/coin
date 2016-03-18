# -*- coding: utf-8 -*-
from coin.models import db


class Task(db.Model):

    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))

    desc = db.Column(db.Text)

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    creator = db.relationship("User", backref=db.backref("task", lazy="dynamic"))

    def __init__(self, name, desc, creator):

        self.name = name

        self.desc = desc

        self.creator = creator

    def __repr__(self):

        # return "<Task(id='%d', name='%s', desc='%s')>" % (self.id, self.name, self.desc)

        return self.name