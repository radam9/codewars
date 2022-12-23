# https://www.codewars.com/kata/581c06b95cfa838603000435
# 5 Kyu
# Scraping: Codewars Top 500 Users

# My Solution
from bs4 import BeautifulSoup
import urllib.request as requests


class User:
    def __init__(self, name: str, honor: int, clan: str):
        self.name = name
        self.clan = clan
        self.honor = honor


class Leaderboard(object):
    def __init__(self):
        self.position = {}

    def add_user(self, index, user):
        self.position[index] = user


URL = "https://www.codewars.com/users/leaderboard"


def solution():
    leaderboard = Leaderboard()
    html = requests.urlopen(URL)
    soup = BeautifulSoup(html, "html.parser")
    table_rows = soup.findAll("tr")
    for index, row in enumerate(table_rows):
        name = row.get("data-username", None)
        if name:
            clan = row.contents[2].text or ""
            honor = int(row.contents[3].text.replace(",", ""))
            user = User(name=name, honor=honor, clan=clan)
            leaderboard.add_user(index, user)
    return leaderboard


# Codewars influenced solution
from bs4 import BeautifulSoup
from collections import namedtuple
import urllib.request as requests

Leaderboard = namedtuple("Leaderboard", ["position"])
User = namedtuple("User", ["name", "clan", "honor"])

URL = "https://www.codewars.com/users/leaderboard"


def solution():
    leaderboard = Leaderboard({})
    html = requests.urlopen(URL)
    soup = BeautifulSoup(html, "html.parser")
    table_rows = soup.findAll("tr", attrs={"data-username": True})
    for index, row in enumerate(table_rows, 1):
        name = row.get("data-username", None)
        clan = row.contents[2].text or ""
        honor = int(row.contents[3].text.replace(",", ""))
        leaderboard.position[index] = User(name, clan, honor)
    return leaderboard