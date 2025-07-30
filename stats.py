def count_book_words(book_content):
    num_words = len((book_content.split()))
    return num_words
    
def count_book_characters(book_content):
    count_dict = {}
    book_lower = book_content.lower()
    character_set = set(book_lower)
    character_list = list(book_lower)
    # print(character_list)
    for character in character_set:
        count_dict[character] = 0
        for char in character_list:
            if char == character:
                count_dict[character] += 1
    return count_dict

def sort_on(char):
    return char["count"]

def sort_character_dicts(count_dict):
    char_list = []
    for character in count_dict:
        if character.isalpha() == True:
            count = count_dict[character]
            char_dict = {"char": character, "count": count}
            char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list