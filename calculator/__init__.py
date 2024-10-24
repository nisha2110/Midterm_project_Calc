import os
import pkgutil
import importlib
import sys
from calculator.commands import CommandHandler
from calculator.commands import Command
from dotenv import load_dotenv
import logging
import logging.config
from calculator.plugins.csv.csv_command import CsvCommand

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        # Instantiate CommandHandler internally
        self.command_handler = CommandHandler()
        
    
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'calculator.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    logging.info(f"Loading plugin '{plugin_name}'..")
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            logging.debug(f"Checking item: {item_name} -> {item}")  # Debug output for each item

            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                command_name = item_name.lower().replace('command', '')
            
            # Instantiate the command with self.command_handler
                self.command_handler.register_command(command_name, item(self.command_handler))
                logging.info(f"Command '{command_name}' from plugin '{plugin_name}' registered.")

            

    def print_available_commands(self):
        available_commands = self.command_handler.get_registered_commands()
        # This will print the list of available commands
        if available_commands:
            logging.info(f"Available commands: {available_commands}")
             #print("Available commands:", available_commands)
        
    def start(self):
        # Register commands here
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        print("Type 'exit' to exit.")
        logging.info("Type 'menu' to see all available commands.")
        
        # Load existing data from the CSV file
        csv_command = CsvCommand(self.command_handler)  # Pass command handler if needed
        csv_command.execute()  # This will print existing operations

        while True:  # REPL: Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip().lower()
            if user_input == 'exit':
                logging.info("Application exit. Goodbye!")
                raise SystemExit("Exiting...")
            elif user_input == 'menu':
                self.print_available_commands()
            elif user_input == 'csv':
                 csv_command.execute()  # Print existing operations again if requested by the user
                
            else:
                parts = user_input.split()
                command_name = parts[0]
                
                # Check if command is valid
                if command_name not in self.command_handler.commands:
                    logging.error(f"No such command: {command_name}")
                    continue
                
                # Ensure correct number of arguments (2 numbers expected for math commands)
                if len(parts) != 3:
                    logging.error(f"'{command_name}' requires two numeric arguments.")
                    continue
                
                # Check if the arguments are valid numbers
                try:
                    arg1, arg2 = float(parts[1]), float(parts[2])
                except ValueError:
                    logging.error("Both arguments must be numbers.")
                    continue

                # Execute the command if arguments are valid
                result = self.command_handler.execute_command(command_name, arg1, arg2)
                
                if result is not None:
                    # Log and display the result
                    logging.info(f"Result: {result}")
                    print(f"Result: {result}")

                    # Store the result in the CSV file
                    CsvCommand().execute(operation=command_name, a=arg1, b=arg2, result=result)
                    

