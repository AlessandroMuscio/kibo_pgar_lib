from AnsiColors import AnsiColors


class InputData:
    """The class can read a specific data type inserted in input by the user.
    It also allows the possibility to make controls on the data inserted."""

    RED_ATTENTION = f"{AnsiColors.RED}Attention!{AnsiColors.RESET}"
    ALPHANUMERIC_CHARACTERS_ERROR = (
        f"{RED_ATTENTION}\nOnly alphanumeric characters are allowed."
    )
    EMPTY_STRING_ERROR = f"{RED_ATTENTION}\nNo characters were inserted."
    ALLOWED_CHARACTERS_ERROR = f"{RED_ATTENTION}\nThe only allowed characters are: "
    YES_ANSWERS = "yY"
    NO_ANSWERS = "nN"
    INTEGER_FORMAT_ERROR = f"{RED_ATTENTION}\nThe inserted data is in an incorrect format. An integer is required."
    MINIMUM_ERROR = (
        f"{RED_ATTENTION}\nA value greater than or equal to %.2f is required."
    )
    MAXIMUM_ERROR = f"{RED_ATTENTION}\nA value less than or equal to %.2f is required."
    FLOAT_FORMAT_ERROR = f"{RED_ATTENTION}\nThe inserted data is in an incorrect format. A float is required."

    def __init__(self) -> None:
        """Prevents instantiation of this class

        Raises:
            NotImplementedError
        """

        raise NotImplementedError()

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

        is_empty = True

        while is_empty:
            read = InputData.read_string(message, alphanumeric)

            is_empty = not bool(read)
            if is_empty:
                print(InputData.EMPTY_STRING_ERROR)

        return read

    @staticmethod
    def read_char(message: str, allowed: str = None) -> str:
        """Read a single character input from the user.

        Params:
            message -> The message to display to the user.

            allowed (optional) -> Contains the allowed characters, defaults to None.

        Returns:
            The single character input by the user.
        """

        is_allowed = False

        while not is_allowed:
            read = InputData.read_non_empty_string(message, False)[0]

            if allowed and read in allowed:
                is_allowed = True
            else:
                print(InputData.ALLOWED_CHARACTERS_ERROR, list(allowed))

        return read

    @staticmethod
    def read_yer_or_no(question: str) -> bool:
        """Prompts the user with a question and expects a yes or no response.

        Params:
            question -> The question to display the user without question mark.

        Returns:
            True if the user reponds with 'y' or 'Y', False otherwise.
        """

        question = f"{question}? [{InputData.YES_ANSWERS[1]}/{InputData.NO_ANSWERS[0]}]"
        response = InputData.read_char(question)

        return response in InputData.YES_ANSWERS

    @staticmethod
    def read_integer(message: str) -> int:
        """Reads an integer input from the user.

        Params:
            message -> The message to display the user.

        Returns:
            The integer input by the user.
        """

        is_integer = False

        while not is_integer:
            try:
                read = int(input(message))
                is_integer = True
            except ValueError:
                print(InputData.INTEGER_FORMAT_ERROR)

        return read

    @staticmethod
    def read_integer_with_minimum(message: str, min_value: int) -> int:
        """Reads an integer input from the user with a minimun value constraint.

        Params:
            message -> The message to display the user.

            min_value -> The minimum allowed value for the input.

        Returns:
            The integer input by the user that is greater than or equal to min.
        """

        is_input_valid = False

        while not is_input_valid:
            read = InputData.read_integer(message)
            if read >= min_value:
                is_input_valid = True
            else:
                print(InputData.MINIMUM_ERROR % min_value)

        return read

    @staticmethod
    def read_integer_with_maximum(message: str, max_value: int) -> int:
        """Reads an integer input from the user with a maximun value constraint.

        Params:
            message -> The message to display the user.

            max_value -> The maximum allowed value for the input.

        Returns:
            The integer input by the user that is less than or equal to max.
        """

        is_input_valid = False

        while not is_input_valid:
            read = InputData.read_integer(message)
            if read <= max_value:
                is_input_valid = True
            else:
                print(InputData.MAXIMUM_ERROR % max_value)

        return read

    @staticmethod
    def read_integer_between(message: str, min_value: int, max_value: int) -> int:
        """Reads an integer input from the user with a minimum and maximun value constraint.

        Params:
            message -> The message to display the user.

            min_value -> The minimum allowed value for the input.

            max_value -> The maximum allowed value for the input.

        Returns:
            The integer input by the user that is greater than or equal to min and less than or equal to max.
        """

        is_input_valid = False

        while not is_input_valid:
            read = InputData.read_integer(message)
            if read < min_value:
                print(InputData.MINIMUM_ERROR % max_value)
            elif read > max_value:
                print(InputData.MAXIMUM_ERROR % max_value)
            else:
                is_input_valid = True

        return read

    @staticmethod
    def read_float(message: str) -> float:
        """Reads a float input from the user.

        Params:
            message -> The message to display the user.

        Returns:
            The float input by the user.
        """

        is_float = False

        while not is_float:
            try:
                read = float(input(message))
                is_float = True
            except ValueError:
                print(InputData.FLOAT_FORMAT_ERROR)

        return read

    @staticmethod
    def read_float_with_minimum(message: str, min_value: float) -> float:
        """Reads a float input from the user with a minimun value constraint.

        Params:
            message -> The message to display the user.

            min_value -> The minimum allowed value for the input.

        Returns:
            The float input by the user that is greater than or equal to min.
        """

        is_input_valid = False

        while not is_input_valid:
            read = InputData.read_float(message)
            if read >= min_value:
                is_input_valid = True
            else:
                print(InputData.MINIMUM_ERROR % min_value)

        return read

    @staticmethod
    def read_float_with_maximum(message: str, max_value: float) -> float:
        """Reads a float input from the user with a maximun value constraint.

        Params:
            message -> The message to display the user.

            max_value -> The maximum allowed value for the input.

        Returns:
            The float input by the user that is less than or equal to max.
        """

        is_input_valid = False

        while not is_input_valid:
            read = InputData.read_float(message)
            if read <= max_value:
                is_input_valid = True
            else:
                print(InputData.MAXIMUM_ERROR % max_value)

        return read

    @staticmethod
    def read_float_between(message: str, min_value: float, max_value: float) -> float:
        """Reads a float input from the user with a minimum and maximun value constraint.

        Params:
            message -> The message to display the user.

            min_value -> The minimum allowed value for the input.

            max_value -> The maximum allowed value for the input.

        Returns:
            The float input by the user that is greater than or equal to min and less than or equal to max.
        """

        is_input_valid = False

        while not is_input_valid:
            read = InputData.read_float(message)
            if read < min_value:
                print(InputData.MINIMUM_ERROR % max_value)
            elif read > max_value:
                print(InputData.MAXIMUM_ERROR % max_value)
            else:
                is_input_valid = True

        return read
