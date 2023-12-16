"""Build a noveltree_yw7 plugin.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the novxlib package.

The novxlib project (see https://github.com/peter88213/novxlib)
must be located on the same directory level as the noveltree_yw7 project. 

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/noveltree_yw7
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../novxlib-Alpha/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}nv_yw7.py'
TARGET_FILE = f'{BUILD}nv_yw7.py'

os.makedirs(BUILD, exist_ok=True)


def main():
    inliner.run(SOURCE_FILE, TARGET_FILE, 'novxlib', '../../novxlib-Alpha/src/')
    print('Done.')


if __name__ == '__main__':
    main()