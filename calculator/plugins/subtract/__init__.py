import logging
from calculator.commands import Command

class SubtractCommand(Command):
    def __init__(self, command_handler):
        super().__init__()
        self.command_handler = command_handler

    def execute(self, arg1, arg2):
        result = arg1 - arg2
        logging.info(f"Subtracting {arg1} - {arg2} = {result}")
        return result