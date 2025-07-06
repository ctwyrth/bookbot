import sys
import re

def count_words(text):
  return len(text.split())

def count_chars(text):
  char_dict = {}

  # text = re.sub('[^a-zA-Z]', '', text)
  # text = text.lower()

  # print(text)

  for char in text:
    lower_char = char.lower()
    if lower_char in char_dict:
      char_dict[lower_char] += 1
    else:
      char_dict[lower_char] = 1
  
  return char_dict