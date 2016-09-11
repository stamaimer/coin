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

    photo_id = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    photo = db.relationship('Resource', foreign_keys=photo_id)

    video_id = db.Column(db.Integer(), db.ForeignKey("resource.id"))

    video = db.relationship('Resource', foreign_keys=video_id)

    podcast_id = db.Column(db.Integer(), db.ForeignKey("podcast.id"))

    podcast = db.relationship('Podcast', foreign_keys=podcast_id)

    cv_id = db.Column(db.Integer(), db.ForeignKey("cv.id"))

    cv = db.relationship('Cv', foreign_keys=cv_id)

    news_id = db.Column(db.Integer(), db.ForeignKey("news.id"))

    news = db.relationship('News', foreign_keys=news_id)

    portfolio_id = db.Column(db.Integer(), db.ForeignKey("portfolio.id"))

    portfolio = db.relationship('Portfolio', foreign_keys=portfolio_id)

    pip_block_id = db.Column(db.Integer(), db.ForeignKey("pip_block.id"))

    pip_block = db.relationship('Pip_block', foreign_keys=pip_block_id)

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

        pip_user['photo_id'] = self.photo_id

        pip_user['video_id'] = self.video_id

        pip_user['podcast_id'] = self.podcast_id

        pip_user['cv_id'] = self.cv_id

        pip_user['news_id'] = self.news_id

        pip_user['portfolio_id'] = self.portfolio_id

        pip_user['pip_block_id'] = self.pip_block_id

        return pip_user
