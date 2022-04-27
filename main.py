# Write a script to run the 3 python files in order with arguments
import sys
import os
import subprocess

def main():

    args = sys.argv[1:]

    subprocess.call(['python3', 'fetch_and_clean.py'] + args)

    subprocess.call(["python3", "data_preprocess.py"])

    subprocess.call(["python3", "content_processor.py"])

    subprocess.call(["python3", "NLP.py"])

if __name__ == '__main__':
    main()