# import sys
from stats import count_words, count_chars, sort_chars

# def main() -> str:
#   with open('books/frankenstein.txt') as f:
#     file_contents = f.read()
#     print(file_contents)

# if __name__ == '__main__':
#   sys.exit(main())
import json
# import re

def main():
  path_to = "books/frankenstein.txt"
  book_text = get_text(path_to)
  num_words_in_book = count_words(book_text)
  char_count_in_book = count_chars(book_text)
  sorted_chars_in_book = sort_chars(char_count_in_book)

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
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

# def count_words(text):
#   return len(text.split())

# def count_chars(text):
#   char_dict = {}

#   text = re.sub('[^a-zA-Z]', '', text)
#   text = text.lower()

#   # print(text)

#   for char in text:
#     if char_dict.get(char):
#       char_dict[char] += 1
#     else:
#       char_dict[char] = 1
  
#   return char_dict

main()

