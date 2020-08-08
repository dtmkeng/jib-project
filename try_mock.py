import random
import unittest

from unittest.mock import patch

class TestRandom(unittest.TestCase):
    
    @patch('__main__.random.randint')
    def test_it_should_call_raninit_with_1_and_10(self, mock):
        #call
        get_random_number_plus_one()
        ## assert here
        mock.assert_called_once_with(1, 10)
        
    @patch('__main__.random.randint')
    def test_it_should_get_4_when_random_get_3(self, mock):
        #mock
        mock.return_value = 3
        #call
        result = get_random_number_plus_one()
        ## assert here
        self.assertEqual(result, 4)

    def test_it_should_get_3(self):
        while True:
            result = get_random_number_plus_one()
            if result == 3:
                break
        self.assertEqual(result, 3)

def get_random_number_plus_one():
    return random.randint(1,10) + 1

unittest.main()