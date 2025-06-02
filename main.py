from stats import get_word_number_count, get_character_number_count, sort_dict
import sys

def main():
    if (len(sys.argv)!=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_word_number_count(path_to_file)} total words")
    print(f"--------- Character Count -------")
    temp_dict=sort_dict(get_character_number_count(path_to_file))
    for temp in temp_dict:
        if (temp["character"].isalpha()):
            print(f"{temp["character"]}: {temp["num"]}")
main()
