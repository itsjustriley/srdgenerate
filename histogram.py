from collections import Counter

def histogram(source_text):
    words = source_text.split()
    words = [word.strip('.,?!()[]{}"') for word in words]
    words = [word for word in words if word.isalpha()]
    words = [word for word in words if len(word) > 0]
    return Counter(words)

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]

if __name__ == '__main__':
    def source_text():
        with open('dnd5esrd.txt', 'r') as f:
            return f.read().replace('\n', ' ')
        
    source_text = source_text()

    histogram = histogram(source_text)


    # print("Histogram:")
    # print({k: histogram[k] for k in list(histogram)[:5]})

    print("Unique words:")
    print(unique_words(histogram))

    print("Frequency of 'the':")
    print(frequency('the', histogram))

    print("Frequency of 'dragon':")
    print(frequency('dragon', histogram))

    print("Frequency of 'sword':")
    print(frequency('sword', histogram))

