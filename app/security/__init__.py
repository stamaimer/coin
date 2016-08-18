# -*- coding: utf-8 -*-

"""

    coin.security
    ~~~~~~~~~~~~~

    stamaimer 08/16/16

"""

from flask_security import Security, SQLAlchemyUserDatastore
from coin.model import db
from coin.model.role import Role
from coin.model.user import User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(user_datastore)
