
import sys
from calculator.commands import Command

class ExitCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler
    
    def execute(self):
        sys.exit("Exiting...")
