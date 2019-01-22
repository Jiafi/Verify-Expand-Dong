#!/usr/bin/env python

try:
  from PIL import Image
except ImportError:
  import Image
import pytesseract
import argparse

"""verify_expand.py: Will verify if a caption can be made with letters in a picture"""
__author__ = "Jordan Wolinsky"
# Todo add multiple images to check.  Use the return of image to output to create the caption
# If it works

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('files', help="file location", type=str, nargs="+")
  parser.add_argument('caption', help="desired caption", type=str)
  args = parser.parse_args()
  verify_expand(args.files, args.caption)


def verify_expand(files, caption):
  letters = set()
  for f in files:
    letters |= set(pytesseract.image_to_string(Image.open(f), lang='eng').lower())


  print(set(caption.lower()).issubset(letters))

if __name__ == '__main__':
  main()
