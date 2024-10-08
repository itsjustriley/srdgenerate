import random

def rearrange_words(words):
    random.shuffle(words)
    return ' '.join(words)

if __name__ == '__main__':
    import sys
    words = sys.argv[1:]
    print(rearrange_words(words))