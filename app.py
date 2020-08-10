#!/usr/bin/env python
from __future__ import print_function
import os, sys, shutil, json

def organize_files():
  json_obj = json.loads(open('./config.json').read())
  extensions_and_directories = json_obj['FileTypes']
  path = json_obj['Location']
  items = os.listdir(path)
  for item in items:
    for directory, extensions in extensions_and_directories.iteritems():
      for extension in extensions:
        if extension in item:
          originalfilename = item[:item.index(extension)]
          copyfilename = originalfilename
          copypath = './' + directory + '/' + copyfilename + extension
          appendix = 1
          while os.path.exists(copypath):
            copyfilename = originalfilename + '(' + str(appendix) + ')' + extension
            copypath = './' + directory + '/' + copyfilename
            appendix += 1
          shutil.move(item, copypath)

if __name__ == "__main__":
  organize_files()