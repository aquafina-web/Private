# protected
class user:
    _email = ''

    def __init__(self, email):
        self._email = email

s1 = user('@abcgmail.com')
print(s1._email)
