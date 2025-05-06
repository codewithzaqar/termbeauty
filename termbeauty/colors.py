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
    def colorize(text, fg_color=None, bg_color=None, fg_256=None, bg_256=None, fg_rgb=None, bg_rgb=None):
        """Apply foreground and/or background color to the given text."""
        result = text
        reset = "\033[0m"

        # Standard foreground color
        if fg_color:
            if fg_color.lower() not in Color.FOREGROUND:
                raise ValueError(f"Unsupported foreground color: {fg_color}. Available: {list(Color.FOREGROUND.keys())}")
            result = f"{Color.FOREGROUND[fg_color.lower()]}{result}"

        # Standard background color
        if bg_color:
            if bg_color.lower() not in Color.BACKGROUND:
                raise ValueError(f"Unsupported background color: {bg_color}. Available: {list(Color.BACKGROUND.keys())}")
            result = f"{Color.BACKGROUND[bg_color.lower()]}{result}"
        return f"{result}{Color.FOREGROUND['reset']}"
    
        # 256-color foreground
        if fg_256 is not None:
            if not (0 <= fg_256 <= 255):
                raise ValueError("256-color code must be between 0 and 255")
            result = f"\033[38;5;{fg_256}m{result}]"

        # 256-color background
        if bg_256 is not None:
            if not (0 <= bg_256 <= 255):
                raise ValueError("256-color code must be between 0 and 255")
            result = f"\033[48;5;{bg_256}m{result}]"
        
        # True-color foreground (RGB)
        if fg_rgb:
            if not (isinstance(fg_rgb, tuple) and len(fg_rgb) == 3 and all(0 <= v <= 255 for v in fg_rgb)):
                raise ValueError("fg_rgb must be a tuple of 3 integers (0-255) for R, G, B")
            r, g, b = fg_rgb
            result = f"\033[38;2;{r};{g};{b}m{result}]"

        # True-color background (RGB)
        if bg_rgb:
            if not (isinstance(bg_rgb, tuple) and len(bg_rgb) == 3 and all(0 <= v <= 255 for v in bg_rgb)):
                raise ValueError("bg_rgb must be a tuple of 3 integers (0-255) for R, G, B")
            r, g, b = bg_rgb
            result = f"\033[48;2;{r};{g};{b}m{result}]"

        return f"{result}{reset}"