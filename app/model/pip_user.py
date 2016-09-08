# -*- coding: utf-8 -*-

"""

    coin.app.model.pip_user
    ~~~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from app.model import db, roles_users


class Pip_user(db.Model):

    __tablename__ = "pip_user"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    email = db.Column(db.String(255), unique=True, nullable=False, index=True)

    password = db.Column(db.String(255), nullable=False)

    name = db.Column(db.String(255))

    title = db.Column(db.String(255))

    department = db.Column(db.String(255))

    info = db.Column(db.Text())

    access_code = db.Column(db.String(255))

    photo = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    video = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    podcast = db.Column(db.Integer(), db.ForeignKey("podcast.id"))

    cv = db.Column(db.Integer(), db.ForeignKey("cv.id"))

    news = db.Column(db.Integer(), db.ForeignKey("news.id"))

    portfolio = db.Column(db.Integer(), db.ForeignKey("portfolio.id"))

    pip_block = db.Column(db.Integer(), db.ForeignKey("pip_block.id"))

    def __init__(self, email=None, password=None, name=None, title=None, department=None, info=None, access_code=None, photo=None, video=None, podcast=None, cv=None, news=None, portfolio=None, pip_block=None):

        self.email = email

        self.password = password

        self.name = name

        self.title = title

        self.department = department

        self.info = info

        self.access_code = access_code

        self.photo = photo

        self.video = video

        self.podcast = podcast

        self.cv = cv

        self.news = news

        self.portfolio = portfolio

        self.pip_block = pip_block

    # def __repr__(self):
    #
    #     return self.email

    def to_json(self):

        pip_user = dict()

        pip_user['id'] = self.id

        pip_user['email'] = self.email

        pip_user['password'] = self.password

        pip_user['name'] = self.name

        pip_user['title'] = self.title

        pip_user['department'] = self.department

        pip_user['info'] = self.info

        pip_user['access_code'] = self.access_code

        pip_user['photo'] = self.photo

        pip_user['video'] = self.video

        pip_user['podcast'] = self.podcast

        pip_user['cv'] = self.cv

        pip_user['news'] = self.news

        pip_user['portfolio'] = self.portfolio

        pip_user['pip_block'] = self.pip_block

        return pip_user
