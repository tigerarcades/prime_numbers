import sys

from tigerarcades.primes import is_prime_number


def main(argument: int):
    """
    Main function calling library code.
    """
    print(f"value {argument} is prime: {is_prime_number(argument)}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--number", type=int, help="the argument for the primality test"
    )
    args = parser.parse_args()
    if args.number is not None:
        main(args.number)
        sys.exit(0)
    else:
        print(
            "argument --number must not be empty and an integer value",
            file=sys.stderr,
        )
        sys.exit(1)
