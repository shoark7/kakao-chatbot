"""API for dictionary and movie schedule applications

"""
from bs4 import BeautifulSoup
import requests


DICT_URL_PREFIX = 'http://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query='


def dict_search(word):
    response = requests.get(DICT_URL_PREFIX + word)
    if response.status_code != 200:
        raise Exception("Something is wrong")

    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.find('span', class_='fnt_k05'):
        text = soup.find('span', class_='fnt_k05')
    else:
        raise AttributeError("That vocabulary doesn't exist in the dictonary")

    return text
