from unittest import TestCase
from task4 import format_text


class Test(TestCase):
    def test_format_text(self):
        test_text = ('She married a very nice young architect from Belfast, whom she met on a bus. '
                     'I don\'t know when the decision was made. If I had gone to university '
                     'I would have studied medicine.')
        result = format_text(test_text)
        self.assertEqual(result, ('i,3\n'
                                  'she,2\n'
                                  'a,2\n'
                                  'young,1\n'
                                  'would,1\n'
                                  'whom,1\n'
                                  'when,1\n'
                                  'was,1\n'
                                  'very,1\n'
                                  'university,1'))
