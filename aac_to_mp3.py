#!/usr/bin/env python

import os
import os.path
import sys
import subprocess

#OUTPUT_DIR = '/Users/matt/Desktop/mp3/'
OUTPUT_DIR = 'c:/test/'

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
            destination)
            ])

def flat_file(text_file):
    for dir in text_file:
        convert_and_save(dir)

    return 0

def main():
    path = os.getcwd()
    convert_and_save(path)    

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)