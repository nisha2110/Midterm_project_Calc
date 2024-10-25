# Mid-term Project Description:
- This project is a Midterm project  focuses on building an advanced calculator app in python. It is designed to highlight industry level coding practicies and flow, including design patterns, modular code, logging, environment variable configuration and more. 

## Video demonstration:
- Link Here [https://www.youtube.com/watch?v=eyA2-21DJp0]
## Key Features:
1. Basic Arithmetic Operations:
- Integrate these concepts with existing program to add four basic commands: add, subtract, multiply, and divide, making calculator interactive  through a command-line interface (REPL).
2. Menu Command: 
- Make a menu command that, when the application launches and the user inputs "menu," shows the available commands from the command dictionary.
3. Plugin Architecture:
 - refactor program to enable plugins to load automatically, allowing new commands to be added easily without modifying the core code.
4. Install Pandas library for load and save data in csv format. 
5. GitHub Actions:
- This feature involves setting up GitHub Actions to automatically run our program's tests whenever changes are pushed to the main branch. By doing this, yoweu can ensure that any new code additions or modifications don't break existing functionality.
6. Environment Variables:
- Using environment variables is important for managing sensitive data like passwords, API keys, and other configuration settings without hardcoding them in our program. By storing this information in environment variables, we can keep it secure and easily change it without modifying the code.
- This variable indicates the environment in which our application is running. Common values include DEVELOPMENT, TESTING, and PRODUCTION and Ensure .env file is properly loaded (using packages like python-dotenv if needed) to access these variables.
- create .env file 
 - ENVIRONMENT=DEVELOPMENT
 - DATABASE_USERNAME=root
 - Link to Example Code :[https://github.com/nisha2110/Midterm_project_Calc/blob/master/calculator/__init__.py]
- we learn to create a .env file to store these variables locally and ensure that this file is added to .gitignore to prevent it from being accidentally pushed to GitHub. This practice protects sensitive information and helps maintain security in our projects. 
7. Logging:
- Adding logging functionality to our program will allow us to track application behavior, monitor usage, and debug more effectively. Unlike simple print statements, logging can provide more structured and detailed output.

## Implememtation of the design patterns:
1. Command-Line Interface (REPL):
- The REPL interface (app.start()) enables direct interaction with the calculator.
Supports arithmetic operations (add, subtract, multiply, divide) and manages calculation history.
To start, run python3 main.py and interact via the REPL.
-  Link Here [https://github.com/nisha2110/Midterm_project_Calc/blob/master/calculator/__init__.py]

2. Plugin System:
- Implemented a plugin loader to dynamically load new commands without changing core code.
Plugins are detected from the plugins/ directory. Each plugin must follow the structure outlined in the documentation.
Use the menu command within the REPL to view available commands.
- Link Here [https://github.com/nisha2110/Midterm_project_Calc/tree/master/calculator/plugins]

3. Calculation History Management with Pandas:
- Supports saving, loading, clearing, and deleting calculation history using Pandas.
- History is stored in arithmetic_operations.csv.
- Link Here calculation history  [https://github.com/nisha2110/Midterm_project_Calc/blob/master/calculator/history.py] 
- Link Here CSV file [https://github.com/nisha2110/Midterm_project_Calc/tree/master/data]

## Design Patterns and Architecture:
1. Facade Pattern:
- Simplifies data manipulation using Pandas by encapsulating complex interactions.
- Link Here [https://github.com/nisha2110/Midterm_project_Calc/blob/master/calculator/history.py]
2. Command Pattern:
- Structures commands within the REPL, enabling easier addition and management of commands.
- Link Here [https://github.com/nisha2110/Midterm_project_Calc/blob/master/calculator/__init__.py]
3. Factory Method, Singleton, and Strategy Patterns:
- Enhance code flexibility and scalability.

## Logging:
- logging.basicConfig() sets up logging with a specific format, outputting logs to both a file (calculator.log) and the console.
- Reads the logging.conf file to set up the logging system based on the detailed configuration provided.
- We can write logs using logging.info(), logging.warning(), and logging.error() within our program. The logs will be managed by the - - handlers our configured (console output and rotating file).
- Link Here [https://github.com/nisha2110/Midterm_project_Calc/blob/master/logging.conf]
- Link to logs manage [https://github.com/nisha2110/Midterm_project_Calc/blob/master/calculator/__init__.py]
## Exception Handling (LBYL & EAFP)
1. Look Before You Leap (LBYL):
- Check conditions before executing code that may cause exceptions (e.g., checking file existence before reading).
- Before attempting to read the input CSV file, the code checks if the file exists using os.path.exists(input_csv_file_path).
-  This is a precautionary step to ensure the code only tries to read the file if it is actually present.
- If the file exists, it proceeds to read the data from the file inside a try block, which allows it to handle any potential exceptions 
- If the file does not exist, it avoids the read attempt and directly creates a new, empty DataFrame.
- Link Here [https://github.com/nisha2110/Midterm_project_Calc/blob/master/calculator/plugins/csv/csv_command.py]
2. Easier to Ask for Forgiveness than Permission (EAFP):
- Use try-except blocks to handle potential exceptions gracefully.
Link to EAFP [https://github.com/nisha2110/Midterm_project_Calc/blob/master/calculator/commands/__init__.py]
## Instructions:
1. create clone the repo.
2. First Deactivate the virtual environment with the command "deactivate" and then activate it again command.
  i. source venv/bin/activate
3. Install the required libraries.
  - pip install pandas
  - Update the requirements file with pip freeze > requirements.txt.

Note When someone copies / clones my repository they will install the specfic library / dependency requirements for my project using the command:

-> pip install -r requirments.txt
-> Finally, Open VScode and test code.
   i. code .

## Testing
1. Run all tests with : pytest
2. Run Coverage : pytest --cov
3. Run application: python main.py
4. To test a specific file, use pytest tests/test_calculator.py

## Other commands used during project
 1. mv oldfile newfilename
 2. git remote remove origin
 3. rm -rf .pytest_cache
 4. To add multiple specific files: git add path/to/file1.py path/to/file2.py path/to/file3.py
 5. coverage report -m