import unittest
from word_predict import WordPredict

class TestWordPredict(unittest.TestCase):

    def test_learn(self):
        test_object = WordPredict()
        sentence = ['This', 'is', 'a', 'cat']
        test_object.learn(sentence)
        memory = test_object.memory
        self.assertEqual(len(memory), 4)
        keys = memory.keys()
        self.assertEqual(keys[0], 'this')
        self.assertEqual(keys[1], 'a')
        self.assertEqual(keys[2], 'is')
        self.assertEqual(keys[3], 'cat')
        self.assertEqual(len(memory['this']), 1)
        self.assertEqual(len(memory['a']), 1)
        self.assertEqual(len(memory['cat']), 1)

if __name__ == '__main__':
    unittest.main()
