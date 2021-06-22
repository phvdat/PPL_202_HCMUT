import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
        Function main() {
            Call(printStrLn, [Call(read, [4])]);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],[CallStmt(Id("printStrLn"),[CallExpr(Id("read"),[NumberLiteral(4.0)])])])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    
   