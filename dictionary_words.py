import random
import sys
# import timeit

def dictionary_words(number_of_words):
  with open('/usr/share/dict/words', 'r') as f:
    words = f.read().split('\n')
    return ' '.join(random.sample(words, number_of_words)) + '.'
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        number_of_words = int(sys.argv[1])
    else:
        number_of_words = 1

    # def wrapper():
    #     dictionary_words(number_of_words)
    
    # execution_time = timeit.timeit(wrapper, number=1000)

    print(dictionary_words(number_of_words))

    # print(f'Execution time: {execution_time} seconds')