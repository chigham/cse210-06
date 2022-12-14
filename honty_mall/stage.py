import random

from honty_mall.door import Door
from honty_mall.terminal_service import TerminalService

class Stage():

    def __init__(self):
        self._terminal_service = TerminalService()
        self._doors = [Door(), Door(), Door()]
        i = 1
        for door in self._doors:
            door.set_index(i)
            i += 1
        special_door = random.choice(range(3))
        self._doors[special_door].set_as_surprise()
        self._stay_or_switch = False
    
    def make_it_or_break_it(self, index):
        self._stay_or_switch = self._terminal_service.to_switch_or_not_to_switch(f"You chose door {index}. Do you think you chose the correct door, or would you like to switch?\nEnter '{index}' to stick with door #{index}, or 's' to switch doors: ", index)
        
        if self._stay_or_switch == index:
            self._doors[index - 1].open()
        elif self._stay_or_switch.lower() == 's':
            # look at remaining doors for open == False
            if self._remaining_doors[0].check_if_open():
                # open that door
                self._remaining_doors[1].open()
            elif self._remaining_doors[1].check_if_open():
                self._remaining_doors[0].open()

    def choose_door(self, index):
        
        self._remaining_doors = self._doors[:index - 1] + self._doors[index:]
        # choose one of the other doors
        door_to_maybe_open = random.choice(self._remaining_doors)
        # check to see if the car is behind that door
        if door_to_maybe_open.check_if_surprise():
        # if so, choose the other door and open it
            list(set(self._remaining_doors) - set([door_to_maybe_open]))[0].open()
        # if not, open the door
        elif door_to_maybe_open.check_if_surprise() == False:
            door_to_maybe_open.open()

    def present_stage(self):
        for door in self._doors:
            door.present()
