import shutil
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def print_centered(text, width=None):
    """Print text centered in the terminal."""
    if width is None:
        width = shutil.get_terminal_size().columns
    print(text.center(width))