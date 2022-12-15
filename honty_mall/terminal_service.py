from pprint import pprint

class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    # Not used in this case
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    # this should be good
    def read_letter(self, prompt):
        """Gets input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input (as a character).
        """
        return input(prompt).upper()
    
    def read_number(self, prompt):
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

    def write_word(self, array):
        """Displays the given array on the terminal. 
           The entire word would be on the same line

        Args: 
            self (TerminalService): An instance of TerminalService.
            array (array): The array to display.
        """
        print()
        for i in range(len(array)):
            print(f"{array[i]}", end=" ")
        print("\n")