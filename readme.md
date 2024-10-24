# Mid-term Project Description:
- This project is a Midterm project  focuses on building an advanced calculator app in python. It is designed to highlight industry level coding practicies and flow, including design patterns, modular code, logging, environment variable configuration and more. 
1. Create directory and use touch command create files.
2. Integrate these concepts with existing program to add four basic commands: add, subtract, multiply, and divide, making calculator interactive.
3. Make a menu command that, when the application launches and the user inputs "menu," shows the available commands from the command dictionary.
4. Plugin Architecture:
 - refactor program to enable plugins to load automatically, making it simple to add commands without requiring manual updates.
5. Install Pandas library for load and save data in csv format. 
5. GitHub Actions:
- This feature involves setting up GitHub Actions to automatically run our program's tests whenever changes are pushed to the main branch. By doing this, yoweu can ensure that any new code additions or modifications don't break existing functionality.
6. Environment Variables:
- Using environment variables is important for managing sensitive data like passwords, API keys, and other configuration settings without hardcoding them in our program. By storing this information in environment variables, we can keep it secure and easily change it without modifying the code.
- create .env file 
 - ENVIRONMENT=DEVELOPMENT
 - DATABASE_USERNAME=root
 
- we learn to create a .env file to store these variables locally and ensure that this file is added to .gitignore to prevent it from being accidentally pushed to GitHub. This practice protects sensitive information and helps maintain security in our projects. 
7. Logging:
- Adding logging functionality to our program will allow us to track application behavior, monitor usage, and debug more effectively. Unlike simple print statements, logging can provide more structured and detailed output.
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