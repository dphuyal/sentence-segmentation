import nltk


input_file = open("input.txt", "r")
text = input_file.read()
input_file.close()

sentences = nltk.sent_tokenize(text)


with open("outputSample.txt", "w") as s:
    s.writelines("%s\n" % line for line in sentences)
