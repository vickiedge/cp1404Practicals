word_count_dict = {}
text = input("Text: ")
word_list = text.split()

for word in word_list:
    word_count_dict[word] = word_count_dict.get(word, 0) + 1

print(text)
#for word, count in word_count_dict.items():
#    print("{} : {}".format(word, count))
words = list(word_count_dict.keys())
words.sort()
max_length = max((len(word) for word in words))
print(max_length)
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count_dict[word]))


