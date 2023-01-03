#!/usr/bin/python3
"""string splitter by multiple delimiters"""


def text_indentation(text):
    """Function prints a text with 2 new lines after each of these characters
    : ., ? and :
    Args:
        text (str): text to be split
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    split_text = text_splitter(text, ('.', '?', ':'))
    for words in split_text:
        print(words, end="")


def text_splitter(texts, tag):
    """splits text by delimiter
    Args:
        texts (str)
        tag (tuple)
    """
    a, b, c = tag
    new_line = "\n\n"
    text1 = texts.split(a)
    text2 = "{}{}".format(a, new_line).join(i.lstrip() for i in text1).split(b)
    text3 = "{}{}".format(b, new_line).join(j.lstrip() for j in text2).split(c)
    text4 = "{}{}".format(c, new_line).join(k.lstrip() for k in text3)
    return text4
