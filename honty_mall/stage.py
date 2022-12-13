from honty_mall.door import Door

class Stage():

    def __init__(self):
        self._doors = [Door(), Door(), Door()]
        i = 1
        for door in self._doors:
            door.set_index(i)
            i += 1

    def present_stage(self):
        for door in self._doors:
            door.present()
