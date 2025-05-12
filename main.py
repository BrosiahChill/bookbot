from stats import get_book_text, number_of_words, chars_in_book_text, sorted_dictionary
import sys

def main():
    if len(sys.argv) == 2:
        book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(book)
    num_words = number_of_words(book_text)
    character_count = chars_in_book_text(book_text)
    dict_sorted = sorted_dictionary(character_count)
    print("=============== BOOKBOT =================")
    print(f"Analyzing book found at {book}...")
    print("--------------- Word Count --------------")
    print(f"Found {num_words} total words")
    print("------------ Character Count ------------")
    for d in dict_sorted:
        for k, v in d.items():
            print(f"{k}: {v}")

    print("================ END ====================")
        

main()