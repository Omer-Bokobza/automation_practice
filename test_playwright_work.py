from playwright_work import valid_input, buy_dress
import time
from playwright.sync_api import sync_playwright
import logging
import pytest


# add your specific path to filename to get the log text file
log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()


@pytest.fixture
def user():
    data =  {
      "email": "asdasd@wxz.com",
      "password": "123456"
    }
    return data


def test_email(user):
    log.info("test empty email")
    assert valid_input("", user["password"], "An email address required")
    log.debug("test was successful you didn't log in")


def test_password(user):
    log.info("test empty password")
    assert valid_input(user["email"], "", "Password is required")
    log.debug("test was successful you didn't log in")


def test_wrong_email(user):
    log.info("test wrong email")
    assert valid_input("asdasdwxz.com", user["password"], "Invalid email address")
    log.debug("test was successful you didn't log in")


def test_wrong_password(user):
    log.info("test wrong password")
    assert valid_input(user["email"], "000", "Invalid password")
    log.debug("test was successful you didn't log in")

def test_user():
    log.info("test none-existing user")
    assert valid_input("asdzgfgfgh@yahoo.com", "13467985", "Authentication failed")
    log.debug("test was successful you didn't log in")


def test_buy_dress(user):
    lowest_price_dress = 16.40
    log.info("test buying cheapest dress")
    assert buy_dress() == lowest_price_dress
    log.debug("test was successful you buy the cheapest summer dress")
