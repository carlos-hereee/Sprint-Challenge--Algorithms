'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# Use recusion


def count_th(word):
    # use the count method for strings
    count = word.count('th')
    return count
    # TBC


count_th('the the')
