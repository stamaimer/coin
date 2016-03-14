# -*- coding: utf-8 -*-
from coin import coin


def init_logger():

    if not coin.debug:

        from logging import Formatter

        from logging import FileHandler

        file_handler = FileHandler("./log/coin.log")

        file_handler.setFormatter(Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))

        coin.logger.addHandler(file_handler)
