

import unittest

def count_letters(word):

    result = {}

    for letter in word:

        if letter in result:

            result[letter] += 1

        else:

            result[letter] = 1

    return result

class TestCountLetters(unittest.TestCase):

    def test_simple(self):

        result = count_letters('a')

        self.assertEqual(result, {'a': 1})

    def test_complex(self):

        result = count_letters('hola')

        self.assertEqual(

            result,

            {

                'h': 1,

                'o': 1,

                'l': 1,

                'a': 1,
            }

        )

    def test_super_complex(self):

        result = count_letters('hola chau')

        self.assertEqual(

            result,

            {

                'h': 2,

                'o': 1,

                'l': 1,

                'a': 2,

                ' ': 1,

                'c': 1,

                'u': 1

            }
        )
    def test_case_sensitive(self):
        result = count_letters('Hello World')
        self.assertEqual(result, {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1})


if __name__ == '__main__':

    unittest.main()

