# -*- coding: utf-8 -*-

"""

    manage
    ~~~~~~

    stamaimer 08/15/16

"""

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from coin import create_app
from coin.model import db

app = create_app("config.development")

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command("db", MigrateCommand)


if __name__ == "__main__":

    manager.run()
