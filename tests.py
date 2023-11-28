import unittest
from greetings_tests import *
from basic_info_tests import *

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = unittest.TestSuite()

    tests.addTest(loader.loadTestsFromTestCase(greetingsTest))
    tests.addTest(loader.loadTestsFromTestCase(basicInfoTest))

    runner = unittest.TextTestRunner()
    runner.run(tests)