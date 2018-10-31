"""
Program to prompt user for page title or search phrase, then prints the title, summary and URL,
loops until user input is blank.
"""

import wikipedia

def wiki_mini_search():
    search = input("Enter page title or search phrase: ")
    while search != " ":
        print(wikipedia.summary(search))
        summary = wikipedia.page(search)
        print(summary.title)
        print(summary.summary)
        print(summary.url)
        search = input("Enter page title or search phrase: ")
    print("Thanks for searching")

    # This fails to work, unsure why??
    #     try:
    #         search = wikipedia.summary(search)
    #     except wikipedia.exceptions.DisambiguationError as e:
    #         print(e.options)
    #         print(search.title, search.summary, search.url)
    # search = input("Enter page title or search phrase: ")


wiki_mini_search()
