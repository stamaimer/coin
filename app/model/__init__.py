# -*- coding: utf-8 -*-

"""

    coin.model
    ~~~~~~~~~~

    stamaimer 08/15/16

"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

roles_users = db.Table("roles_users",
                       db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
                       db.Column("role_id", db.Integer(), db.ForeignKey("role.id")))
