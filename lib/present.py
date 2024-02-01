class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents

class PasswordChecker:
    def check(self, password):
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")