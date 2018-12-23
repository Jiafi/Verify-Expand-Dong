#!/usr/bin/env python

try:
  from PIL import Image
except ImportError:
  import Image
import pytesseract
import argparse

"""verify_expand.py: Will verify if a caption can be made with letters in a picture"""
__author__ = "Jordan Wolinsky"


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('file', help="file location", type=str)
  parser.add_argument('caption', help="desired caption", type=str)
  args = parser.parse_args()
  verify_expand(args.file, args.caption)


def verify_expand(file_name, caption):
  letters = pytesseract.image_to_string(Image.open(file_name), lang='eng')
  print(letters)
  print(is_substring(set(caption.lower()), set(letters.lower())))



def is_substring(substring, string):
  return substring.issubset(string)

if __name__ == '__main__':
  main()
