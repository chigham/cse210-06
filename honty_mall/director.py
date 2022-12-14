from honty_mall.stage import Stage
from honty_mall.terminal_service import TerminalService

class Director():

    def __init__(self):
        self._stage = Stage()
        self._terminal_service = TerminalService()
        self._chosen_door = False
        self._stay_or_switch = False

    def _make_it_or_break_it(self):
        self._stay_or_switch = self._terminal_service.read_text(f"You chose door {self._chosen_door}. Do you think you chose the correct door, or would you like to switch?\nEnter '{self._chosen_door}' to stick with door #{self._chosen_door}, or 's' to switch doors: ")

    def play_game(self):

        self._stage.present_stage()

        self._chosen_door = self._terminal_service.read_number("Which door do you choose? 1, 2, or 3? ")

        self._stage.choose_door(self._chosen_door)

        self._stage.present_stage()

        self._stage.make_it_or_break_it(self._chosen_door)

        self._stage.present_stage()

