class WordPredict():

    def __init__(self):
        self.memory = {}
    
    def get_next_word(self, sentence, word):
        next_word_index = sentence.index(word) + 1
        next_word = sentence[next_word_index]
        return next_word

    def learn(self, sentence):
        for word in sentence:
            next_word = slef.get_next_word(sentence, word)

    def predict(self, word):
        pass

if __name__ == '__main__':
    word_predict = WordPredict()
    input_file = open('input.txt')
    for line in input_file.readlines():
        method = line.split()[0].lower()
        sentence = line.strip().split()[1:]
        if method == 'learn':
            learn = getattr(word_predict, method)
            learn(sentence)
        elif method == 'predict':
            predict = getattr(word_predict, method)
            word = ' '.join(line.split()[1:])
            predict(word)

