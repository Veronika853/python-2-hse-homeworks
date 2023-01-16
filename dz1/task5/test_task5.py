from unittest import TestCase
from task5 import find_anagrams


class Test(TestCase):
    def test_find_anagrams(self):
        result = find_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(result, [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']])
