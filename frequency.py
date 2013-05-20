#
# test code for finding the frequency 
# of a word in a text file
# 
# python 2.7.4

import sys

def frequency(fp):
    # read in the file
    filestrings = fp.readlines()
    WordsDict = {}

    #
    # loop over the lines in the file 

    count = 0
    for lines in filestrings:
        try:
            tokens = lines.split()
#
#           loop over the words to get a score
#           if the word is not in the dictionary
#           add it to the newWordsList
            for word in tokens:
                try:
                    WordsDict[word] = WordsDict[word] + 1
                except:
                    WordsDict[word] = 1
            count = count + 1
        except:
            pass

    return WordsDict

def main():
    textfile = open(sys.argv[1])
    Words = {}
    Words = frequency(textfile)
    for key in Words.keys():
        print key,'-', Words[key]

if __name__ == '__main__':
    main()
