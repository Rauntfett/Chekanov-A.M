def change_order_of_words() -> str:
    string = str(input('Введите строку '))
    list_of_splited_words = string.split()
    reversed_list_of_splited_words = []
    for element in list_of_splited_words[::-1]:
        reversed_list_of_splited_words.append(element)
    new_string = ' '.join(reversed_list_of_splited_words)
    return new_string


print(change_order_of_words())