import click
from sqlalchemy.orm.exc import NoResultFound

from nkcli.config import read_conf
from nkcli.db import Session, setup
from nkcli.horse import Horse
from nkcli.scraper import Scraper


@click.group()
def root():
    global Session
    conf = read_conf("./config.toml")
    Session = setup(conf["database"]["url"])


@root.command()
@click.argument("horse_id")
def info(horse_id):
    session = Session()
    try:
        horse = session.query(Horse).filter(Horse.netkeiba_id == horse_id).one()
    except NoResultFound:
        scraper = Scraper()
        horse = scraper.get_horse(horse_id)
        pedigree = scraper.get_pedigree(horse_id)
        horse.sire = pedigree.sire["id"]
        horse.dam = pedigree.dam["id"]
        session.add(horse)
        session.commit()
    horse.print()
    if horse.sire:
        try:
            sire = session.query(Horse).filter(Horse.netkeiba_id == horse.sire).one()
        except NoResultFound:
            scraper = Scraper()
            sire = scraper.get_horse(horse.sire)
            pedigree = scraper.get_pedigree(horse.sire)
            sire.sire = pedigree.sire["id"]
            sire.dam = pedigree.dam["id"]
            session.add(sire)
            session.commit()
        print("Sire:     ", sire.name, "/", sire.netkeiba_id)
    if horse.dam:
        try:
            dam = session.query(Horse).filter(Horse.netkeiba_id == horse.dam).one()
        except NoResultFound:
            scraper = Scraper()
            dam = scraper.get_horse(horse.dam)
            pedigree = scraper.get_pedigree(horse.dam)
            dam.sire = pedigree.sire["id"]
            dam.dam = pedigree.dam["id"]
            session.add(dam)
            session.commit()
        print("Dam:      ", dam.name, "/", dam.netkeiba_id)


@root.command()
@click.argument("horse_id")
def pedigree(horse_id):
    scraper = Scraper()
    pedigree = scraper.get_pedigree(horse_id)
    pedigree.print()


@root.command()
@click.argument("user_id")
def favorite(user_id, cookie=None):
    scraper = Scraper()
    if cookie != None:
        user_id = scraper.cookie_to_id(cookie)
    scraper.user_favorite(user_id)

"""
@root.command()
def sire_ranking():
    print("sire-ranking")
"""

if __name__ == "__main__":
    root()