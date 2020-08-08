# ถ้า input / 3  == Fizz
# ถ้า 5 === Buzz
# ถ้า 5 3 == FizxBuzz
import unittest


def fizxbuzz(number):
    if number == 1:
        return 1
    if number == 3:
        return 'Fizz'


class TestFizzBuzz(unittest.TestCase):
    def test_input_1_should_get_1(self):
        result = fizxbuzz(1)
        self.assertEqual(result, 1)

    def test_input_3_should_get_fizz(self):
        result = fizxbuzz(3)
        self.assertEqual(result, 'Fizz')


# unittest.main()
print(__name__)

if __name__ == '__main__':
    unittest.main()
