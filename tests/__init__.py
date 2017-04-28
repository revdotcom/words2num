import unittest
import words2num


class TestITN(unittest.TestCase):
    """Test inverse text normalization for numbers.
    """

    def test_lang(self):
        """Test multi-lang handling of words2num.
        """
        try:
            words2num.w2n(None, lang='123')
            assert False, "exception not raised for invalid language"
        except NotImplementedError:
            pass

        try:
            words2num.w2n("ninety", lang='en_TEST')
        except NotImplementedError:
            assert False, "no default fallback for region-specified language"



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
