import re

text = """The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events."""


def search_and_replace():
    global text

    result = False

    adj = re.compile(r"\bADJECTIVE\b")
    noun = re.compile(r"\bNOUN\b")
    verb = re.compile(r"\bVERB\b")

    match = adj.search(text)
    if match:
        result = True
        word = input("Enter an adjective: ")
        text = text[: match.start()] + word + text[match.end() :]

    match = noun.search(text)
    if match:
        result = True
        word = input("Enter a noun: ")
        text = text[: match.start()] + word + text[match.end() :]

    match = verb.search(text)
    if match:
        result = True
        word = input("Enter a verb: ")
        text = text[: match.start()] + word + text[match.end() :]

    return result


def main():
    global text
    while search_and_replace():
        pass

    print(text)


if __name__ == "__main__":
    main()
