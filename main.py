# main.py
from calculator import App    

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    calculator = App().start()  # Instantiate an instance of App