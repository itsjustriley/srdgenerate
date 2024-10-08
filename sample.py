import histogram
import random

# takes a histogram and returns a single word at random

def random_word(histogram):
    words = list(histogram.keys())
    rand_index = random.randint(0, len(words) - 1)
    return words[rand_index]

def weighted_random_word(histogram):
    total_words = sum(histogram.values())
    rand_num = random.randint(1, total_words)
    for word, count in histogram.items():
        rand_num -= count
        if rand_num <= 0:
            return word
        
def top_ten_words(histogram):
    return sorted(histogram.items(), key=lambda x: x[1], reverse=True)[:10]

if __name__ == '__main__':
    def source_text():
        with open('dnd5esrd.txt', 'r') as f:
            return f.read().replace('\n', ' ')
    
    source_text = source_text()
    histogram = histogram.histogram(source_text)
    print(top_ten_words(histogram))
    print(random_word(histogram))
    print(weighted_random_word(histogram))