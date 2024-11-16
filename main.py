# import sys

# def main() -> str:
#   with open('books/frankenstein.txt') as f:
#     file_contents = f.read()
#     print(file_contents)

# if __name__ == '__main__':
#   sys.exit(main())
import json

def main():
  path_to = "books/frankenstein.txt"
  book_text = get_text(path_to)
  num_words_in_book = count_words(book_text)
  char_count_in_book = count_chars(book_text)


def get_text(path):
  with open(path) as book_file:
    book_file_contents = book_file.read()
  
  return book_file_contents

def count_words(text):
  return len(text.split())

def count_chars(text):
  char_dict = {}

  text = text.lower()

  for char in text:
    if char_dict.get(char):
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  
  return char_dict

main()