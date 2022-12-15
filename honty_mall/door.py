class Door():

    def __init__(self):
        self._surprise = False
        self._index = 0
        self._opened = False

    def set_as_surprise(self):
        self._surprise = True
    
    def set_index(self, new_index):
        self._index = new_index
    
    def ensure_no_surprise(self):
        self._surprise = False
    
    def check_if_surprise(self):
        return self._surprise
    
    def check_if_open(self):
        return self._opened
    
    def open(self):
        self._opened = True
    
    def present(self):
        if self._opened == False:
            print(f" ___\n| {self._index} |\n|___|")
        elif self._opened:
            if self._surprise == False:
                print(f"\nxxxxx\nxx{self._index}xx\nxxxxx")
            elif self._surprise:
                print(f" ___\n| {self._index} |\n|CAR|\nCongratulations! You won the car!")
