# -*- coding: utf-8 -*-

from . import *

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)