from .colors import Color
from .styles import Style

class Formatter:
    """Class to combine colors and styles for rich terminal formatting."""

    @staticmethod
    def format_text(text, fg_color=None, bg_color=None, fg_256=None, bg_256=None, style=None):
        """Format text with optional color and style."""
        result = text
        if fg_color or bg_color or fg_256 is not None or bg_256 is not None:
            result = Color.colorize(result, fg_color, bg_color, fg_256, bg_256)
        if style:
            result = Style.stylize(result, style)
        return result
    
    @staticmethod
    def print_formatted(text, fg_color=None, bg_color=None, fg_256=None, bg_256=None, style=None):
        """Print formatted text directly to the terminal"""
        print(Formatter.format_text(text, fg_color, bg_color, fg_256, bg_256, style))