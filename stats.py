import sys
import re

def count_words(text):
  return len(text.split())

def count_chars(text):
  char_dict = {}

  for char in text:
    lower_char = char.lower()
    if lower_char in char_dict:
      char_dict[lower_char] += 1
    else:
      char_dict[lower_char] = 1
  
  return char_dict

def sort_chars(char_count):
  # sorted_char_count = {k: v for k, v in sorted(char_count.items(), key = lambda item: item[1], reverse = True)}
  # def sort_on(items):
  #   return items[1]
  
  sorted_char_count = sorted(char_count.items(), key = lambda item: item[1], reverse = True)
  sorted_char_count = dict(sorted_char_count)

  return sorted_char_count