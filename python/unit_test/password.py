import unittest

def is_valid_password(pwd):
    return len(pwd) >= 8

class TestPassword(unittest.TestCase):
    def test_passwords(self):
        passwords = [
            ("password123", True),
            ("abc", False),
            ("welcome12", True),
            ("12345", False)
        ]

        for pwd, expected in passwords:
            with self.subTest(password=pwd):
                self.assertEqual(is_valid_password(pwd), expected)

unittest.main()