import unittest
import letter


class TestMark(unittest.TestCase):

    def test_mark_A(self):
       for i in range(80,101):
          self.assertEqual(letter.letter_grade(i),"A")

    def test_mark_B(self):
       for i in range(70,80):
          self.assertEqual(letter.letter_grade(i),"B")

    def test_mark_C(self):
       for i in range(60,70):
          self.assertEqual(letter.letter_grade(i),"C")

    def test_mark_D(self):
       for i in range(50,60):
          self.assertEqual(letter.letter_grade(i),"D")

    def test_mark_F(self):
       for i in range(0,50):
          self.assertEqual(letter.letter_grade(i),"F")



if __name__== '__main__':
    unittest.main()
