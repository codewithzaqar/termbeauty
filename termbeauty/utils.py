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

def draw_box(text, width=None, border_char="*"):
    """Draw a simple box around text with customizable border character."""
    if width is None:
        width = shutil.get_terminal_size().columns - 4  # Account for padding
    text = text.strip()
    text_width = min(len(text), width - 4)  # Space for borders and padding
    padding_text = f" {text[:text_width].center(text_width)} "
    border = border_char * (len(padding_text) + 2)
    print(border)
    print(f"{border_char}{padding_text}{border_char}")
    print(border) 