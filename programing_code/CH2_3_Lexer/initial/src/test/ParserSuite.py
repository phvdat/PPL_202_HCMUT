import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int a[10]"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """float goo (float a, b) {
        return 1 - foo(1, a, b);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))