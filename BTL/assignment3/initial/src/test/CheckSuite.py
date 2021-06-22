import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_no_entry_point1(self):
        """ No Entry Point """
        input = """
        Function main1(){
            Let a;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_no_entry_point2(self):
        """ No Entry Point """
        input = """
        Function main1(){
            Let a;
        }
        Function main2(){
            Let a;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))


    def test_redeclare_global_var1(self):
        """ Global Variable Redeclared """
        input = """
        Let a = 10;
        Let a: Boolean;
        Function main(){
            Let a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclare_global_var2(self):
        """ Global Variable Redeclared3 """
        input = """
        Let a:Number;
        Let a;
        Function main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclare_func1(self):
        """ Function Redeclared """
        input = """
        Let a:Number = "string";
        Function main(){}
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),NumberType,StringLiteral(string))"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_undeclared_function5(self):
        """Simple program: main 5"""
        input = """Function main() {
            Let x =10;
            Let x;
        }
        """
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclare_param1(self):
        """ Parameter Redeclared """
        input = """
        Function main(a, a){}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclare_param2(self):
        """ Parameter Redeclared """
        input = """
        Function main(a, b){
            Constant $c = 10;
            Constant $c = 11;
        }
        """
        expect = "Redeclared Constant: $c"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_id_undeclared1(self):
        input = """
        Function main($a, $a){
            Constant $c = 10;
            Constant $d = "string";
        }
        """
        expect = "Redeclared Parameter: $a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_id_undeclared2(self):
        """ Undeclared Identifier """
        input = """
        Function main(){
            a = a + 1;
            a = a - b;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    # def test_id_undeclared3(self):
    #     """ Undeclared Identifier """
    #     input = """
    #     Function main(){
    #         Let a[1.0,3.0]:String;
    #         a[2] = 10.0;
    #         a = [];
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Assign(Id(a),NumberLiteral(10.0))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    def test_func_undeclared1(self):
        """ Undeclared Function 411"""
        input = """
        Function main(){
            Let a:Number;
            Let b="string";
            a = b;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_func_undeclared2(self):
        """ Undeclared Function 412"""
        input = """
        Function main(){
            Let b="string";
            a = b;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_func_undeclared3(self):
        """ Undeclared Function 413 """
        input = """
        Function main(){
            Let a;
            Let b;
            c = Call(sum, []);
        }
        """
        expect = "Undeclared Function: sum"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_func_undeclared14(self):
        """ Test 414 """
        input = """
        Function main(){
            Let a[10]:Number = [1, 2, 3];
            Let b;
            Let a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,414))



    def test_redeclare_func2(self):
        """ Function Redeclared """
        input = """
        Function main(){
            Let a:String = "100";
            Let a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_func_undtest_eclared6(self):
        """ Test 416 """
        input = """
        Function main(){
            Let a[2, 3];
            a[1] = 10;
            b = 100;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,416))


    def test_func_undeclared7(self):
        """ Test 417 """
        input = """
        Function main(){
            Let a:String = {name: "Pham", age:21};
            Let a;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,JSONLiteral((Key=Id(name),Value=StringLiteral(Pham)),(Key=Id(age),Value=NumberLiteral(21.0)))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_func_undeclared8(self):
        """ Test 418 """
        input = """
        Function main(){
            Let a = {name: "Pham", age:21};
            Let a;
            Return;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,418))    
    
    def test_redeclare_global_var94(self):
        """ Global Variable Redeclared """
        input = """
        Function main(){
            Let a:Number = 100;
            Let a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclared_function1(self):
        """Simple program: main 420"""
        input = """
        Function foo(){
            Call(printSLn, ["Pham Van Dat"]);
            Return;
        }
        Function main() {
            Call(foo, []);
            Call(foo2, [2]);
            
        }
        """
        expect = str(Undeclared(Function(), "foo2"))
        self.assertTrue(TestChecker.test(input, expect, 420))


    def test_diff_numofparam_stmt1(self):
        """Complex program 421"""
        input = """Function main() {
            Call(printSLn, ["HCMUT"]);
            a = 10;
        }"""
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_diff_numofparam_stmt2(self):
        """Complex program 422"""
        input = """Function main() {
            Call(printSLn, [5]);
            Let a = 10;
        }"""
        expect = "Type Mismatch In Statement: CallStmt(Id(printSLn),[NumberLiteral(5.0)])"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        """More complex program 423"""
        input = """Function main() {
            Call(printStrLn, [Call(read, [4])]);
        }
        """
        expect = str(TypeMismatchInExpression(
                CallExpr(Id("read"), [NumberLiteral(4.0)])))
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_function_local_variable(self):
        """More complex program test"""
        input = """
        Function foo(a, b){
            Let c:Number;
            c = a;
        }
        Function main() {
            Call(printStrLn, [Call(read, [4])]);
        }
        """
        expect = str(TypeMismatchInExpression(
                CallExpr(Id("read"), [NumberLiteral(4.0)])))
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        """More complex program test"""
        input = """
        Let x;
        Function foo(a, b){
            Let c:Number;
            c = a;
            a = x;
        }
        Function main() {
            x = "back khoa";
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(x),StringLiteral(back khoa))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        """More complex program test"""
        input = """
        Let x;
        Function foo(x, b){
            x = 10;
        }
        Function main() {
            x = "back khoa";
            c = 10;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 426))

    
    def test_427(self):
        """More complex program test"""
        input = """
        Let x;
        Function foo(x, b){
            x = "string";
            Return b;
        }
        Function main() {
            Let c;
            x = 10 + Call(foo, [c,3]);
            c = 10;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(c),NumberLiteral(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        """More complex program test"""
        input = """
        Let x;
        Function foo(x, b){
            x = "string";
            Return "HCMUT";
        }
        Function main() {
            Let c;
            x = 10 + Call(foo, [c,3]);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,NumberLiteral(10.0),CallExpr(Id(foo),[Id(c),NumberLiteral(3.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_func_undtest_eclared29(self):
        """ Test 416 """
        input = """
        Function main(){
            Let a = {name: "Pham", age:21};
            a{"name"} = 10;
            b = 100;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,429))

 

    def test_ifstatement1(self):
        """ Test 430 """
        input = """
        Function main(){
            Let a;
            Let b;
            if(a){
                Let c= 100;
            }
            elif(b){
                Let d = 10;
            }
            else{
                Constant $e = "Pham";
            }
            Let x:String;
            x = a
            return 0;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,430))






































    # test case của thầy

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function main() {
            Call(foo, []);
        }
        """
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function main() {
            Call(printSLn, []);
        }"""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printSLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 496))

    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function main() {
    #         Call(printStrLn, [Call(read, [10])]);
    #     }
    #     """
    #     expect = str(TypeMismatchInExpression(
    #         CallExpr(Id("read"), [NumberLiteral(10)])))
    #     self.assertTrue(TestChecker.test(input, expect, 497))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"), [], ([], [
    #         CallExpr(Id("foo"), [])]))])
    #     expect = str(Undeclared(Function(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 498))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #         FuncDecl(Id("main"), [], ([], [
    #             CallStmt(Id("printSLn"), [
    #                 CallExpr(Id("read"), [NumberLiteral(4.0)])
    #             ])]))])
    #     expect = str(TypeMismatchInExpression(
    #         CallExpr(Id("read"), [NumberLiteral(4.0)])))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #         FuncDecl(Id("main"), [], ([], [
    #             CallStmt(Id("printStrLn"), [])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 500))