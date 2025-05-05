import sys
import time

class ProgressBar:
    """Simple terminal progress bar."""

    def __init__(self, total, width=50, fill_char="#", empty_char="-"):
        self.total = total
        self.width = width
        self.fill_char = fill_char
        self.empty_char = empty_char
        self.progress = 0

    def update(self, increment=1):
        """Update the progress bar by an increment."""
        self.progress = min(self.progress + increment, self.total)
        percent = (self.progress / self.total) * 100
        filled = int(self.width * self.progress // self.total)
        bar = self.fill_char * filled + self.empty_char * (self.width - filled)
        sys.stdout.write(f"\r[{bar}] {percent:.1f}%")
        sys.stdout.flush()
        if self.progress == self.total:
            sys.stdout.write("\n")
            sys.stdout.flush()