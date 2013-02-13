'''
Sqlalchemy models corresponding to
nouns defined in the ontology.
'''

from sqlalchemy import Column, String

from terms.robots.schemata import Schema


class User(Schema):

    name = Column(String(20))
    surname = Column(String(20))
