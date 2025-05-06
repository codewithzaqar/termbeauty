from .formatters import Formatter

class Table:
    """Class to create and display formatted tables with per-cell styling in the terminal."""

    def __init__(self, headers, border_char="|", align="left"):
        self.headers = headers
        self.rows = []
        self.cell_formats = []  # Store formatting for each cell
        self.border_char = border_char
        self.align = align.lower()
        self.widths = [len(str(h)) for h in headers]

    def add_row(self, row, formats=None):
        """Add a row to the table with optional per-cell formatting and update column widths."""
        if len(row) != len(self.headers):
            raise ValueError(f"Row length ({len(row)}) must match headers ({len(self.headers)})")
        self.rows.append(row)
        # Ensure formats is a list of dicts, defaulting to empty dicts if None
        self.cell_formats.append(formats or [{}] * len(row))
        self.widths = [max(w, len(str(cell))) for w, cell in zip(self.widths, row)]

    def render(self, fg_color=None, bg_color=None, fg_256=None, bg_256=None, fg_rgb=None, bg_rgb=None, style=None):
        """Render the table as a formatted string with optional global and per-cell formatting."""
        if not self.rows:
            return Formatter.format_text("Empty table", fg_color, bg_color, fg_256, bg_256, fg_rgb, bg_rgb, style)
        lines = []
        # Header with global formatting
        header_cells = [str(h).ljust(w) if self.align == "left" else str(h).rjust(w) for h, w in zip(self.headers, self.widths)]
        header_line = f" {self.border_char} ".join(header_cells)
        formatted_header = Formatter.format_text(f"{self.border_char} {header_line} {self.border_char}", 
                                                fg_color, bg_color, fg_256, bg_256, fg_rgb, bg_rgb, style)
        lines.append(formatted_header)
        # Separator
        separator = self.border_char + "-+-".join("-" * w for w in self.widths) + self.border_char
        lines.append(Formatter.format_text(separator, fg_color, bg_color, fg_256, bg_256, fg_rgb, bg_rgb, style))
        # Rows with per-cell formatting 
        for row, row_formats in zip(self.rows, self.cell_formats):
            cells = []
            for cell, fmt, w in zip(row, row_formats, self.widths):
                cell_text = str(cell).ljust(w) if self.align == "left" else str(cell).rjust(w)
                cells.append(Formatter.format_text(cell_text, **fmt))
            row_line = f" {self.border_char} ".join(cells)
            lines.append(f"{self.border_char} {row_line} {self.border_char}")
        return "\n".join(lines)

    def print(self, fg_color=None, bg_color=None, fg_256=None, bg_256=None, fg_rgb=None, bg_rgb=None, style=None):
        """Print the table directly to the terminal."""
        print(self.render(fg_color, bg_color, fg_256, bg_256, fg_rgb, bg_rgb, style))