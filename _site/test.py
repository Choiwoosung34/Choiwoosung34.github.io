def LBYL(text):
    char_count_map = {}
    for c in text:
        if c in char_count_map:
            char_count_map[c] += 1
        else:
            char_count_map[c] = 1
    return char_count_map

def EAFP(text):
    char_count_map = {}
    for c in text:
        try:
            char_count_map[c] += 1
        except KeyError:
            char_count_map[c] = 1
    return char_count_map


text = """
Python For Beginners
Welcome! Are you completely new to programming? If not then we presume you will be looking for information about why and how to get started with Python. Fortunately an experienced programmer in any programming language (whatever it may be) can pick up Python very quickly. It's also easy for beginners to use and learn, so jump in!

Installing
Installing Python is generally easy, and nowadays many Linux and UNIX distributions include a recent Python. Even some Windows computers (notably those from HP) now come with Python already installed. If you do need to install Python and aren't confident about the task you can find a few notes on the BeginnersGuide/Download wiki page, but installation is unremarkable on most platforms.

Learning
Before getting started, you may want to find out which IDEs and text editors are tailored to make Python editing easy, browse the list of introductory books, or look at code samples that you might find helpful.

There is a list of tutorials suitable for experienced programmers on the BeginnersGuide/Tutorials page. There is also a list of resources in other languages which might be useful if English is not your first language.

The online documentation is your first port of call for definitive information. There is a fairly brief tutorial that gives you basic information about the language and gets you started. You can follow this by looking at the library reference for a full description of Python's many libraries and the language reference for a complete (though somewhat dry) explanation of Python's syntax. If you are looking for common Python recipes and patterns, you can browse the ActiveState Python Cookbook

Looking for Something Specific?
If you want to know whether a particular application, or a library with particular functionality, is available in Python there are a number of possible sources of information. The Python web site provides a Python Package Index (also known as the Cheese Shop, a reference to the Monty Python script of that name). There is also a search page for a number of sources of Python-related information. Failing that, just Google for a phrase including the word ''python'' and you may well get the result you need. If all else fails, ask on the python newsgroup and there's a good chance someone will put you on the right track.

Frequently Asked Questions
If you have a question, it's a good idea to try the FAQ, which answers the most commonly asked questions about Python.

Looking to Help?
If you want to help to develop Python, take a look at the developer area for further information. Please note that you don't have to be an expert programmer to help. The documentation is just as important as the compiler, and still needs plenty of work!
"""

import timeit
text *= 100

eafp_time = min(
    timeit.repeat(
        stmt="EAFP(text)",
        number=100,
        repeat=5,
        globals=globals(),
    )
)

lbyl_time = min(
    timeit.repeat(
        stmt="LBYL(text)",
        number=100,
        repeat=5,
        globals=globals(),
    )
)

print(f"이 경우 LBYL 이 {lbyl_time / eafp_time:.3f}배 만큼 EAFP 보다 느리다")
