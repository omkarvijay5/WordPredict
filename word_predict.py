class WordPredict():

    def learn(self, sentence):
        pass

    def predict(self, word):
        print "i am in predict", word
        pass

if __name__ == '__main__':
    word_predict = WordPredict()
    input_file = open('input.txt')
    for line in input_file.readlines():
        method = line.split()[0].lower()
        sentence = ' '.join(line.strip().split()[1:])
        if method == 'learn':
            learn = getattr(word_predict, method)
            learn(sentence)
        elif method == 'predict':
            predict = getattr(word_predict, method)
            word = ' '.join(line.split()[1:])
            predict(word)

