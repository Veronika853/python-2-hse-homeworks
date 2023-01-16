from unittest import TestCase
from task3 import format_text


class Test(TestCase):
    def test_format_text_20_chars(self):
        test_text = ('I have a theory about British cooking, and I was interested to read that several famous cookery '
                     'writers agree with me. My theory is this. Our basic ingredients, when fresh, '
                     'are so full of flavor that we haven\'t had to invent sauces and complex recipes '
                     'to disguise their natural taste')
        result = format_text(test_text, 20)
        self.assertEqual(result, ('I have a theory\n'
                                  'about British\n'
                                  'cooking, and I was\n'
                                  'interested to read\n'
                                  'that several famous\n'
                                  'cookery writers\n'
                                  'agree with me. My\n'
                                  'theory is this. Our\n'
                                  'basic ingredients,\n'
                                  'when fresh, are so\n'
                                  'full of flavor that\n'
                                  'we haven\'t had to\n'
                                  'invent sauces and\n'
                                  'complex recipes to\n'
                                  'disguise their\n'
                                  'natural taste'))

    def test_format_text_40_chars(self):
        test_text = ('I have a theory about British cooking, and I was interested to read that several famous cookery '
                     'writers agree with me. My theory is this. Our basic ingredients, when fresh, '
                     'are so full of flavor that we haven\'t had to invent sauces and complex recipes '
                     'to disguise their natural taste')
        result = format_text(test_text, 40)
        self.assertEqual(result, ('I have a theory about British cooking,\n'
                                  'and I was interested to read that\n'
                                  'several famous cookery writers agree\n'
                                  'with me. My theory is this. Our basic\n'
                                  'ingredients, when fresh, are so full of\n'
                                  'flavor that we haven\'t had to invent\n'
                                  'sauces and complex recipes to disguise\n'
                                  'their natural taste'))
