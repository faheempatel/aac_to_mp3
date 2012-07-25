#!/usr/bin/env python

import os
import os.path
import sys
import subprocess

OUTPUT_DIR = '/Users/matt/Desktop/mp3/'

def main():
    path = os.getcwd()
    filenames = [
        filename
        for filename
        in os.listdir(path)
        if filename.endswith('.m4a')
        ]

    for filename in filenames:
        subprocess.call([
            "ffmpeg", "-i",
            os.path.join(path, filename),
            "-acodec", "libmp3lame", "-ab", "256k",
            os.path.join(OUTPUT_DIR, '%s.mp3' % filename[:-4])
            ])
    
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)