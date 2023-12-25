def find_in_different_registers(words: list[str]):
    temp = dict()
    for word in words:
        if word not in temp:
            temp[word] = 1
        else:
            temp[word] += 1
    res = set()
    duplicates = set()
    for i in temp:
        if temp[i] > 1:
            duplicates.add(i.lower())
    for i in temp:
        if i.lower() not in duplicates:
            res.add(i.lower())
    return list(res)


if __name__ == '__main__':
    words = ["Мама", "МАМА", "Мама", "папа", "ПАПА", "Мама", "ДЯдя", "брАт", "Дядя", "Дядя", "Дядя"]
    print(find_in_different_registers(words))
