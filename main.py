import os
import subprocess
import sys


def run_code(day):
    if 0 <= day <= 25:
        directory = f"{day}"
        file_path = os.path.join(directory, "main.py")
        if os.path.isfile(file_path):
            subprocess.run([sys.executable, file_path])
        else:
            print(f"No main.py found in directory {directory}")
    else:
        print("Please provide an integer between 0 and 25")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <day>")
    else:
        try:
            day = int(sys.argv[1])
            run_code(day)
        except ValueError:
            print("Please provide a valid integer")
