import re


str = input('Enter string: ')
words = re.sub('\W', ' ', str).split()
print(words)
