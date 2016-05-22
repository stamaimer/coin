# -*- coding: utf-8 -*-

from coin import coin


def init_logger():

    if not coin.debug:

        import logging

        from logging import getLogger

        from logging import Formatter

        from logging import FileHandler

        from logging.handlers import SMTPHandler

        file_handler = FileHandler("./log/coin.log")

        file_handler.setFormatter(Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))

        mail_handler = SMTPHandler("127.0.0.1",
                                   "error@coin.com",
                                   ["stamaimer@gmail.com"],
                                   "Coin Failed")

        mail_handler.setFormatter(Formatter('''
        Message type:       %(levelname)s
        Location:           %(pathname)s:%(lineno)d
        Module:             %(module)s
        Function:           %(funcName)s
        Time:               %(asctime)s

        Message:

        %(message)s
        '''))

        mail_handler.setLevel(logging.ERROR)

        coin.logger.addHandler(file_handler)

        coin.logger.addHandler(mail_handler)

        coin.logger.addHandler(getLogger("sqlalchemy"))
