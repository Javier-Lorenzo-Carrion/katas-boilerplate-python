from katas.password_validator.errors import PasswordTooShortError


class Password:
    _value: str

    def __init__(self, value: str):
        self._value = value

    @classmethod
    def of(cls, value: str) -> 'Password':
        cls.validate_password_length(value)

        return Password(value)

    @classmethod
    def validate_password_length(cls, value):
        if len(value) < 8:
            raise PasswordTooShortError

    def __str__(self):
        return self._value

