from stats import get_num_words
from stats import get_char_count
from stats import sorted_dict_list
from stats import return_dict_key_name
from stats import return_dict_key_value
import sys


def main():
    if len(sys.argv) == 2:

        bookpath = sys.argv[1]

        print(bookpath)

        word_count = get_num_words(bookpath)
        print("\n============ BOOKBOT ============")
        print(f"\nAnalyzing book found at {bookpath}...")
        print("\n----------- Word Count ----------")
        print(f"\nFound {word_count} total words")
        print("\n--------- Character Count -------\n")

        for element in sorted_dict_list(get_char_count(bookpath)):
            #print(element)
            print(f"{return_dict_key_name(element)}: {return_dict_key_value(element)}")
        print("\n============= END ===============")
    else:

        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)




main()
