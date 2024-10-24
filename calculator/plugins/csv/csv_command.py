import logging
import os
import pandas as pd
from calculator.commands import Command

class CsvCommand(Command):
    def __init__(self, command_handler=None):
        self.command_handler = command_handler  # Store the command handler if needed
        
    def execute(self, operation=None, a=None, b=None, result=None):
        """
        Handles reading from and writing to a CSV file for arithmetic operation results.
        First, it saves the operation data to the input CSV, and then it appends the new record directly
        to the output CSV for arithmetic operations.
        """
        # Ensure the 'data' directory exists and is writable
        data_dir = './data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")
        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable.")
            return

        # Define the CSV file paths
        input_csv_file_path = os.path.join(data_dir, 'operations.csv')
        output_csv_file_path = os.path.join(data_dir, 'arithmetic_operations.csv')

        # If the input CSV file exists, read the existing data
        if os.path.exists(input_csv_file_path):
            try:
                # Load existing operations from the input CSV file
                df = pd.read_csv(input_csv_file_path)
                logging.info("Loaded existing CSV file successfully.")
            except Exception as e:
                logging.error(f"Error reading input CSV file: {e}")
                df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        else:
            # Create a new DataFrame if the input file does not exist
            df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

        # Print existing records from the CSV
        print("Existing Arithmetic Operations:")
        print(df)

        # If new operation data is provided, add it to the DataFrame
        if operation and a is not None and b is not None and result is not None:
            new_record = pd.DataFrame({
                'Operation': [operation],
                'Operand1': [a],
                'Operand2': [b],
                'Result': [result]
            })
            
            # Save the operation data to the input CSV file
            df = pd.concat([df, new_record], ignore_index=True)  # Combine the old and new records
            
            try:
                df.to_csv(input_csv_file_path, index=False)
                logging.info(f"Arithmetic operations saved to input CSV at '{input_csv_file_path}'.")
            except Exception as e:
                logging.error(f"Error writing to input CSV file: {e}")

            # Append the new arithmetic operation record to the output CSV file
            if os.path.exists(output_csv_file_path):
                # If the output file exists, append to it
                new_record.to_csv(output_csv_file_path, mode='a', header=False, index=False)
            else:
                # If the output file does not exist, create it with the header
                new_record.to_csv(output_csv_file_path, index=False)
            
            logging.info(f"New arithmetic operation saved to output CSV at '{output_csv_file_path}'.")

        # Provide relative and absolute paths for logging purposes
        absolute_input_path = os.path.abspath(input_csv_file_path)
        absolute_output_path = os.path.abspath(output_csv_file_path)
        logging.info(f"The absolute path to the input file is {absolute_input_path}")
        logging.info(f"The absolute path to the output file is {absolute_output_path}")
