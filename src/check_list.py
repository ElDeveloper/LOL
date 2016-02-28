#!/usr/bin/env python
"""
    <name>
        check_list.py

    <Description>
        Obtains a random word from /usr/share/words and checks
        if there is a list of that. 

    <Usage>
        from check_list import check_random_list, LOLException
        try:
            check_random_list()
        Except LOLException as e:
            print("{}".format(e))
        else:
            print("No new list-less object for LOL")
""" 
import wikipedia
import linereader
import random

DICT = "../dict.txt"
WC_DICT = 48915

class LOLException(Exception):
    pass

def check_random_list():

    # get a random word from our magical wikipedia page 
    randfile = linereader.copen(DICT)
    random_word = randfile.getline(random.randint(1, WC_DICT))

    try:
        query = "List of {}".format(random_word)
        page = wikipedia.page(query)
        result_word = page.title.lstrip("List of")
        if result_word != random_word:
            raise LOLException(random_word)
    except wikipedia.exceptions.PageError:
        raise LOLException(random_word)
    
    return random_word

if __name__ == "__main__":
    try:
        random_word = check_random_list()
    except LOLException as e:
        print("There is not a list of {}".format(e))
    else:
        print("There is a list of {}".format(random_word))

