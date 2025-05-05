from .formatters import Formatter

class Table:
    """Class to create and display formatted tables in the terminal."""

    def __init__(self, headers, border_char="|", align="left"):
        self.headers = headers
        self.rows = []
        self.border_char = border_char
        self.align = align.lower()
        self.widths = [len(str(h)) for h in headers]

    def add_row(self, row):
        """Add a row to the table and update column widths."""
        if len(row) != len(self.headers):
            raise ValueError(f"Row length ({len(row)}) must match headers ({len(self.headers)})")
        self.rows.append(row)
        self.widths = [max(w, len(str(cell))) for w, cell in zip(self.widths, row)]

    def render(self, fg_color=None, bg_color=None, fg_256=None, bg_256=None, style=None):
        """Render the table as a formatted string."""
        lines = []
        # Header
        header_cells = [str(h).ljust(w) if self.align == "left" else str(h).rjust(w) for h, w in zip(self.headers, self.widths)]
        header_line = f" {self.border_char} ".join(header_cells)
        lines.append(f"{self.border_char} {header_line} {self.border_char}")
        # Separator
        lines.append(self.border_char + "-+-".join("-" * w for w in self.widths) + self.border_char)
        # Rows
        for row in self.rows:
            cells = [str(c).ljust(w) if self.align == "left" else str(c).rjust(w) for c, w in zip(row, self.widths)]
            row_line = f" {self.border_char} ".join(cells)
            lines.append(f"{self.border_char} {row_line} {self.border_char}")
        # Format the entire table
        formatted = "\n".join(lines)
        return Formatter.format_text(formatted, fg_color, bg_color, fg_256, bg_256, style)
    
    def print(self, fg_color=None, bg_color=None, fg_256=None, bg_256=None, style=None):
        """Print the table directly to the terminal."""
        print(self.render(fg_color, bg_color, fg_256, bg_256, style))