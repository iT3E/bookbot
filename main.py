import sys
from stats import get_num_words, get_num_chars, sort_on, trans_dict, lom_to_string


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        raise sys.exit(1)
    book_filepath = sys.argv[1]
    word_count = get_num_words(get_book_text(book_filepath))
    char_count = get_num_chars(get_book_text(book_filepath))
    # sorted_count = get_sorted_list("testing one two three")
    # test_dict = {"a": 1, "b": 2, "c": 3}
    trans = trans_dict(char_count)
    trans.sort(key=sort_on, reverse=True)
    trans_to_string = lom_to_string(trans)
    # sort = sort_on(trans)
    # sorted_count = get_sorted_list(test_dict)

    print(
        f"""
============ BOOKBOT ============
Analyzing book found at {book_filepath}
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{trans_to_string}
"""
    )


main()
