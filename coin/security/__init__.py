# -*- coding: utf-8 -*-
from flask.ext.security import Security, SQLAlchemyUserDatastore
from coin import coin
from coin.models import db, Role, User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(coin, user_datastore)

user_datastore.create_user(email="stamaimer@gmail.com", password="stamaimer")

db.session.commit()
