# Pham Van Dat
# 1811892
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

    def test_id_undeclared3(self):
        """ Undeclared Identifier """
        input = """
        Function main(){
            Let a:String = "Pham";
            Let b:Number;
            b = a +. "Dat";
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(b),BinaryOp(+.,Id(a),StringLiteral(Dat)))"
        self.assertTrue(TestChecker.test(input,expect,410))

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

 
    def test_while_statemnt1(self):
        """ Test 430 """
        input = """
        Function main(){
            Let a:Boolean;
            While(a){
                Constant $c=10;
                Break;
            }
            Let x:String;
            x = a;
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(x),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_while_statemnt2(self):
        """ Test 431 """
        input = """
        Function main(){
            Let a;
            While(1 < 2){
                a = "hcmut";
                Break;
            }
            a = 100;
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(a),NumberLiteral(100.0))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_while_statemnt3(self):
        """ Test 432 """
        input = """
        Let a;
        Function foo() {
            Let a;
            a = 100;
            Return;
        }        
        Function main() {
            a = "hcmut";
            b =10;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_while_statement4(self):
        """ Test 433 """
        input = """
        Function main(){
            Let a;
            While(1 < 2){
                Let a;
                Constant $z = 10;
                a = "hcmut";
                Break;
            }
            a = 100;
            b = "Pham";
            Return 0;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_for_statement1(self):
        """ Test 434 """
        input = """
        Function main(){
            Let a;
            Let arr[5];
            For i In arr{
                a = a + 1;
            }
            a = "hoa no khong mau";
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(a),StringLiteral(hoa no khong mau))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_for_statement2(self):
        """ Test 435 """
        input = """
        Function main(){
            Let a;
            Let arr:Number;
            For i In arr{
                a = a + 1;
            }
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: ForIn(Id(i),Id(arr),[Assign(Id(a),BinaryOp(+,Id(a),NumberLiteral(1.0)))])"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_for_statement3(self):
        """ Test 436 """
        input = """
        Function main(){
            Let a;
            Let arr:Number;
            For i Of arr{
                a = a + 1;
            }
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: ForOf(Id(i),Id(arr),[Assign(Id(a),BinaryOp(+,Id(a),NumberLiteral(1.0)))])"
        self.assertTrue(TestChecker.test(input,expect,436))
    
    def test_for_statement4(self):
        """ Test 435 """
        input = """
        Function main(){
            Let a;
            Let json[];
            For i Of json{
                a = a + 1;
            }
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: ForOf(Id(i),Id(json),[Assign(Id(a),BinaryOp(+,Id(a),NumberLiteral(1.0)))])"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_for_statement5(self):
        """ Test 438 """
        input = """
        Function main(){
            Let a;
            Let json = {name: "Pham", age:21};
            For i Of json{
                a = a + 1;
            }
            Let b:Boolean;
            b =  a;
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_for_statement6(self):
        """ Test 438 """
        input = """
        Function main(){
            Let a;
            For i Of {name: "Pham", age:21}{
                a = a + 1;
            }
            Let b:Boolean;
            b =  a;
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_for_statement7(self):
        """ Test 441 """
        input = """
        Function main(){
            Let a;
            For i In [1,2,3,4]{
                a = a + i;
            }
            a = "a walk to remember";
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(a),StringLiteral(a walk to remember))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_for_statement8(self):
        """ Test 441 """
        input = """
        Function main(){
            Let a = {
                name: "Yanxi Place",
                address: "Chinese Forbidden City"
            };
            For key Of a {
                key = 10;
            }
            key = "Name";
            Return 0;
        }
        """
        expect = "Undeclared Identifier: key"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_442(self):
        """ Test """
        input = """
        Function main(){
            Let a= True;
            Let b:Number;
            Let c;
            c = a && b;
            Return c;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_443(self):
        """ Test """
        input = """
        Function main(){
            Let a;
            a= 3+ True;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,NumberLiteral(3.0),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_444(self):
        """ Test """
        input = """
        Function main(){
            Let a;
            a= (a + 3.4) * (a -2);
            b = a;
            Return b;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_445(self):
        """ Test """
        input = """
        Function main(){
            Let x, y, z;
            z = ((x-3)>(-y)) && (!y);
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(y))"
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_446(self):
        """ Test """
        input = """
        Function main(){
            Let x, y, z;
            z = ((x-3)>(-y)) && (!y);
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(y))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_447(self):
        """ Test """
        input = """
        Function main(){
            Let x, y, z;
            x = (x&&y) || ( False || (z ==. "any_string"));
            z = x;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(z),Id(x))"
        self.assertTrue(TestChecker.test(input,expect,447))

    
    def test_448(self):
        """ Test """
        input = """
        Function main(){
            Let x, y, z:String;
            x = y + z + 10;
            Return x;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(y),Id(z))"
        self.assertTrue(TestChecker.test(input,expect,448))

        
    def test_449(self):
        """ Test """
        input = """
        Function main(){
            Let x, y, z:String;
            x = y || 10;
            Return x;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(y),NumberLiteral(10.0))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_450(self):
        """ Test """
        input = """
        Function main(){
            Let x, y, z:String;
            x = y || z;
            Return x;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(y),Id(z))"
        self.assertTrue(TestChecker.test(input,expect,450))    

    def test_451(self):
        """ Test """
        input = """
        Function main(){
            Let x, y, z:String;
            x = y +. z;
            Let a:Number = x;
            Return a;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),NumberType,Id(x))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_452(self):
        """ Test """
        input = """
        Function main(){
            Let x, y, z:String;
            x = (z +. "string") + y;
            Let a:Number = x;
            Return a+x;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(+.,Id(z),StringLiteral(string)),Id(y))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_for_statement8(self):
        """ Test 453 """
        input = """
        Function main(){
            Let a = {
                name: "Yanxi Place",
                address: "Chinese Forbidden City"
            };
            For key Of a {
                Let temp = key +. "Sai Gon";
            }
            key = "Name";
            Return 0;
        }
        """
        expect = "Undeclared Identifier: key"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_for_in(self):
        """ Test 454 """
        input = """
        Function main(){
            For i In [1, 2, 3] {
                Call(printSLn, [i]);
            }
            Call(printSLn, [i]);
            Return 0;
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,454))


    def test_for_of(self):
        """ Test 455 """
        input = """
        Function main(){
            Let a = {
                add: "Sai Gon",
                year: 2021
            };
            For key Of a {
                Call(printSLn, [ key +. a{"key"}]);
            }
            Call(printSLn, [ key +. a{"key"}]);

            Return 0;
        }
        """
        expect = "Undeclared Identifier: key"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_456(self):
        """ Test 56 """
        input = """
        Function main(){
            Let a =[1, 2, 3, 4, 5];
            Let b = {name: "Pham", age:21};
            a = b;
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_if457(self):
        """ Test 57 """
        input = """
        Function main(){
            Let a:Boolean;
            If(a){
                Call(printSLn, ["Back khoa"]);
            }
            Elif(!a){
                Call(printSLn, ["Kinh Te"]);
            }
            Else{
                Return b;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_ifstatement458(self):
        """ Test 430 """
        input = """
        Function main(){
            Let a:Boolean;
            Let b:Boolean;
            If(a){
                Let c= 100;
            }
            Elif(b){
                Let d = 10;
            }
            Else{
                Constant $e = "Pham";
            }
            Let x:String;
            x = a;
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(x),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,458))
        
    def test_ifstatement459(self):
        """ Test 430 """
        input = """
        Function main(){
            Let a:Number;
            If(a){
                Let c= 100;
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),[VarDecl(Id(c),NoneType,NumberLiteral(100.0))])"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_while_if(self):
        """ Test 460 """
        input = """
        Function main(a[5], b) {
            Let i = 0;
            While (i < 5) {
                a[i] = b + 1;
                Let u: Number = 1;
                If (a[u] == 10) {
                    Return a[i];
                }
            }
            Return u;
        }
        """
        expect = "Undeclared Identifier: u"
        self.assertTrue(TestChecker.test(input,expect,460))


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

