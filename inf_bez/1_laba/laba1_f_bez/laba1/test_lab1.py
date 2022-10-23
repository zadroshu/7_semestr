import unittest
from lab1 import decrypt
from lab1 import crypt
import random


class MyTestCase(unittest.TestCase):

    def test_crypto(self):
        """
        Test that it crypt and decrypt text
        """
        text = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ".lower()
        _text = crypt(text)
        result = decrypt(_text)
        print("Test 1")
        print("======")
        print("original:  " + text)
        print("crypt   :  " + _text)
        print("decrypt :  " + result)
        self.assertEqual(text, result)

    def test_crypto_enhanced(self):
        """
        Test that it enhanced crypt and decrypt text
        """
        text = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ".lower()
        rez = True
        _text = crypt(text)
        d = []
        print("Test 2")
        print("======")
        n=0;
        for i in range(10):
            ind = int(random.random() * len(text))
            if text[ind] == ' ':
                continue
            d.append(ord(text[ind]) - ord(_text[ind]))
            if n > 0 :
                rez = rez and d[n] == d[n - 1]
            n = n + 1
        print(d)
        self.assertTrue(not rez)


if __name__ == '__main__':
    unittest.main()
