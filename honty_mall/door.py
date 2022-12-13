class Door():

    def __init__(self):
        self.surprise = False
        self._index = 0

    def set_as_surprise(self):
        self.surprise = True
    
    def set_index(self, new_index):
        self._index = new_index
    
    def ensure_no_surprise(self):
        self.surprise = False
    
    def present(self):
        print(f" ___\n| {self._index} |\n|___|")
