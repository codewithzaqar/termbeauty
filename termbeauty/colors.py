class Color:
    """Class to handle ANSI color codes for terminal text."""

    # ANSI foreground color codes
    FOREGROUND = {
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

    # ANSI background color codes
    BACKGROUND = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
        "reset": "\033[0m"
    }

    @staticmethod
    def colorize(text, fg_color=None, bg_color=None):
        """Apply foreground and/or background color to the given text."""
        result = text
        if fg_color:
            if fg_color.lower() not in Color.FOREGROUND:
                raise ValueError(f"Unsupported foreground color: {fg_color}. Available: {list(Color.FOREGROUND.keys())}")
            result = f"{Color.FOREGROUND[fg_color.lower()]}{result}"
        if bg_color:
            if bg_color.lower() not in Color.BACKGROUND:
                raise ValueError(f"Unsupported background color: {bg_color}. Available: {list(Color.BACKGROUND.keys())}")
            result = f"{Color.BACKGROUND[bg_color.lower()]}{result}"
        return f"{result}{Color.FOREGROUND['reset']}"