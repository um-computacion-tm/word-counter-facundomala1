

import unittest


def count_words(word):
    word_list = word.split()
    result = {}
    for w in word_list:
        if w in result:
            result[w] += 1
        else:
            result[w] = 1
    return result

class TestCountLetters(unittest.TestCase):

    def test_simple(self):

        result = count_words('hola')

        self.assertEqual(result, {'hola': 1})

if __name__ == '__main__':

    unittest.main()

