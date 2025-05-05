from .colors import Color
from .styles import Style

class Formatter:
    """Class to combine colors and styles for rich terminal formatting."""

    @staticmethod
    def format_text(text, color=None, style=None):
        """Format text with optional color and style."""
        result = text
        if color:
            result = Color.colorize(result, color)
        if style:
            result = Style.stylize(result, style)
        return result
    
    @staticmethod
    def print_formatted(text, color=None, style=None):
        """Print formatted text directly to the terminal"""
        print(Formatter.format_text(text, color, style))