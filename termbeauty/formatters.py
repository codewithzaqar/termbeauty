from .colors import Color
from .styles import Style

class Formatter:
    """Class to combine colors and styles for rich terminal formatting."""

    @staticmethod
    def format_text(text, fg_color=None, bg_color=None, fg_256=None, bg_256=None, fg_rgb=None, bg_rgb=None, style=None):
        """Format text with optional color and style."""
        result = text
        if any([fg_color, bg_color, fg_256 is not None, bg_256 is not None, fg_rgb, bg_rgb]):
            result = Color.colorize(result, fg_color, bg_color, fg_256, bg_256, fg_rgb, bg_rgb)
        if style:
            result = Style.stylize(result, style)
        return result
    
    @staticmethod
    def print_formatted(text, fg_color=None, bg_color=None, fg_256=None, bg_256=None, fg_rgb=None, bg_rgb=None, style=None):
        """Print formatted text directly to the terminal"""
        print(Formatter.format_text(text, fg_color, bg_color, fg_256, bg_256, fg_rgb, bg_rgb, style))