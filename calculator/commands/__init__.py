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

   # Example of EAFP
    def execute_command(self, name, arg1, arg2):
        try:
            # Easier to Ask for Forgiveness than Permission: Attempt to execute directly[EAFP]
            return self.commands[name].execute(arg1, arg2)
        except KeyError:
            # Handle the exception if the command does not exist
            logging.error(f"No such command: '{name}'")
            return f"No such command: '{name}'"
        except ValueError as e:
            # Handle specific error during command execution
            logging.error(f"Error executing command '{name}': {e}")
            return f"Error: {e}"  # Return the error message to the user
        