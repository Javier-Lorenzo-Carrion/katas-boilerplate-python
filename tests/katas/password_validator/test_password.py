from unittest import TestCase

from katas.password_validator.password import Password


class PasswordShould(TestCase):
    def test_be_valid(self):
        password = Password.of("Cul4s$so")

        self.assertEqual(str(password), "Cul4s$so")

