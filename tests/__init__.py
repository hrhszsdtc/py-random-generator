import base64
import hashlib
import hmac
import random
import secrets
import unittest
import uuid

from randgen import (
    gen_random_bytes,
    gen_random_int,
    gen_random_single_digit,
    gen_random_true_or_false,
    gen_random_urlsafe_token,
    gen_rawdata,
)


class TestCode(unittest.TestCase):
    def test_gen_rawdata(self):
        rawdata = gen_rawdata()
        self.assertIsInstance(rawdata, str)
        self.assertEqual(len(rawdata), 64)
        self.assertTrue(all(c in "0123456789abcdef" for c in rawdata))

    def test_gen_random_int(self):
        a = 10
        b = 20
        random_int = gen_random_int(a, b)
        self.assertIsInstance(random_int, int)
        self.assertTrue(a <= random_int <= b)

    def test_gen_random_bytes(self):
        nbytes = 16
        random_bytes = gen_random_bytes(nbytes)
        self.assertIsInstance(random_bytes, bytes)
        self.assertEqual(len(random_bytes), nbytes)

    def test_gen_random_urlsafe_token(self):
        nbytes = 16
        random_token = gen_random_urlsafe_token(nbytes)
        self.assertIsInstance(random_token, str)
        self.assertEqual(len(random_token), (nbytes * 4 + 2) // 3)
        self.assertTrue(
            all(
                c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
                for c in random_token
            )
        )

    def test_gen_random_single_digit(self):
        random_digit = gen_random_single_digit()
        self.assertIsInstance(random_digit, int)
        self.assertTrue(0 <= random_digit <= 9)

    def test_gen_random_true_or_false(self):
        random_bool = gen_random_true_or_false()
        self.assertIsInstance(random_bool, bool)


if __name__ == "__main__":
    unittest.main()
