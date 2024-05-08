# Standard Modules
from enum import IntEnum
from typing import Iterable

# Internal Modules
from kibo_pgar_lib import AnsiFontColors, AnsiFontWeights, RESET


class Alignment(IntEnum):
    LEFT: int = 0
    CENTER: int = 1
    RIGHT: int = 2


class CLITable:
    _RED_ERROR: str = f"{AnsiFontColors.RED}{AnsiFontWeights.BOLD}Error!{RESET}\n"
    _ROWS_LENGTH_EXCEPTION: str = (
        f"{_RED_ERROR}All the rows must be lists of the same length."
    )
    _ROW_LENGTH_EXCEPTION: str = (
        f"{_RED_ERROR}The new row length must be equal to all the others."
    )

    _HORIZONTAL_SEPARATOR: str = "-"
    _VERTICAL_SEPARATOR: str = "|"
    _JOIN_SEPARATOR: list[str] = ["+", " "]

    def __init__(self) -> None:
        self._show_vlines = False
        self._cell_alignment = Alignment.RIGHT
        self._headers: list[str] = []
        self._table: list[list[str]] = []

    @property
    def show_vlines(self) -> bool:
        return self._show_vlines

    @show_vlines.setter
    def show_vlines(self, show: bool) -> None:
        self._show_vlines = show

    @property
    def headers(self) -> list[str]:
        return self._headers

    @headers.setter
    def headers(self, headers: list[str]) -> None:
        self._headers = headers

    @property
    def rows(self) -> list[list[str]]:
        return self._table

    @rows.setter
    def rows(self, rows: list[list[str]]) -> None:
        if not all(
            isinstance(row, list) and len(row) == len(self._headers) for row in rows
        ):
            raise ValueError(CLITable._ROWS_LENGTH_EXCEPTION)

        self._table = rows

    def append_header(self, header: str) -> None:
        self._headers.append(header)

        for row in self._table:
            row.append("")

    def extend_headers(self, headers: Iterable[str]) -> None:
        self._headers.extend(headers)

        to_extend: list[str] = ["" for _ in range(len(headers))]
        for row in self._table:
            row.extend(to_extend)

    def append_row(self, row: list[str]) -> None:
        if len(row) != len(self._headers):
            raise ValueError(CLITable._ROW_LENGTH_EXCEPTION)

        self._table.append(row)

    def extend_table(self, rows: list[list[str]]) -> None:
        if not all(
            isinstance(row, list) and len(row) == len(self._headers) for row in rows
        ):
            raise ValueError(CLITable._ROWS_LENGTH_EXCEPTION)

        self._table.extend(rows)

    @property
    def _get_max_width_per_column(self) -> list[int]:
        max_widths: list[int] = [0 for _ in range(len(self._headers))]
        local_table: list[list[str]] = self._table
        local_table.insert(0, self._headers)

        for i, row in enumerate(local_table):
            for cell in row:
                max_widths[i] = max(max_widths[i], len(cell))

        return max_widths

    def __str__(self) -> str:
        pass


def main() -> None:
    cock: CLITable = CLITable()

    cock.headers = ["id", "name", "salary", "age", "gender", "department"]
    cock.extend_table(
        [
            ["1", "Sam", "95000", "45", "Male", "Operations"],
            ["2", "Bob", "80000", "21", "Male", "Support"],
            ["3", "Anne", "125000", "25", "Female", "Analytics"],
            ["4", "Julia", "73000", "30", "Female", "Analytics"],
        ]
    )

    print(cock._get_max_width_per_column())


if __name__ == "__main__":
    main()
