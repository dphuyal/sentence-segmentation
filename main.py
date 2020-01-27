# -*- coding: utf-8 -*-

'''
Name: Deep Phuyal
CSci 517-NLP Homework1
Sources cited: https://stackoverflow.com/questions/37691057/what-does-the-following-re-code-mean
https://regex101.com/r/nG1gU7/128
https://stackoverflow.com/questions/21639275/python-syntaxerror-non-ascii-character-xe2-in-file
https://stackoverflow.com/questions/11367902/negative-list-index

'''

import re

# Regex patterns
caps = "([A-Z])"
digits = "([0-9])"
prefixes = "(Mr|Ms|Mrs|St|Dr|Gov|MR|MS|MRS|ST|DR|GOV)[.]"
sent_starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Our\s|However\s|Moreover\s|Nevertheless\s)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"  # Matches the patterns like U.S. U.S.A. U.S.A.S. and so on

'''
A simple fileReader function that:
    opens the input data file,
    reads the entire file,
    and returns the read data
'''


def fileReader():
    data = open("input.txt", "r")
    data = data.read()
    return data


def splitTextIntoSentences():
    data = fileReader()
    data = data.replace("\n", " ")
    if 'Ph.D' in data:
        data = data.replace("Ph.D.", "Ph<period>D<period>")
    if '...' in data:
        data = data.replace("...", "<period><period><period>")

    data = re.sub(prefixes, "\\1<period>", data)  # Searches and replaces . with <period> and preserves the pattern inside () of prefixes before .
    data = re.sub("\s" + caps + "[.] ", " \\1<period> ", data)
    data = re.sub(acronyms + "[.]", "\\1<stop>", data)
    data = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]", "\\1<period>\\2<period>\\3<period>", data)
    data = re.sub(caps + "[.]" + caps + "[.]", "\\1<period>\\2<period>", data)
    data = re.sub(digits + "[.]" + digits, "\\1<period>\\2", data)

    data = data.replace(".", ".<stop>")     # Replaces all the occurence of "." in the text to .<stop>
    data = data.replace("?", "?<stop>")     # Replaces all the occurence of "?" in the text to ?<stop>
    data = data.replace("!", "!<stop>")     # Replaces all the occurence of "?" in the text to ?<stop>
    data = data.replace("<period>", ".")    # Replaces all the occurences of <period> in the text to "."
    sentences = data.split("<stop>")        # Splits data at "<stop>" and returns a list

    sentences = sentences[:-1]  # negative index to get rid of trailing new line
    sentences = [s.strip() for s in sentences]  # returns a copy of string with whitespace characters removed/striped from the beginning and the ending of the sentences

    # Creates a new file output.txt and loops until the len of sentences to write in the file
    file = open('output.txt', 'w')
    for i in range(len(sentences)):
        file.write(str(i + 1) + ". " + sentences[i] + "\n")


splitTextIntoSentences()
