import unittest
import random
import sys
from multiprocessing import Process
from words2num import words2num, NumberParseException
from num2words import num2words


class TestEN_US(unittest.TestCase):
    """Test inverse text normalization for numbers.
    """

    def test_en_us(self):
        """Test valid en-US input.
        """
        test_trials = ("two",
            "twelve",
            "zero",
            "one hundred and two",
            "a hundred twenty-three",
            "one thousand one hundred and one",
            "thirty-four hundred fifty-six",
            "two hundred thousand, three hundred forty five",
            "twenty-three hundred thousand four",
            "sixty-eight billion, two hundred two million and two",
            "sixty eight billion two hundred two million two",
            "nine trillion eight hundred seven",
            "ninety nine point nine",
            "ninety nine point nine nine nine nine nine nine nine six",
            "fifteen point four",
            "two thousand point five",
            "eleven million point three three",
            "one billion point six four",
            "six hundred point nine nine",
            "one point zero zero four",
            "zero point five",
            "four point oh",
            "nine point oh nine",
            "point eight eight",
            "point oh zero five",
            "a thousand and fifty four",
            "three sixty",
            "four twelve",
            "three sixty five")
        test_targets = (2,
            12,
            0,
            102,
            123,
            1101,
            3456,
            200345,
            2300004,
            68202000002,
            68202000002,
            9000000000807,
            99.9,
            99.99999996,
            15.4,
            2000.5,
            11000000.33,
            1000000000.64,
            600.99,
            1.004,
            0.5,
            4.0,
            9.09,
            0.88,
            0.005,
            1054,
            360,
            412,
            365
            )
        tests = zip(test_trials, test_targets)

        for (trial, target) in tests:
            result = words2num(trial)
            assert result == target,\
                   "'{0}' -> {1} != {2}".format(trial, result, target)


    @unittest.skipIf(sys.version_info[0] < 3, 'python2 fails at concurrency')
    def test_en_us_auto(self):
        """Test many (valid) inputs sampled from a wide range.
        Inputs are created by num2word.
        """
        def inv_test(n):
            words = num2words(n)
            result = words2num(words)
            assert n == result,\
                   "{0} ({1}) inverted as {3}".format(n, words, result)

        _step = 64
        for start_i in random.sample(range(9999999999999), 64):
            plist = [Process(target=inv_test, args=(n,))\
                     for n in range(start_i, start_i + _step)]
            for p in plist:
                p.start()
            for p in plist:
                p.join()


    def test_en_us_neg(self):
        """Test invalid en-US input.
        Ensure that invalid number sequences raise NumberParseException.
        """
        tests = ("one one",
            "one one one",
            "one one one one",
            "one one one one one",
            "one million one hundred one one",
            "one thousand one million one",
            "one thousand hundred million",
            "twenty-zero",
            "a million billion thousand",
            "one point one one million one one",
            "four four point five",
            "one point thousand",
            "one point two point three",
            "one point point two",
            "eleven thousand point two hundred",
            "one point",
            "two thousand point",
            "a five hundred",
            "a six thousand",
            "six thousand a hundred and twenty",
            "nineteen twenty")

        for test in tests:
            try:
                value = words2num(test)
                assert False,\
                       "parsed invalid input '{0}' as {1}".format(test, value)
            except NumberParseException:
                pass
            except ValueError:
                pass


if __name__ == '__main__':
    unittest.main()
