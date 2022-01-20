

def expanded_form(n: int) -> str:
    """
    :param n:
    :return: полученное число в виде строки
    """
    if n <= 0:
        raise ValueError('число должно быть положительным')
    if type(n) != int:
        raise TypeError('функция должна принимать положительное число')
    s = str(n)
    res = ''
    l = len(s) - 1
    for digit in s:
        if digit != '0':
            res += digit + '0' * l + ' + '
        l -= 1
    return res[:-3]


if __name__ == "__main__":
    result = expanded_form(108)
    print(result)

