def remove_even(listItems):
    result = []
    for i in listItems:
        if i % 2 != 0:
            result.append(i)
    return result


def remove_even_list_comprehension(listItems):
    result = [i for i in listItems if i % 2 != 0]
    print(result)


if __name__ == '__main__':
    myLists = [1, 2, 4, 5, 10, 6, 3]
    data = remove_even(myLists)
    remove_even_list_comprehension(myLists)
    print(data)
