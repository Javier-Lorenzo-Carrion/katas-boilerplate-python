from unittest import TestCase

from katas.password_validator.errors import PasswordTooShortError
from katas.password_validator.password import Password


class PasswordShould(TestCase):
    def test_be_valid(self):
        password = Password.of("Cul4s$so")

        self.assertEqual(str(password), "Cul4s$so")

    def test_ensure_password_must_contain_at_least_eight_characters(self):
        with self.assertRaises(PasswordTooShortError):
            password = Password.of("Cul4$so")

