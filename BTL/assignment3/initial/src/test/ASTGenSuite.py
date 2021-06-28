import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
        Function main(){
            Let a[2, 3];
            a[1] = [[4, 5, 6], [1, 2, 3]];
            b = 100;
        }
        """
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    
   
        