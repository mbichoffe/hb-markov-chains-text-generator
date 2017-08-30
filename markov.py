"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    f = open(file_path)

    text = f.read()

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()


    # for i in range(len(words) - 2):
    #     key = (words[i], words[i+1])
    #     if key not in chains:
    #         chains[(words[i], words[i+1])] = []

    #     chains[key].append(words[i+2])

    #

    # return chains

    # try using D.setdefault(K, [default])

    for i in range(len(words) - 2):
        key = (words[i], words[i+1])
        chains.setdefault(key, []).append(words[i+2])

    return chains


def make_text(chains):
    """Return text from chains."""
    # get random key to start the link
        # append into words list
        # look up key in dictionary
            # get random word within the list
            # append into words list
        # evaluate last two words in words[] to find key in dictionary
    words = []

    start_link = choice(chains.keys())

    [words.append(word) for word in start_link]

    third_word = choice(chains[start_link])

    words.append(third_word)
    blob = True
    while blob:
        last_two_words = (words[-2], words[-1])
        if last_two_words not in chains:
            blob = False

        words.append(choice(chains[last_two_words]))

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print input_text

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
