class Style:
    """Class to handle text styling in the terminal."""

    # ANSI style codes
    STYLES = {
        "bold": "\033[1m",
        "underline": "\033[4m",
        "reset": "\033[0m"
    }

    @staticmethod
    def stylize(text, style):
        """Apply a style to the given text."""
        if style.lower() not in Style.STYLES:
            raise ValueError(f"Unsupported style: {style}. Available styles: {list(Style.STYLES.keys())}")
        return f"{Style.STYLES[style.lower()]}{text}{Style.STYLES['reset']}"