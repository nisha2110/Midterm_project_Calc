import pandas as pd
import os
import logging

class CalculationHistory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
            cls._instance.history = pd.DataFrame(columns=['Operation', 'Arg1', 'Arg2', 'Result'])
        return cls._instance

    def load_history(self):
        """Load history from the CSV file if it exists."""
        if os.path.exists("./data/arithmetic_operations.csv"):
            self.history = pd.read_csv("./data/arithmetic_operations.csv")
            logging.info("History loaded from file.")
        else:
            logging.info("No history file to load.")

    def save_history(self):
        """Save the in-memory history to the CSV file."""
        self.history.to_csv("./data/arithmetic_operations.csv", index=False)
        logging.info("History saved to file.")

    def add_record(self, operation, arg1, arg2, result):
        """Add a new record to the in-memory history."""
        new_record = pd.DataFrame([[operation, arg1, arg2, result]], columns=['Operation', 'Arg1', 'Arg2', 'Result'])
        self.history = pd.concat([self.history, new_record], ignore_index=True)

    def print_history(self):
        """Print the in-memory history."""
        print(self.history)

    def clear_history(self):
        """Clear the in-memory history and the CSV file contents."""
        # Clear the in-memory history
        self.history = pd.DataFrame(columns=['Operation', 'Arg1', 'Arg2', 'Result'])
        
        # Clear the content of the CSV file by overwriting it with an empty DataFrame
        if os.path.exists("arithmetic_operations.csv"):
            self.history.to_csv("./data/arithmetic_operations.csv", index=False)
            print("History cleared from memory and file.")
            

    def delete_history_file(self):
        """Deletes the history file if it exists."""
    file_path = "./data/arithmetic_operations.csv"
    if os.path.exists(file_path):
        os.remove(file_path)
        print("History file deleted.")
    else:
        print("No history file to delete.")

    