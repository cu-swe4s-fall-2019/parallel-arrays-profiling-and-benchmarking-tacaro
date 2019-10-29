import unittest
import random
import hash_functions as hf


class Test_Hash_Functions(unittest.TestCase):
    def test_h_ascii_basic(self):
        self.assertEqual(hf.h_ascii('test', 500), 447)

    def test_h_ascii_small_array(self):
        self.assertEqual(hf.h_ascii('test', 25), 24)

    def test_h_ascii_empty_string(self):
        with self.assertRaises(ValueError):
            hf.h_ascii('', random.randint(1, 100))

    def test_h_ascii_bad_array(self):
        with self.assertRaises(ValueError):
            hf.h_ascii('test', random.randint(0, -100))

    def test_h_ascii_none_string(self):
        with self.assertRaises(ValueError):
            hf.h_ascii(None, random.randint(1, 100))

    def test_h_ascii_integer(self):
        self.assertEqual(hf.h_ascii('13', 200), 99)

    def test_h_rolling_basic(self):
        self.assertEqual(hf.h_rolling('test', 500), 238)

    def test_h_rolling_small_array(self):
        self.assertEqual(hf.h_rolling('test', 25), 13)

    def test_h_rolling_empty_string(self):
        with self.assertRaises(ValueError):
            hf.h_rolling('', random.randint(1, 100))

    def test_h_rolling_bad_array(self):
        with self.assertRaises(ValueError):
            hf.h_rolling('test', random.randint(0, -100))

    def test_h_rolling_none_string(self):
        with self.assertRaises(ValueError):
            hf.h_rolling(None, random.randint(1, 100))

    def test_h_rolling_integer(self):
        self.assertEqual(hf.h_rolling('13', 100), 30)

    def test_fletcher64_basic(self):
        self.assertEqual(hf.h_fletcher64('a'), 416611827809)

    def test_fletcher64_basic2(self):
        self.assertEqual(hf.h_fletcher64('fletcher_test'), 41210211206508)

    def test_fletcher64__empty_string(self):
        with self.assertRaises(ValueError):
            hf.h_fletcher64('')

    def test_h_rolling_none_string(self):
        with self.assertRaises(ValueError):
            hf.h_fletcher64(None)

    def test_h_rolling_integer(self):
        self.assertEqual(hf.h_fletcher64('13'), 639950127204)


if __name__ == '__main__':
    unittest.main()
