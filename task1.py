def getMaxItem(mas: list) -> int:
    max = mas[0]
    for x in mas:
        if x > max:
            max = x
    return max


def getMinItem(mas: list) -> int:
    min = mas[0]
    for x in mas:
        if x < min:
            min = x
    return min
