import unittest
from format_price import format_price_in_local


class FormatPriceTestCase(unittest.TestCase):

    def test_integer(self):
        self.assertEqual(
            format_price_in_local(1234567890),
            '1 234 567 890'
        )
        
    def test_integer_with_zero_decimals(self):
        self.assertEqual(
            format_price_in_local(00009.000),
            '9'
        )
        
    def test_float(self):
        self.assertEqual(
            format_price_in_local(1234567890.128),
            '1 234 567 890.13'
        )
   
    def test_float_with_dot_in_string(self):
        self.assertEqual(
            format_price_in_local('1234567890.199'),
            '1 234 567 890.20'
        )
   
    def test_float_with_comma_in_qoutes(self):
        self.assertEqual(
            format_price_in_local('1234567890,5678'),
            '1 234 567 890.57'
        )

    def test_price_in_double_quotes(self):
        self.assertEqual(
            format_price_in_local("1234567890,009"),
            '1 234 567 890.01'
        )

    def test_zero(self):
        self.assertEqual(
            format_price_in_local(0000.00000),
            '0'
        )

    def test_wrong_input_format(self):
        self.colon_delimeter = '123456789:126'
        self.letter_delimeter = '123456689z3667'
        self.any_delimeter = '123456689-3667'
        self.list = [1234,5678]
        self.tuple = (12345,67890)
        self.dict = {12:34, 56:78}
        self.none = None
        self.negative = -1234.567

        with self.assertRaises(ValueError):
            format_price_in_local(self.colon_delimeter)

        with self.assertRaises(ValueError):
            format_price_in_local(self.letter_delimeter)

        with self.assertRaises(ValueError):
            format_price_in_local(self.any_delimeter)

        with self.assertRaises(ValueError):
            format_price_in_local(self.list)

        with self.assertRaises(ValueError):
            format_price_in_local(self.tuple)

        with self.assertRaises(ValueError):
            format_price_in_local(self.dict)

        with self.assertRaises(ValueError):
            format_price_in_local(self.none)

        with self.assertRaises(ValueError):
            format_price_in_local(self.negative)


if __name__ == '__main__':
    unittest.main()
