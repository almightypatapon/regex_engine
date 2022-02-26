import unittest
import regex


class MyTestCase(unittest.TestCase):
    def test_stage_1(self):
        self.assertTrue(regex.compare_str('a', 'a'))
        self.assertTrue(regex.compare_str('.', 'a'))
        self.assertTrue(regex.compare_str('', 'a'))
        self.assertTrue(regex.compare_str('', ''))
        self.assertFalse(regex.compare_str('a', ''))

    def test_stage_2(self):
        self.assertTrue(regex.compare_str('apple', 'apple'))
        self.assertTrue(regex.compare_str('.pple', 'apple'))
        self.assertTrue(regex.compare_str('appl.', 'apple'))
        self.assertTrue(regex.compare_str('.....', 'apple'))
        self.assertFalse(regex.compare_str('peach', 'apple'))

    def test_stage_3(self):
        self.assertTrue(regex.compare_str('apple', 'apple'))
        self.assertTrue(regex.compare_str('ap', 'apple'))
        self.assertTrue(regex.compare_str('le', 'apple'))
        self.assertTrue(regex.compare_str('a', 'apple'))
        self.assertTrue(regex.compare_str('.', 'apple'))
        self.assertFalse(regex.compare_str('apwle', 'apple'))
        self.assertFalse(regex.compare_str('peach', 'apple'))

    def test_stage_4(self):
        self.assertTrue(regex.compare_str('^app', 'apple'))
        self.assertTrue(regex.compare_str('le$', 'apple'))
        self.assertTrue(regex.compare_str('^a', 'apple'))
        self.assertTrue(regex.compare_str('.$', 'apple'))
        self.assertTrue(regex.compare_str('apple$', 'tasty apple'))
        self.assertTrue(regex.compare_str('^apple', 'apple pie'))
        self.assertTrue(regex.compare_str('^apple$', 'apple'))
        self.assertFalse(regex.compare_str('^apple$', 'tasty apple'))
        self.assertFalse(regex.compare_str('^apple$', 'apple pie'))
        self.assertFalse(regex.compare_str('^app$', 'apple'))
        self.assertFalse(regex.compare_str('^le', 'apple'))

    def test_stage_5(self):
        self.assertTrue(regex.compare_str('colou?r', 'color'))
        self.assertTrue(regex.compare_str('colou?r', 'colour'))
        self.assertFalse(regex.compare_str('colou?r', 'colouur'))
        self.assertTrue(regex.compare_str('colou*r', 'color'))
        self.assertTrue(regex.compare_str('colou*r', 'colour'))
        self.assertTrue(regex.compare_str('colou*r', 'colouur'))
        self.assertTrue(regex.compare_str('col.*r', 'color'))
        self.assertTrue(regex.compare_str('col.*r', 'colour'))
        self.assertTrue(regex.compare_str('col.*r', 'colr'))
        self.assertTrue(regex.compare_str('col.*r', 'collar'))
        self.assertFalse(regex.compare_str('col.*r$', 'colors'))

    def test_stage_6(self):
        self.assertTrue(regex.compare_str('\\.$', 'end.'))
        self.assertTrue(regex.compare_str('3\\+3', '3+3=6'))
        self.assertTrue(regex.compare_str('\\?', 'Is this working?'))
        self.assertTrue(regex.compare_str('\\\\', '\\'))
        self.assertFalse(regex.compare_str('colou\\?r', 'color'))
        self.assertFalse(regex.compare_str('colou\\?r', 'colour'))


if __name__ == '__main__':
    unittest.main()
