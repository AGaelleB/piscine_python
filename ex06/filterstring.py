import sys
from ft_filter import ft_filter


def main():
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

    res = list(ft_filter(lambda x: len(x) > int_value, tokenized_string))
    print(res)


if __name__ == "__main__":
    main()