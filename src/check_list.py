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
        except LOLException as e:
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
    """
        <Name>
            LOLException

        <Description>
            This exception is raised when a wikipedia page does not contain a
            list of such word. The List-less Object is contained in the message
    """
    pass


def check_random_list():
    """
        <Name>
            check_random_list()

        <Description>
            Randomly picks a word from a dictionary and tries to fetch the
            wikipedia article of a list for it. If there is a list of this
            word, the word is returned. If there isn't a LOLException is
            raised.

        <Raises>
            LOLException(word): if there isn't a list of this word in wikipedia

        <Returns>
            word: the word that *does* contain a list
    """

    # get a random word from our magical wikipedia page
    randfile = linereader.copen(DICT)
    random_word = randfile.getline(random.randint(1, WC_DICT))

    query = "List of {}".format(random_word)
    try:
        page = wikipedia.page(query)
    except wikipedia.exceptions.PageError:
        raise LOLException(random_word)

    result_word = page.title.lstrip("List of")
    if result_word != random_word:
        raise LOLException(random_word)

    return random_word

if __name__ == "__main__":
    try:
        random_word = check_random_list()
    except LOLException as e:
        print("There is not a list of {}".format(e))
    else:
        print("There is a list of {}".format(random_word))
