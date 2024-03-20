from AnsiColors import AnsiColors


class InputData:
    RED_ATTENTION = f"{AnsiColors.RED}Attention!{AnsiColors.RESET}"
    ALPHANUMERIC_CHARACTERS_ERROR = (
        f"{RED_ATTENTION}\nOnly alphanumeric characters are allowed."
    )
    EMPTY_STRING_ERROR = f"{RED_ATTENTION}\nNo characters were inserted."

    @staticmethod
    def read_string(message: str, alphanumeric: bool) -> str:
        """Prints message in the terminal and reads the text inserted by the user. If it isn't a string an error message is printed. It's also possible to select if the inserted text needs to be alphanumeric or not via the alphanumeric input variable.

        Params:
            message -> The message to print.

            alphanumeric -> If the input needs to be alphanumeric or not.

        Returns:
            A string representing the user input.
        """

        if not alphanumeric:
            return input(message).strip()

        is_alphanumeric = False
        while not is_alphanumeric:
            read = input(message).strip()

            is_alphanumeric = read.isalnum()

            if not is_alphanumeric:
                print(InputData.ALPHANUMERIC_CHARACTERS_ERROR)

        return read

    @staticmethod
    def read_non_empty_string(message: str, alphanumeric: bool) -> str:
        """Prints message in the terminal and reads the text inserted by the user, given that it isn't empty. If it isn't a string an error message is printed. It's also possible to select if the inserted text needs to be alphanumeric or not via the alphanumeric input variable.

        Params:
            message -> The message to print.

            alphanumeric -> If the input needs to be alphanumeric or not.

        Returns:
            A string representing the user input.
        """

        is_empty = False

        while not is_empty:
            read = InputData.read_string(message, alphanumeric)

            is_empty = not read
            if is_empty:
                print(InputData)

    @staticmethod
    def read_char(message: str, allowed: str = None) -> str:
        pass

    @staticmethod
    def read_yer_or_no(question: str) -> bool:
        pass

    @staticmethod
    def read_integer(message: str) -> int:
        pass

    @staticmethod
    def read_integer_with_minimum(message: str, min: int) -> int:
        pass


def main():
    print("Testing...")

    print("Read string")
    test = InputData.read_string("Insert your string: ", True)
    print(f"You inserted {test}")


if __name__ == "__main__":
    main()
