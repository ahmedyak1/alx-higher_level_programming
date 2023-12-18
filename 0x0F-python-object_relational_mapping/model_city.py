#!/usr/bin/python3
""" a class City"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()

class City(Base):
    """Module of a city"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(130), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

