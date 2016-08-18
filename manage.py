# -*- coding: utf-8 -*-

"""

    manage
    ~~~~~~

    stamaimer 08/15/16

"""

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.model import db
from app.model.user import User
from app.model.role import Role
from app.security import user_datastore

app = create_app("config.development.DevelopmentConfig")

migrate = Migrate(app, db)

manager = Manager(app)


def make_shell_context():

    return dict(app=app, db=db, User=User, Role=Role, user_datastore=user_datastore)

manager.add_command("shell", Shell(make_context=make_shell_context))

manager.add_command("db", MigrateCommand)


if __name__ == "__main__":

    manager.run()
