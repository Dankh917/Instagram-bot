import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bot_functions import login,follow_sugg,unfollow,like_ph_hashtag


def main():
    login()
    follow_sugg()
    unfollow()
    like_ph_hashtag("your hashtag here without the '#'")

main()