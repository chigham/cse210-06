import random

from honty_mall.door import Door
from honty_mall.terminal_service import TerminalService

class Stage():
    """
    The stage class presents 3 doors and contains actions performed under the direction of the director. Utilizes three doors and terminal service.

    self._terminal_service: The service that collects input and prints to the console.
    self._doors: A list containing 3 doors.
    self._chosen_door: A number [1,2,3] used to determine the first door selected.
    self._stay_or_switch: Input from the user ('s' or a number [1,2,3]) containing their second decision.
    self._remaining_doors: (comes later) A list containing the two doors that were not selected in the first decision.
    """

    def __init__(self):
        """
        The Constructor method for the Stage class.

        self: The Stage class.
        """

        self._terminal_service = TerminalService()
        self._doors = [Door(), Door(), Door()]
        self._stay_or_switch = False
        
        # Set indeces for the doors that makes sense to the player [1,2,3]
        i = 1
        for door in self._doors:
            door.set_index(i)
            i += 1
        
        # Place a car behind one of the doors
        special_door = random.choice(range(3))
        self._doors[special_door].set_as_surprise()

    def present_stage(self):
        """
        Calls all doors to show themselves to the player

        self: The Stage class.
        """

        for door in self._doors:
            door.present()
    
    def choose_door(self, index):
        """
        Chooses a door not to open yet. Opens another door that does not reveal the car.

        self: The Stage class.
        index: An integer [1,2,3] that the player selected to represent their chosen door.
        """
        
        # Set self._remaining_doors to be the two doors that were not chosen
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
    
    def make_it_or_break_it(self, index):
        """
        The action that determines the second and final choice of the player: should they open the door they chose or switch to open the other remaining closed door? Possible answers are an integer [1,2,3] that matches their chosen door, or the letter 's' to represent 'switch'.

        self: The Stage class.
        index: The integer [1,2,3] player-friendly index that represents their first chosen door, which is still closed.
        """
        
        self._stay_or_switch = self._terminal_service.to_switch_or_not_to_switch(f"You chose door {index}. Do you think you chose the correct door, or would you like to switch?\nEnter '{index}' to stick with door #{index}, or 's' to switch doors: ", index)
        
        # If they chose to stay with the same door, open it
        if self._stay_or_switch == str(index):
            self._doors[index - 1].open()
        
        # Otherwise, if they chose to switch to the other closed door,
        # find the other closed door and open that one
        elif self._stay_or_switch.lower() == 's':
            if self._remaining_doors[0].check_if_open():
                self._remaining_doors[1].open()
            elif self._remaining_doors[1].check_if_open():
                self._remaining_doors[0].open()
