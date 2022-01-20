from inspect import signature


def remove_duplicates(elements: list) -> list:
    """
    :param elements
    :return: список с числами, которые были уникальными во входном списке
    """
    for char in elements:
        if not isinstance(char, (int, float)):
            raise TypeError('список должен содержать числа')
    if type(elements) != list:
        raise TypeError('функция должна принимать не пустой список')
    if len(elements) == 0:
        raise ValueError('список должен содержать хотя бы одно число')
    
    return list(filter(lambda e: elements.count(e) == 1, elements))


if __name__ == "__main__":
    result = remove_duplicates([1, 2, 1.0])
    print(result)
    
    
