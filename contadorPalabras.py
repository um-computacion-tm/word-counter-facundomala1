

import unittest

def count_words(phrase):

    result = {}

    for word in phrase.split(' '):

        lower_word = word.lower()

        if lower_word in result:

            result[lower_word] += 1

        else:

            result[lower_word] = 1

    return result


class TestCountWords(unittest.TestCase):

    def test_simple(self):

        result = count_words('hola')

        self.assertEqual(result, {'hola': 1})
        
    def test_complex(self):

        result = count_words('Hola como estas hola')

        self.assertEqual(

            result,

            {

                'hola': 2,

                'como': 1,

                'estas': 1,

            },

        )
        
if __name__ == '__main__':

    unittest.main()





