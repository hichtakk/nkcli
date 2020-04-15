from sqlalchemy import create_engine, Column, Integer, String, Boolean
#from sqlalchemy import relationship

from nkcli.db import Base, create_session


class Horse(Base):
    __tablename__ = "horse"

    id = Column(Integer(), primary_key=True, nullable=False)
    netkeiba_id = Column(String(10), unique=True, nullable=False)
    name = Column(String(32), nullable=False)
    sex = Column(String(8), nullable=False)
    foaled = Column(Integer)
    color = Column(String())
    record = Column(String())
    earnings = Column(String())
    retired = Column(Boolean())
    sire = Column(String(10))
    dam = Column(String(10))

    def __init__(self, id_):
        self.netkeiba_id = id_

    def print(self):
        print("ID:       ", self.netkeiba_id)
        print("Name:     ", self.name)
        print("Retired:  ", self.retired)
        print("Sex:      ", self.sex)
        print("Foaled:   ", self.foaled)
        print("Color:    ", self.color)
        print("Record:   ", self.record)
        print("Earnings: ", self.earnings)


class Pedigree(object):
    __tablename__ = "pedigree"

    def __init__(self, sire, dam):
        self.sire = sire
        self.dam = dam

    def print(self):
        if self.sire["international_name"] != "":
            print("Sire: {} {} ({})".format(self.sire["id"], self.sire["name"], self.sire["international_name"]))
        else:
            print("Sire: {} {}".format(self.sire["id"], self.sire["name"]))

        if self.dam["international_name"] != "":
            print("Dam:  {} {} ({})".format(self.dam["id"], self.dam["name"], self.dam["international_name"]))
        else:
            print("Dam:  {} {}".format(self.dam["id"], self.dam["name"]))
