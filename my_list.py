
class List:
    def __init__(self, iteration=None):
        if iteration is None:
            self.length = 0
        else:
            self.length = len(iteration)

    def __len__(self):
        return self.length
