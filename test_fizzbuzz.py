# * write a unit test for the FizzBuzzer class using the python unittest
# module.

# * Test that the following.
#    * when `x = FizzBuzzer()`, `x.number` is 0
#    * when `x = FizzBuzzer()`, `x.next()` returns the string `"1"`
#    * when `x = FizzBuzzer(2)`,`x.next()` returns `"fizz"` and calling `x.next()`
# a second time returns `"4"`

import unittest
from fizzbuzz import FizzBuzzer

class TestFizzbuzz(unittest.TestCase):
    """Test FizzBuzz class with initial and subsequent values"""

    def test_fizzbuzz_when_0(self):
        x=FizzBuzzer()
        self.assertEqual(x.number, 0, "starting at 0 initializes number as 0")

    def test_fizzbuzz_when_0_next(self):
        x=FizzBuzzer(0)
        self.assertEqual("1", x.next()['result'], "starting at 0 followed by next returns 1 as string")
       
    def test_fizzbuzz_when_2_next(self):
        x=FizzBuzzer(2)
        self.assertEqual('fizz', x.next()['result'],"starting at 2 followed by next results in 3 which is fizz")

    def test_fizzbuzz_when_2_next_next(self):
        x=FizzBuzzer(2)
        x.next()
        self.assertEqual('4', x.next()['result'],"starting at 2 followed by next 2 times returns 4 as string")


#fizz_test = TestFizzbuzz()
#fizz_test.test_fizzbuzz_when_0()
#fizz_test.test_fizzbuzz_when_0_next()
#fizz_test.test_fizzbuzz_when_2_next()
#fizz_test.test_fizzbuzz_when_2_next_next()
        


