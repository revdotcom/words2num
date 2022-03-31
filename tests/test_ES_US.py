import unittest
import random
import sys
from multiprocessing import Process
from words2num import words2num, NumberParseException
from num2words import num2words


class TestES_US(unittest.TestCase):
    """Test inverse text normalization for numbers.
    """

    def test_es_us(self):
        """Test valid es-US input.
        """
        test_trials = ("dos",
            "doce",
            "cero",
            "ciento dos",
            "ciento veintitrés",
            "mil ciento uno",
            "tres mil cuatrocientos cincuenta y seis",
            "doscientos mil trescientos cuarenta y cinco",
            "dos millones trescientos mil cuatro",
            "sesenta y ocho billones doscientos dos millones dos",
            "nueve trillones ochocientos siete",
            "noventa y nueve punto nueve",
            "noventa y nueve punto nueve nueve nueve nueve nueve nueve nueve seis",
            "quince punto cuatro",
            "dos mil punto cinco",
            "once millones punto tres tres",
            "un billón punto seis cuatro",
            "seiscientos punto nueve nueve",
            "uno punto cero cero cuatro",
            "cero punto cinco",
            "cuatro punto cero",
            "nueve punto cero nueve",
            "punto ocho ocho",
            "punto cero cero cinco",
            "mil cincuenta y cuatro",
            "trescientos sesenta",
            "cuatrocientos doce",
            "trescientos sesenta y cinco")
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
            result = words2num(trial, 'es_US')
            assert result == target,\
                   "'{0}' -> {1} != {2}".format(trial, result, target)


    @unittest.skipIf(sys.version_info[0] < 3, 'python2 fails at concurrency')
    def test_en_us_auto(self):
        """Test many (valid) inputs sampled from a wide range.
        Inputs are created by num2word.
        """
        def inv_test(n):
            words = num2words(n)
            result = words2num(words, 'es_US')
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


    def test_es_us_neg(self):
        """Test invalid es-US input.
        Ensure that invalid number sequences raise NumberParseException.
        """
        tests = ("uno uno",
            "uno uno uno",
            "uno uno uno uno",
            "uno uno uno uno uno",
            "millón ciento uno uno",
            "mil millón uno",
            "veinte cero",
            "uno punto uno uno millón uno uno",
            "cuatro cuatro punto cinco",
            "uno punto mil",
            "uno punto dos punto tres",
            "uno punto punto dos",
            "once mil punto doscientos",
            "uno punto",
            "dos mil punto",
#            "uno quinientos",
            "uno seis mil",
            "dieceinueve veinte")

        for test in tests:
            try:
                value = words2num(test, 'es_US')
                assert False, f"parsed invalid input '{test}' as {value}"
            except NumberParseException:
                pass
            except ValueError:
                pass


if __name__ == '__main__':
    unittest.main()
