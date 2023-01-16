from unittest import TestCase
from task2 import format_text


class Test(TestCase):
    def test_format_text(self):
        test_text = ('KP2.2-13 - Schema rapolozheniya\n'
                     'KP2.2-10 - Schema rapolozheniya\n'
                     'KP2.2-14 - Schema rapolozheniya\n'
                     'KP2.2-01.1 - Vedomost\'\n'
                     'KP2.2-2 - Schema')
        result = format_text(test_text)
        self.assertEqual(result, ('KP2.2-01.1 - Vedomost\'\n'
                                  'KP2.2-2 - Schema\n'
                                  'KP2.2-10 - Schema rapolozheniya\n'
                                  'KP2.2-13 - Schema rapolozheniya\n'
                                  'KP2.2-14 - Schema rapolozheniya'))

    def test_format_text2(self):
        test_text = ('KP1.2-3 - Schema rapolozheniya\n'
                     'KP2.1-01.3 - Vedomost\'\n'
                     'KP2.2-01.1 - Vedomost\'\n'
                     'KP2.2-10 - Schema\n'
                     'KP2.2-20 - Schema\n'
                     'KP2.2-01.2 - Vedomost\'\n'
                     'KP2.2-2 - Schema')
        result = format_text(test_text)
        self.assertEqual(result, ('KP1.2-3 - Schema rapolozheniya\n'
                                  'KP2.1-01.3 - Vedomost\'\n'
                                  'KP2.2-01.1 - Vedomost\'\n'
                                  'KP2.2-01.2 - Vedomost\'\n'
                                  'KP2.2-2 - Schema\n'
                                  'KP2.2-10 - Schema\n'
                                  'KP2.2-20 - Schema'))
