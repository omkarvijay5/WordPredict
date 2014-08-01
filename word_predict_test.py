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
        self.assertEqual(memory['this']['is'], 1)
        self.assertEqual(memory['a']['cat'], 1)
        self.assertEqual(memory['is']['a'], 1)
        self.assertEqual(memory['cat'][None], 1)
        sentence = ['This', 'was', 'on', 'the', 'table']
        test_object.learn(sentence)
        memory = test_object.memory
        self.assertEqual(len(memory), 8)
        self.assertEqual(len(memory['a']), 1)
        self.assertEqual(len(memory['on']), 1)
        self.assertEqual(len(memory['this']), 2)
        self.assertEqual(len(memory['is']), 1)
        self.assertEqual(len(memory['cat']), 1)
        self.assertEqual(len(memory['table']), 1)
        self.assertEqual(len(memory['the']), 1)
        self.assertEqual(len(memory['was']), 1)
        self.assertEqual(memory['a']['cat'], 1)
        self.assertEqual(memory['on']['the'], 1)
        self.assertEqual(memory['this']['is'], 1)
        self.assertEqual(memory['this']['was'], 1)
        self.assertEqual(memory['cat'][None], 1)
        self.assertEqual(memory['table'][None], 1)
        self.assertEqual(memory['the']['table'], 1)
        self.assertEqual(memory['was']['on'], 1)



if __name__ == '__main__':
    unittest.main()
