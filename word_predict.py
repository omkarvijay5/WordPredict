class WordPredict():

    def __init__(self):
        self.memory = {}
    
    def get_next_word(self, sentence, word):
        next_word_index = sentence.index(word) + 1
        if len(sentence) == next_word_index:
            next_word = None
        else:
            next_word = sentence[next_word_index]
        return next_word

    def learn(self, sentence):
        temp_sentence = [w.lower() for w in sentence]
        for word in temp_sentence:
            temp_word = word.lower()
            if temp_word in self.memory:
                next_word = self.get_next_word(temp_sentence, temp_word)
                if next_word in self.memory[temp_word].keys():
                    self.memory[temp_word][next_word] += 1
                else:
                    self.memory[temp_word][next_word] = 1
            else:
                next_word = self.get_next_word(temp_sentence, temp_word)
                self.memory[temp_word] = {next_word: 1}
        print "learned a new sentence"

    def predict(self, word):
        temp_word = word.lower()
        dictionary = self.memory[temp_word]
        next_word = max(dictionary)
        if next_word == None:
            next_word = ''
        print "{0} : {1}".format(word, next_word)

if __name__ == '__main__':
    word_predict = WordPredict()
    input_file = open('input.txt')
    for line in input_file.readlines():
        method = line.split()[0].lower()
        sentence = line.split()[1:]
        if method == 'learn':
            learn = getattr(word_predict, method)
            learn(sentence)
        elif method == 'predict':
            predict = getattr(word_predict, method)
            word = ' '.join(line.split()[1:])
            predict(word)
