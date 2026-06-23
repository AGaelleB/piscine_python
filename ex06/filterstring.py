import sys
from ft_filter import ft_filter


def main():
    """Print words from sys.argv[1] longer than sys.argv[2] characters."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        int_value = int(sys.argv[2])
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    string_value = sys.argv[1]
    tokenized_string = string_value.split()

    filtered = ft_filter(lambda x: len(x) > int_value, tokenized_string)
    res = [word for word in filtered]
    print(res)


if __name__ == "__main__":
    main()
