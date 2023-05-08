import unittest
import sys

version_python = sys.version

class MyTestCase(unittest.TestCase):

    @unittest.skip("skip à l'aide de décorateurs")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(version_python < "3.10",
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the lib
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass