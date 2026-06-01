import sys as sys


def main():
    """
    Counts uppercase, lowercase, digits, punctuation, spaces,
    and total characters in a text provided via command-line or user input.
    """

    argc = len(sys.argv)

    try:
        assert (argc <= 2), "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

    arg_value = None

    if (argc == 1):
        print("What is the text to count?")
        try:
            arg_value = sys.stdin.read()
        except KeyboardInterrupt:
            sys.exit(1)

    if (argc == 2):
        arg_value = sys.argv[1]

    arg_value = str(arg_value)

    count_uppercase = 0
    count_lowercase = 0
    count_digit = 0
    count_punctuation = 0
    count_space = 0

    for c in arg_value:
        if c.isupper():
            count_uppercase += 1
        elif c.islower():
            count_lowercase += 1
        elif c.isdigit():
            count_digit += 1
        elif c.isspace() or c == "\r" or c == "¶":
            count_space += 1
        else:
            count_punctuation += 1

    print(f"The text contains {len(arg_value)} characters:")
    print(f"{count_uppercase} upper letters")
    print(f"{count_lowercase} lower letters")
    print(f"{count_punctuation} punctuation marks")
    print(f"{count_space} spaces")
    print(f"{count_digit} digits")


if __name__ == "__main__":
    main()
