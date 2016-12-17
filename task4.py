import re

def isConsonant(str: str) -> bool:
    if re.findall(r'[bcdfghjklmnprstvwxz]', str) != []:
        return True
    return False


str = input('Enter string: ')
print(isConsonant(str))
