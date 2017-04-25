import unittest
import word2num


class TestITN(unittest.TestCase):
    """Test inverse text normalization for numbers.
    """

    def test_failure(self):
        """Test error handling of word2num.
        """
        test_trials = ("1", "frogess", "telepromptx", "**", "-", "0", "sixes")

        for trial in test_trials:
            try:
                word2num.word2num(trial)
                assert False, "exception not raised for: {0}".format(trial)
            except word2num.NumberParseException:
                pass


    def test_en_us(self):
        """Test valid en-US input.
        """
        test_trials = ("two",
            "twelve",
            "one hundred and two",
            "a hundred twenty-three",
            "thirty-four hundred fifty-six",
            "two hundred thousand, three hundred forty five",
            "twenty-three hundred thousand four",
            "sixty-eight billion, two hundred two million and two",
            "sixty eight billion two hundred two million two",
            "nine trillion eight hundred seven")
        test_targets = (2,
            12,
            102,
            123,
            3456,
            200345,
            2300004,
            68202000002,
            68202000002,
            9000000000807)
        tests = zip(test_trials, test_targets)

        for (trial, target) in tests:
            assert word2num.word2num(trial) == target,\
                   "failed to parse '{0}' as {1}".format(trial, target)


    def test_en_us_neg(self):
        """Test invalid en-US input.
        """
        tests = ("seven eleven",
            "one one",
            "one one one",
            "one one one one",
            "one one one one one",
            "one million one hundred one one",
            "one thousand one million one",
            "one thousand hundred million")

        for test in tests:
            try:
                value = word2num.word2num(test)
                assert False,\
                       "parsed invalid input '{0}' as {1}".format(test, value)
            except word2num.NumberParseException:
                pass


if __name__ == '__main__':
    unittest.main()
