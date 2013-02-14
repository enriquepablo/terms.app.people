'''
Sqlalchemy models corresponding to
nouns defined in the ontology.
'''
from colanderalchemy import Column
from colanderalchemy import SQLAlchemyMapping

from sqlalchemy import String

from terms.core.schemata import Schema


class Person(Schema):

    name = Column(String(20))
    surname = Column(String(20))


person = SQLAlchemyMapping(Person)
