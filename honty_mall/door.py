from honty_mall.terminal_service import TerminalService

class Door():
    """
    The door class represents one of the doors on the stage. The door may or may not be open or conceal a car!

    self._terminal_service: The service that collects input and prints to the console.
    self._surprise: Boolean representing the presence of a car behind said door.
    self._index: An integer [1,2,3] which represents the door index to the player.
    self._opened: Boolean representing whether the door has been opened or not.
    """

    def __init__(self):
        """
        The Constructor method for the Door class.

        self: The Door class.
        """

        self._terminal_service = TerminalService()
        self._surprise = False
        self._index = 0
        self._opened = False

    def set_as_surprise(self):
        """
        Method that places a car behind the door.

        self: The Door class.
        """
        
        self._surprise = True
    
    def set_index(self, new_index):
        """
        Sets a human-friendly index as a native door attribute.

        self: The Door class.
        new_index: An integer [1,2,3] that represents the index value that makes sense to the player.
        """
        
        self._index = new_index
    
    def check_if_surprise(self):
        """
        Returns a boolean representing the presence of a car to the stage class.

        self: The Door class.
        """
        
        return self._surprise
    
    def check_if_open(self):
        """
        Returns a boolean representing if the door is open.

        self: The Door class.
        """

        return self._opened
    
    def open(self):
        """
        Opens the closed door.

        self: The Door class.
        """
        
        self._opened = True
    
    def present(self):
        """
        Prints the door to the console via the terminal service.

        self: The Door class.
        """
        
        # Print a closed door with it's number
        if self._opened == False:
            self._terminal_service.write_text(f" ___\n| {self._index} |\n|___|")
        
        elif self._opened:
            
            # Print an opened door without a car, possibly ending the game
            if self._surprise == False:
                self._terminal_service.write_text(f"\nxxxxx\nxx{self._index}xx\nxxxxx")
            
            # Print an opened door with a car, ending the game
            elif self._surprise:
                self._terminal_service.write_text(f" ___\n| {self._index} |\n|CAR|\nCongratulations! You won the car!")
