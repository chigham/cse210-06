from honty_mall.stage import Stage
from honty_mall.terminal_service import TerminalService

class Director():
    """
    The director class guides the game, utilizing the stage and terminal service.

    self._stage: The stage with 3 doors and a hidden car.
    self._terminal_service: The service that collects input and prints to the console.
    self._chosen_door: A number [1,2,3] used to determine the first door selected.
    """

    def __init__(self):
        """
        The Constructor method for the Director class.

        self: The Director class.
        """

        self._stage = Stage()
        self._terminal_service = TerminalService()
        self._chosen_door = False

    def play_game(self):
        """
        The action the director takes to conduct the game.

        The stage is presented.
        The user chooses a door.
        Another empty door is opened.
        The stage is again presented.
        The user is prompted if they want to open the chosen door or switch doors.
        Updated chosen door is opened, possibly revealing the car.
        Game over.

        self: The Director class.
        """

        self._stage.present_stage()

        self._chosen_door = self._terminal_service.read_number("Which door do you choose? 1, 2, or 3? ")

        self._stage.choose_door(self._chosen_door)

        self._stage.present_stage()

        self._stage.make_it_or_break_it(self._chosen_door)

        self._stage.present_stage()

        self._terminal_service.write_text("Game Over")
