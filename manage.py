# -*- coding: utf-8 -*-

"""

    coin.manage
    ~~~~~~~~~~~

    stamaimer 08/15/16

"""

import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.model import db
from app.model.user import User
from app.model.role import Role
from app.security import user_datastore
from config import config


app = create_app(config["default"])

migrate = Migrate(app, db)

manager = Manager(app)


def make_shell_context():

    return dict(app=app, db=db, User=User, Role=Role, user_datastore=user_datastore)

manager.add_command("shell", Shell(make_context=make_shell_context))

manager.add_command("db", MigrateCommand)


@manager.command
def create_db():

    pass


@manager.command
def delete_db():

    os.remove(os.path.join(os.getcwd(), "data.sqlite"))


@manager.command
def test():

    pass


@manager.command
def deploy():

    from flask_migrate import upgrade

    upgrade()


@manager.command
def profile(length=25, profile_dir=None):

    from werkzeug.contrib.profiler import ProfilerMiddleware

    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length], profile_dir=profile)

    app.run()


if __name__ == "__main__":

    manager.run()
