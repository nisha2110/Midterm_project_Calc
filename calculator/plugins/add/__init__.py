# Example for AddCommand class
import logging
from calculator.commands import Command

class AddCommand(Command):
    def __init__(self, command_handler):
        super().__init__()  # Call the superclass constructor if needed
        self.command_handler = command_handler  # Store the command handler for later use

    def execute(self, arg1, arg2):
        result = arg1 + arg2
        logging.info(f"Adding {arg1} + {arg2} = {result}")
        return result


'''class AddCommand(Command):
    def __init__(self, command_handler):
        super().__init__()  # Call the superclass constructor if needed
        self.command_handler = command_handler  # Store the command handler for later use

    def execute(self, arg1, arg2):
        return arg1 + arg2  # Example implementation'''
        
