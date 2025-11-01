import unittest
import letter


class TestMark(unittest.TestCase):

    def test_mark_A(self):
        result = letter.letter_grade(80)
        self.assertEqual(result,"A")
        

