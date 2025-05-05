from .colors import Color
from .styles import Style

class Formatter:
    """Class to combine colors and styles for rich terminal formatting."""

    @staticmethod
    def format_text(text, fg_color=None, bg_color=None, style=None):
        """Format text with optional color and style."""
        result = text
        if fg_color or bg_color:
            result = Color.colorize(result, fg_color, bg_color)
        if style:
            result = Style.stylize(result, style)
        return result
    
    @staticmethod
    def print_formatted(text, fg_color=None, bg_color=None, style=None):
        """Print formatted text directly to the terminal"""
        print(Formatter.format_text(text, fg_color, bg_color, style))