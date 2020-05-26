import re


def text_analyzer(str=None, *args):
    """This function count the numbers of upper characters,lower characters,
    ponctuation marks and spaces of your text."""
    if len(args) > 0:
        print("ERROR")
        exit()
    if str is None:
        str = input("What is the text to analyze?\n>> ")
    print("The text contains {} characters:\n".format(len(str)))
    print("-", sum(1 for c in str if c.isupper()), "upper letters\n")
    print("-", sum(1 for c in str if c.islower()), "lower letters\n")
    print("-", len(re.findall(r'[.,:!?;\'-]', str)), "punctuation marks\n")
    print("-", str.count(' '), "spaces")
