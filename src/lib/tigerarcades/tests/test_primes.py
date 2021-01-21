import unittest

from tigerarcades.primes import is_prime_number


class TestPrimesModule(unittest.TestCase):
    """
    The class is a container for testing all methods of `tigerarcades.primes`.
    """

    def test_is_prime_number(self):
        """
        Tests `tigerarcades.primes.is_prime_number` with different arguments.

        The tests are not very sophisticated, assuming a general understanding
        of primes. Large prime numbers and numbers which are not need to be
        tested as well.
        """
        self.assertEqual(False, is_prime_number(1))
        self.assertEqual(True, is_prime_number(2))
        self.assertEqual(True, is_prime_number(3))
        self.assertEqual(False, is_prime_number(4))
        self.assertEqual(True, is_prime_number(5))
        self.assertEqual(False, is_prime_number(6))
        self.assertEqual(True, is_prime_number(7))
        self.assertEqual(False, is_prime_number(8))
        self.assertEqual(False, is_prime_number(9))


if __name__ == "__main__":
    unittest.main()
