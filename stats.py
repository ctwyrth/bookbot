import sys
import re

def count_words(text):
  return len(text.split())

def count_chars(text):
  char_dict = {}

  text = re.sub('[^a-zA-Z]', '', text)
  text = text.lower()

  # print(text)

  for char in text:
    if char_dict.get(char):
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  
  return char_dict