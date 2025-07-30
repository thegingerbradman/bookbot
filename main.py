def get_book_text(file_path):
    with open(file_path) as file:
        book_content = file.read()
    return book_content

from stats import count_book_words, count_book_characters, sort_character_dicts
def main():
    script_header = "============ BOOKBOT ============"
    wc_header = "----------- Word Count ----------"
    char_header = "--------- Character Count -------"
    footer = "============= END ==============="
    book_content = (get_book_text("./books/frankenstein.txt"))
    word_count = count_book_words(book_content)
    character_count = count_book_characters(book_content)
    sorted_list = sort_character_dicts(character_count)
    print(script_header)
    print("Analyzing book found at books/frankenstein.txt...")
    print(wc_header)
    print(f"Found {word_count} total words")
    print(char_header)
    for char_dict in sorted_list:
        print(f"{char_dict['char']}: {char_dict['count']}")
    print(footer)

main()