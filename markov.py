import random

class MarkovChain(dict):

  def __init__(self, word_list=None):
    super(MarkovChain, self).__init__()
    self.types = 0
    self.tokens = 0
    self.chain(word_list)

  def chain(self, word_list):
    for i, word in enumerate(word_list):
        if word not in self:
            self[word] = {}
            self.types += 1
        if i < len(word_list) - 1:
            next_word = word_list[i+1]
            if next_word not in self[word]:
                self[word][next_word] = 1
            else:
                self[word][next_word] += 1
        self.tokens += 1

  def sample(self, key=None):
    if key is None:
      rand_num = random.randint(1, self.tokens)
      for word in self:
        frequency_of_following_words = sum(self[word].values())
        rand_num -= frequency_of_following_words
        if rand_num <= 0:
          return word
    else:
      word_dict = self[key]
      rand_num = random.randint(1, len(word_dict))
      for next_word in word_dict:
        rand_num -= word_dict[next_word]
        if rand_num <= 0:
          return next_word
        
  def generate_sentence(self):
    sentence = []
    current_word = self.sample()
    while not current_word[0].isupper():
      current_word = self.sample()
    sentence.append(current_word)
    while True:
      next_word = self.sample(current_word)
      if next_word[-1] in '.!?':
        sentence.append(next_word)
        break
      sentence.append(next_word)
      current_word = next_word
    return ' '.join(sentence)
      

if __name__ == '__main__':
    with open('dnd5esrd.txt', 'r') as f:
        text = f.read().replace('\n', ' ')

    words = text.split()
    words = [word.strip() for word in words if word.strip()]
    words = [words[i] + words[i+1] if words[i+1] in [',', '.', '!', '?', ';', ':'] else words[i] for i in range(len(words)-1)]
    words = [word for word in words if word not in [',', '.', '!', '?', ';', ':']]

    markov_chain = MarkovChain(words)

    print("Markov Chain Statistics:")
    print(f"Total types: {markov_chain.types}")
    print(f"Total tokens: {markov_chain.tokens}")

    print("\nSample words:")
    for i in range(5):
        print(markov_chain.sample())

    print("\nSample words following 'dragon':")
    for i in range(5):
        print(markov_chain.sample('dragon'))

    print("\nGenerated sentences:")
    for i in range(3):
        print(markov_chain.generate_sentence())

