class Password:
    _value: str

    def __init__(self, value: str):
        self._value = value

    @classmethod
    def of(cls, value: str) -> 'Password':
        return Password(value)

    def __str__(self):
        return self._value

