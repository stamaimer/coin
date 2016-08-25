# -*- coding: utf-8 -*-

"""

    coin.app.security
    ~~~~~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from flask_security import Security, SQLAlchemyUserDatastore
from app.model import db
from app.model.role import Role
from app.model.user import User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(datastore=user_datastore)
