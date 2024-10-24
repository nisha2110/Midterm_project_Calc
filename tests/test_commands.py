import pytest
from calculator import App
from calculator.plugins.add import AddCommand
from calculator.plugins.subtract import SubtractCommand
from calculator.plugins.multiply import MultiplyCommand
from calculator.plugins.divide import DivideCommand
from calculator.plugins.menu import MenuCommand
from calculator.plugins.exit import ExitCommand
from calculator.commands import CommandHandler
from calculator.commands import Command

# Mock command class to use for testing
class MockCommand(Command):
    def execute(self, *args):
        return sum(args)


def test_register_command():
    handler = CommandHandler()
    command = MockCommand()
    handler.register_command('add', command)

    assert 'add' in handler.commands
    assert handler.commands['add'] == command
def test_mock_command():
    # Create an instance of MockCommand
    mock_command = MockCommand()
    
    # Test the execute method with sample inputs
    result = mock_command.execute(1, 2, 3)
    
    # Verify that the sum of the inputs is returned
    assert result == 6, "The MockCommand should return the sum of the arguments"
    

'''
def test_execute_command_valid():
    handler = CommandHandler()
    command = MockCommand()
    handler.register_command('add', command)

    result = handler.execute_command('add', 1, 2, 3)
    assert result == 6  # 1 + 2 + 3


def test_execute_command_invalid():
    handler = CommandHandler()
    
    result = handler.execute_command('invalid_command', 1, 2)
    assert result == "No such command: 'invalid_command'"


def test_get_registered_commands():
    handler = CommandHandler()
    command1 = MockCommand()
    command2 = MockCommand()

    handler.register_command('add', command1)
    handler.register_command('subtract', command2)

    registered_commands = handler.get_registered_commands()
    assert sorted(registered_commands) == ['add', 'subtract']'''
# Test for Add Command
def test_add_command(capfd):
    command_handler = CommandHandler()
    command = AddCommand(command_handler)
    result = command.execute(5, 3)
    assert result == 8, " correctly add two numbers"

# Test for Subtract Command
def test_subtract_command(capfd):
    command_handler = CommandHandler()
    command = SubtractCommand(command_handler)
    result = command.execute(10, 4)
    assert result == 6, " correctly subtract two numbers"

# Test for Multiply Command
def test_multiply_command(capfd):
    command_handler = CommandHandler()
    command = MultiplyCommand(command_handler)
    result = command.execute(6, 7)
    assert result == 42, " correctly multiply two numbers"

# Test for Divide Command
def test_divide_command(capfd):
    command_handler = CommandHandler()
    command = DivideCommand(command_handler)
    result = command.execute(8, 2)
    assert result == 4, "correctly divide two numbers"

# Test for Division by Zero
def test_divide_by_zero_command(capfd):
    command_handler = CommandHandler()
    command = DivideCommand(command_handler)
    
    # Use pytest to check if the appropriate exception is raised
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(9, 0)
 
# Test for Menu Command
def test_menu_command():
    # Simulate a command handler with registered commands
    command_handler = CommandHandler()
    
    # Register plugins/commands
    
    
    
    # Create the MenuCommand with the registered commands
    command = MenuCommand(command_handler)
    
    # Execute the menu command and get the result
    result = command.execute()

    
def test_exit_command():
    command_handler = CommandHandler()
    command = ExitCommand(command_handler)
    with pytest.raises(SystemExit) as excinfo:
        command.execute()
    assert str(excinfo.value) == "Exiting..."  
 
  