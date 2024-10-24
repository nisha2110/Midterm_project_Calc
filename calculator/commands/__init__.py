import logging
from abc import ABC, abstractmethod

# Base abstract Command class
class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

# CommandHandler class to manage command registration and execution
class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command
        logging.info(f"Command '{name}' has been registered.")
    
    # Method to return a list of registered commands
    def get_registered_commands(self):
        return f"{list(self.commands.keys())}"   # Return the list of command names

    def execute_command(self, name, arg1, arg2):
        # Check if the command is registered (Look Before You Leap - LBYL)
        if name in self.commands:
            try:
                # Attempt to execute the command
                return self.commands[name].execute(arg1, arg2)
            except ValueError as e:
                logging.error(f"Error executing command '{name}': {e}")
                return f"Error: {e}"  # Return the error message to the user
        else:
            logging.error(f"No such command: '{name}'")
            return f"No such command: '{name}'"


