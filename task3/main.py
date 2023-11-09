import unittest
import pandas as pd


def validate_data(data):
    if not data['open'].dtype == float:
        return False

    if not data['high'].dtype == float:
        return False

    if not data['low'].dtype == float:
        return False

    if not data['close'].dtype == float:
        return False

    if not data['volume'].dtype == 'int64':
        return False

    if not data['instrument'].dtype == object:
        return False

    if not data['datetime'].dtype == '<M8[ns]':
        return False

    return True


class TestDataValidation(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_excel('task3/HINDALCO_1D.xlsx')

    def test_valid_data(self):
        self.assertTrue(validate_data(self.data))

    def test_invalid_open(self):
        invalid_data = self.data.copy()
        invalid_data['open'] = 'invalid'
        self.assertFalse(validate_data(invalid_data))

    def test_invalid_high(self):
        invalid_data = self.data.copy()
        invalid_data['high'] = 'invalid'
        self.assertFalse(validate_data(invalid_data))

    def test_invalid_low(self):
        invalid_data = self.data.copy()
        invalid_data['low'] = 'invalid'
        self.assertFalse(validate_data(invalid_data))

    def test_invalid_close(self):
        invalid_data = self.data.copy()
        invalid_data['close'] = 'invalid'
        self.assertFalse(validate_data(invalid_data))

    def test_invalid_volume(self):
        invalid_data = self.data.copy()
        invalid_data['volume'] = 1.5
        self.assertFalse(validate_data(invalid_data))

    def test_invalid_instrument(self):
        invalid_data = self.data.copy()
        invalid_data['instrument'] = 123
        self.assertFalse(validate_data(invalid_data))

    def test_invalid_date(self):
        invalid_data = self.data.copy()
        invalid_data['datetime'] = 'invalid'
        self.assertFalse(validate_data(invalid_data))


if __name__ == '__main__':
    unittest.main()
