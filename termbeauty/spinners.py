import os
import sys
import time
import itertools

class Spinner:
    """Simple terminal spinner for loading indicators."""

    SPINNER_STYLES = {
        "dots": ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
        "line": ["-", "\\", "|", "/"],
        "arrow": ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"],
        "simple": ["*", "+", "x", "o"]  # Fallback for basic terminals
    }

    def __init__(self, message="Processing", style="dots", speed=0.1):
        self.message = message
        self.style = style if style in self.SPINNER_STYLES else "simple"
        if sys.platform == "win32" and style == "dots" and "WT_SESSION" not in os.environ:
            self.style = "simple"
        self.frames = self.SPINNER_STYLES[self.style]
        self.speed = speed
        self.running = False

    def __enter__(self):
        """Start the spinner."""
        self.running = True
        self._spin()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Stop the spinner and clear the line."""
        self.running = False
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")
        sys.stdout.flush()

    def _spin(self):
        """Run the spinner animation in a loop."""
        spinner = itertools.cycle(self.frames)
        while self.running:
            sys.stdout.write(f"\r{next(spinner)} {self.message}")
            sys.stdout.flush()
            time.sleep(self.speed)