def count_words(book_to_count):
    split_words = book_to_count.split()
    number_of_words = 0
    for words in split_words:
        number_of_words += 1
    return number_of_words

def character_count(words):
    dict_letters = {}
    for letters in words:
        lower_case = letters.lower()
        if lower_case in dict_letters:
            dict_letters[lower_case] += 1
        else:
            dict_letters[lower_case] = 1
    return dict_letters

def print_clean(dict,count):
    min_count = float("-inf")
    sorted = []
    updated_dict = {}
    for letters in dict:
        if letters.isalpha():
            sorted.append(dict[letters])
            
    sorted.sort(reverse=True)
    for number in sorted:
        for key in dict:
            if dict[key] == number:
                updated_dict[key] = number
            
    for stuff in updated_dict:
        print(f"{stuff}: {updated_dict[stuff]}")
    return