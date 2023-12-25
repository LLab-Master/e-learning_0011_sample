import sample3
import unittest

class TestDiv2(unittest.TestCase):

    def test_sample3(self):
        self.assertEqual(sample3.div2(1.2, 0.6), 2.0)

    def test_sample3_zero(self): #ゼロで割ったらエラーが出ることを確認したい
        with self.assertRaises(ZeroDivisionError): #ここでエラーキャッチ
            sample3.div2(1.2, 0.0) #ゼロで割る処理