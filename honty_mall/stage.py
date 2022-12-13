import random

from honty_mall.door import Door

class Stage():

    def __init__(self):
        self._doors = [Door(), Door(), Door()]
        i = 1
        for door in self._doors:
            door.set_index(i)
            i += 1
        special_door = random.choice(range(3))
        self._doors[special_door].set_as_surprise()
    
    def open_door(self, index):
        self._doors[index - 1].open()

    def present_stage(self):
        for door in self._doors:
            door.present()
