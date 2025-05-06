import shutil
import os
import sys

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

def supports_256_colors():
    """Check if the terminal supports 256 colors."""
    if sys.platform == "win32":
        # Windows terminals vary; assume modern terminals (e.g., Windows Terminal) support 256 colors
        return os.environ.get("TERM") in ["xterm-256color", "screen-256color"] or "WT_SESSION" in os.environ
    return os.environ.get("TERM") in ["xterm-256color", "screen-256color", "linux"]

def supports_true_color():
    """Check if the terminal supports true-color (24-bit RGB)."""
    term = os.environ.get("TERM", "")
    colorterm = os.environ.get("COLORTERM", "")
    if sys.platform == "win32":
        # Modern Windows terminals (e.g., Windows Terminal) often support true-color
        return "WT_SESSION" in os.environ or colorterm in ["truecolor", "24bit"]
    return colorterm in ["truecolor", "24bit"] or term.endswith("-truecolor")