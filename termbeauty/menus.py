import sys
import os
import msvcrt  # For Windows key input
from .formatters import Formatter
from .utils import clear_screen

class Menu:
    """Interactive terminal menu with customizable options and styling."""

    def __init__(self, options, title="Select an option", fg_color=None, bg_color=None, fg_256=None, bg_256=None, fg_rgb=None, bg_rgb=None, style=None):
        self.options = options
        self.title = title
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.fg_256 = fg_256
        self.bg_256 = bg_256
        self.fg_rgb = fg_rgb
        self.bg_rgb = bg_rgb
        self.style = style
        self.selected = 0

    def display(self):
        """Display the menu with the current selection highlighted."""
        clear_screen()
        print(Formatter.format_text(self.title, fg_color=self.fg_color, bg_color=self.bg_color, 
                                   fg_256=self.fg_256, bg_256=self.bg_256, fg_rgb=self.fg_rgb, bg_rgb=self.bg_rgb, style=self.style))
        print()
        for i, option in enumerate(self.options):
            prefix = "> " if i == self.selected else "  "
            text = f"{prefix}{option}"
            if i == self.selected:
                text = Formatter.format_text(text, fg_color="white", bg_color="blue", style="bold")
            else:
                text = Formatter.format_text(text, fg_color=self.fg_color, bg_color=self.bg_color, 
                                            fg_256=self.fg_256, bg_256=self.bg_256, fg_rgb=self.fg_rgb, bg_rgb=self.bg_rgb, style=self.style)
            print(text)

    def run(self):
        """Run the interactive menu and return the selected option index."""
        if sys.platform == "win32":
            return self._run_menu_windows()
        else:
            try:
                import tty
                import termios
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    return self._run_menu_unix()
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            except ImportError:
                # Fallback to basic input if termios is unavailable
                return self._run_menu_basic()

    def _run_menu_unix(self):
        """Handle menu navigation for Unix-like systems."""
        while True:
            self.display()
            char = sys.stdin.read(1)
            if char == "\x1b":  # Escape sequence (arrow keys)
                sys.stdin.read(1)  # Skip [
                key = sys.stdin.read(1)
                if key == "A":  # Up arrow
                    self.selected = (self.selected - 1) % len(self.options)
                elif key == "B":  # Down arrow
                    self.selected = (self.selected + 1) % len(self.options)
            elif char in ("\r", "\n"):  # Enter key
                return self.selected
            elif char == "\x03":  # Ctrl+C
                return None

    def _run_menu_windows(self):
        """Handle menu navigation for Windows with arrow key support."""
        while True:
            self.display()
            key = msvcrt.getch()
            if key == b"\xe0":  # Arrow key prefix
                key = msvcrt.getch()
                if key == b"H":  # Up arrow
                    self.selected = (self.selected - 1) % len(self.options)
                elif key == b"P":  # Down arrow
                    self.selected = (self.selected + 1) % len(self.options)
            elif key in (b"\r", b"\n"):  # Enter key
                return self.selected
            elif key == b"\x03":  # Ctrl+C
                return None

    def _run_menu_basic(self):
        """Fallback menu navigation for systems without termios or msvcrt support."""
        self.display()
        print("\nUse numbers to select an option (0 to quit):")
        while True:
            try:
                choice = input("> ")
                if choice == "0":
                    return None
                choice = int(choice) - 1
                if 0 <= choice < len(self.options):
                    return choice
            except ValueError:
                self.display()
                print("\nInvalid input. Use numbers to select an option (0 to quit):")