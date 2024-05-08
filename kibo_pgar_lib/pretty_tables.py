# Standard Modules
from enum import IntEnum
from typing import Any

# Internal Modules
from kibo_pgar_lib import RESET, AnsiFontColors, AnsiFontWeights


class Alignment(IntEnum):
    LEFT: int = -1
    CENTER: int = 0
    RIGHT: int = 1


class CommandLineTable:
    _RED_ERROR: str = f"{AnsiFontColors.RED}{AnsiFontWeights.BOLD}Error!{RESET}"
    _UNKNOWN_ALIGNMENT_EXCEPTION: str = "Impossible to set alignment, value unknown."
    _SET_HEADERS_EXCEPTION: str = "The headers can only be a list of strings."
    _SET_ROWS_EXCEPTION: str = (
        "All the rows must be lists of the same length as of the headers."
    )

    def __init__(self) -> None:
        self.show_vlines: bool = False
        self.cell_alignment: Alignment = Alignment.LEFT
        self.headers: list[str] = []
        self.rows: list[list[str]] = []

    def __getattr__(self, name: str) -> Any:
        return self.__dict__[f"_{name}"]

    def __setattr__(self, name: str, value: Any) -> None:
        match name:
            case "show_vlines":
                value = bool(value)

            case "cell_alignment":
                value = int(value)

                allowed_values: list[int] = list(map(int, Alignment))
                if value not in allowed_values:
                    raise ValueError(
                        "\n".join(
                            [
                                CommandLineTable._RED_ERROR,
                                CommandLineTable._UNKNOWN_ALIGNMENT_EXCEPTION,
                            ]
                        )
                    )

            case "headers":
                if not isinstance(value, list):
                    raise ValueError(
                        "\n".join(
                            [
                                CommandLineTable._RED_ERROR,
                                CommandLineTable._SET_HEADERS_EXCEPTION,
                            ]
                        )
                    )

                value = list(map(str, value))

            case "rows":
                if not (
                    isinstance(value, list)
                    and all(
                        isinstance(row, list) and len(row) == len(self.headers)
                        for row in value
                    )
                ):
                    raise ValueError(
                        "\n".join(
                            [
                                CommandLineTable._RED_ERROR,
                                CommandLineTable._SET_ROWS_EXCEPTION,
                            ]
                        )
                    )

                value = [[str(val) for val in row] for row in value]

        self.__dict__[f"_{name}"] = value


def main() -> None:
    tabella: CommandLineTable = CommandLineTable()

    tabella.show_vlines = True
    tabella.cell_alignment = 0
    tabella.headers = [1, 2, 3, 4]
    tabella.rows = [["a", "b", "c", "d"], [5, 6, 7, 8]]

    print(
        tabella.show_vlines,
        tabella.cell_alignment,
        tabella.headers,
        tabella.rows,
        sep="\n",
    )


if __name__ == "__main__":
    main()
