#!/usr/bin/env python

import os
import os.path
import sys
import subprocess

OUTPUT_DIR = '/Users/matt/Desktop/mp3/'
#OUTPUT_DIR = '/home/faheem/test/'

def convert_and_save(path):
    filenames = [
        filename
        for filename
        in os.listdir(path)
        if filename.endswith('.m4a')
        ]

    for filename in filenames:
        source = os.path.join(path, filename)
        destination = os.path.join(OUTPUT_DIR, '%s.mp3' % filename[:-4])

        subprocess.call([
            "ffmpeg", "-i",
            source,
            "-acodec", "libmp3lame", "-ab", "256k",
            destination
            ])

def flat_file(text_file):
    for path in text_file:
        convert_and_save(path.strip('\n'))

    return 0

def main():
    path = os.getcwd()
    convert_and_save(path)    

    return 0

if __name__ == '__main__':
    #f = open('/home/faheem/dirs.txt', 'r')
    #status = flat_file(f)
    #sys.exit(status)
    #f.close()

    status = main()
    sys.exit(status)