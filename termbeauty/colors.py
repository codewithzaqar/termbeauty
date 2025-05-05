class Color:
    """Class to handle ANSI color codes for terminal text."""

    # ANSI color codes
    COLORS = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }

    @staticmethod
    def colorize(text, color):
        """Apply a color to the given text."""
        if color.lower() not in Color.COLORS:
            raise ValueError(f"Unsupported color: {color}. Available colors: {list(Color.COLORS.keys())}")
        return f"{Color.COLORS[color.lower()]}{text}{Color.COLORS['reset']}"