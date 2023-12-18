#!/usr/bin/python3
""" a class State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ Class that defines prop of State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(130), nullable=False)

