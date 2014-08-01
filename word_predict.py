import sys

if __name__ == '__main__':
    try: 
        method = sys.argv[1]
    except:
        print "Please add learn or predict trailing with a sentence or a word"

