import re

str = input('Enter string: ')
words = re.sub('\W', ' ', str).split()
for i in range(len(words)):
    words[i] = words[i].lower()
dictionary = {}
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for pair in dictionary:
    print('{0}: {1}'.format(pair, dictionary[pair]))
