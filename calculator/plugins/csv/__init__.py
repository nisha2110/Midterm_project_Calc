# calculator/plugins/csv/__init__.py

# Optionally import the CsvCommand to make it accessible when importing the csv module
from .csv_command import CsvCommand

# You can also include any package-level documentation or variables if needed
__all__ = ['CsvCommand']

# Optionally log that the csv plugin is loaded
import logging

logging.info("CSV plugin initialized.")
