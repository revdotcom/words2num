import unittest
import words2num


class TestITN(unittest.TestCase):
    """Test inverse text normalization for numbers.
    """

    def test_failure(self):
        """Test error handling of words2num.
        Make sure that invalid strings raise value errors.
        """
        test_trials = ("1", "frogess", "telepromptx", "**", "-", "0", "sixes")

        for trial in test_trials:
            try:
                words2num.w2n(trial)
                assert False, "exception not raised for: {0}".format(trial)
            except ValueError:
                pass


if __name__ == '__main__':
    unittest.main()
