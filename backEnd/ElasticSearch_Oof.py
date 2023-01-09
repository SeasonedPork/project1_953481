from jikanpy import Jikan

jikan = Jikan


def search(input):
    if input != "":
        result = jikan.search(input)
    else:
        result = "Empty Input"
    return result
