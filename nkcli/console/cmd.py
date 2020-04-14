import click

from nkcli.scraper import Scraper

@click.group()
def rootCmd():
    pass


@rootCmd.command()
@click.argument("horse_id")
def info(horse_id):
    scraper = Scraper()
    horse = scraper.get_horse(horse_id)
    horse.print()


@rootCmd.command()
@click.argument("horse_id")
def pedigree(horse_id):
    scraper = Scraper()
    pedigree = scraper.get_pedigree(horse_id)
    pedigree.print()


@rootCmd.command()
@click.argument("cookie")
def favorite(cookie):
    scraper = Scraper()
    user_id = scraper.cookie_to_id(cookie)
    scraper.user_favorite(user_id)

"""
@rootCmd.command()
def sire_ranking():
    print("sire-ranking")
"""