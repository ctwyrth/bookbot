import sys
from stats import count_words, count_chars, sort_chars
import json

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  # path_to = "books/frankenstein.txt"
  path_to = sys.argv[1]
  book_text = get_text(path_to)
  num_words_in_book = count_words(book_text)
  char_count_in_book = count_chars(book_text)
  sorted_chars_in_book = sort_chars(char_count_in_book)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path_to}...")
  print("----------- Word Count ----------")
  # print(f"{num_words_in_book} words found in the document")
  print(f"Found {num_words_in_book} total words")
  print("--------- Character Count -------")
  
  # print(char_count_in_book)
  # print(json.dumps(char_count_in_book))
  # print(json.dumps(sorted_char_count))

  for key in sorted_chars_in_book:
    if key.isalpha():
      print(f"{key}: {sorted_chars_in_book[key]}")
  
  print("============== END ==============")


def get_text(path):
  with open(path) as book_file:
    book_file_contents = book_file.read()
  
  return book_file_contents

main()

