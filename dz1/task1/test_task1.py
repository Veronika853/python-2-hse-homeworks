import unittest
from task1 import format_text


class MyTestCase(unittest.TestCase):
    def test_format_text(self):
        test_text = ('1. Николаев Михаил: 7\n'
                     '2. Кленков Андрей: 4\n'
                     '3. Николаев Станислав: 2')
        result = format_text(test_text)
        self.assertEqual(result, ('name,grade\n'
                                  'Кленков Андрей,4\n'
                                  'Николаев Михаил,7\n'
                                  'Николаев Станислав,2'))
