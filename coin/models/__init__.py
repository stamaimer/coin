# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select, text

print sqlalchemy.__version__

engine = create_engine("", convert_unicode=True)

Base = declarative_base()

Base.metadata.bind = engine

import user

import task

import record

Base.metadata.create_all()

session = scoped_session(sessionmaker(bind=engine))

