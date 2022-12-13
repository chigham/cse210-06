from honty_mall.stage import Stage
from honty_mall.terminal_service import TerminalService

class Director():

    def __init__(self):
        self._stage = Stage()
        self._terminal_service = TerminalService()
        self._chosen_door = False

    def _prompt_to_open(self):
        return input()

    def play_game(self):

        self._stage.present_stage()

        self._chosen_door = self._terminal_service.read_number("Which door do you choose? 1, 2, or 3? ")

        self._stage.open_door(self._chosen_door)

        self._stage.present_stage()