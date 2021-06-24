import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
        Let x, y, z:Number;
        Constant $x=2;
        Function foo(a){
        }
        Function foo1(a){
        }
        Function main() {
            If(Call(foo,[z])){
            }
            Elif(x){
            }
            Else{
                If(Call(foo1,[x])){

                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    
   
        