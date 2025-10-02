"""
    Simple class for pytest examples

"""
class Silly:
    def __init__(self, name):
        self.name = name

    def triple(self, value):
        return value * 3
    
    def normalize(self, value):
        return value.lower().strip()
