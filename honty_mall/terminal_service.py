from pprint import pprint

class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    
    def read_number(self, prompt):
        """
        Handle user input for the first decision - which door would you like to choose?

        self: The TerminalService class.
        prompt: The text prompting for input.
        """
        
        result = ""
        while type(result) != int or result not in [1, 2, 3]:
            result = input(prompt)
            try:
                result = int(result)
                if result not in [1, 2, 3]:
                    print(2 + "no") #fails, forces except
            except:
                print("pick an appropriate number")
        return result
    
    def to_switch_or_not_to_switch(self, prompt, index):
        """
        Handle user input for the second decision - stay with the same door or switch to the other open door?

        self: The TerminalService class.
        prompt: The text prompting for input.
        index: The integer [1,2,3] representing the door's index number to the player.
        """
        
        result = ""
        while result not in ['s', str(index)]:
            result = input(prompt)
            if result.lower() == 's' or result == str(index):
                return result
            else:
                print(f"Pick an appropriate response ['s' or '{index}']")


    # Not used in this case
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)
