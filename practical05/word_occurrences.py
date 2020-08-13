text = input("Text: ")
words = text.split(" ")
word_dir = {}

for word in words:
    if word in word_dir.keys():
        word_dir[word] += 1
    else:
        word_dir[word] = 1

for word in word_dir:
    print("{:{}} = {}".format(word, 10, word_dir[word]))
