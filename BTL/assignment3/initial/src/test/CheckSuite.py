# Pham Van Dat
# 1811892
import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
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
            a[1] = [1,2,3,4,5];
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
            Call(printLn, ["Pham Van Dat"]);
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
            Call(printLn, ["HCMUT"]);
            a = 10;
        }"""
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_diff_numofparam_stmt2(self):
        """Complex program 422"""
        input = """Function main() {
            Call(printLn, [5]);
            Let a = 10;
        }"""
        expect = "Type Mismatch In Statement: CallStmt(Id(printLn),[NumberLiteral(5.0)])"
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
        """ Test 440 """
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

    def test_for_statement41(self):
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
            For i In ["1", "2", "3"] {
                Call(printLn, [i]);
            }
            Call(printLn, [i]);
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
                Call(printLn, [ key +. a{"key"}]);
            }
            Call(printLn, [ key +. a{"key"}]);

            Return 0;
        }
        """
        expect = "Undeclared Identifier: key"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_456(self):
        """ Test 56 """
        input = """
        Function main(){
            Let a[5] =[1, 2, 3, 4, 5];
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
            If(True){
                Call(printLn, ["Back khoa"]);
            }
            Elif(!a){
                Call(printLn, ["Kinh Te"]);
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
            Return 0;
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
            Return 0;
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

    def test_461(self):
        """ Test 461 """
        input = """
        Let x:Number;
        Function main(a[5], i) {
            Let x;
            While (i < 5) {
                x = "HCMUT";
            }
            x = "Pham VD";
            Return u;
        }
        """
        expect = "Undeclared Identifier: u"
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_462(self):
        """ Scope """
        input = """
        Let x:Number;
        Function main(a[5], i) {
            Let x;
            While (i < 5) {
                x = "HCMUT";
                If(True){
                    a[2] = x;
                    a[2] = 10;

                }
            }
            x = "Pham VD";
            Return u;
        }
        """
        expect = "Type Mismatch In Statement: Assign(ArrayAccess(Id(a),[NumberLiteral(2.0)]),NumberLiteral(10.0))"
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_463(self):
        """ Scope """
        input = """
        Let x:Number;
        Function main(a[5], i) {
            Let x;
            While (i < 5) {
                x = "HCMUT";
                For j In a{
                    Let a = x;
                    Let j;

                }
            }
            x = "Pham VD";
            Return u;
        }
        """
        expect = "Redeclared Variable: j"
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_464(self):
        """ Scope """
        input = """
        Let a:Number = [1,2,3,4];
        Function foo(){
            Return a;
        }
        Function main(a[5], i) {
            Let x;
            While (i < 5) {
                x = "HCMUT";
                For j In Call(foo, []){
                    Let a = x;
                    Let j;

                }
            }
            x = "Pham VD";
            Return u;
        }
        """
        expect = "Redeclared Variable: j"
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test_464(self):
        """ Scope """
        input = """
        Let a = {name: "Pham", age:21};
        Function foo(){
            Return a;
        }
        Function main(a[5], i) {
            Let x;
            While (i < 5) {
                x = "HCMUT";
                For j In Call(foo, []){
                    Let a = x;
                    Let j;

                }
            }
            x = "Pham VD";
            Return u;
        }
        """
        expect = "Type Mismatch In Statement: ForIn(Id(j),CallExpr(Id(foo),[]),[VarDecl(Id(a),NoneType,Id(x)),VarDecl(Id(j),NoneType)])"
        self.assertTrue(TestChecker.test(input,expect,464))
    

    def test65(self):
        input="""
            Function foo(a,b)
            {
                Let c;
                For i In [1,10] {
                    c = Call(foo,[c,a]);
                }
                Return -1;
            }
            Function main()
            {
                Let z;
                z = Call(foo, [1,2]) + Call(foo, [True, False]);
            }
        """
        expect=str(TypeCannotBeInferred(Assign(Id('c'),CallExpr(Id('foo'),[Id('c'),Id('a')]))))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test66(self):
        input = """
            Function foo(a)
            {
                Return;
            }
            Function main()
            {
                Let y, a, x;
                y = a + Call(foo, [x]);
            }
        """
        expect = str(TypeCannotBeInferred(BinaryOp('+',Id('a'),CallExpr(Id('foo'),[Id('x')]))))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test67(self):
        input = """
            Let a, b;
            Function foo(x,y,z)
            {
                Return;
            }
            Function main()
            {
                Let b = 1;
                If (b ==. "John") { 
                    Return a; 
                }
                Call(foo,[1,2,3]);
            }
        """
        expect = str(TypeMismatchInExpression(BinaryOp('==.',Id('b'),StringLiteral('John'))))
        self.assertTrue(TestChecker.test(input, expect, 467))


    def test_468(self):
        """Simple program: main"""
        input = """
        Let x, y, z:Number;
        Constant $x=2;
        Function foo(a){
        }
        Function main() {
            If(Call(foo,[x])){

            }
        }
        """
        expect = str(TypeCannotBeInferred(If([(CallExpr(Id("foo"),[Id("x")]),[])],[])))
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        """Simple program: main"""
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
                    a = 10;
                }
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        """Simple program: main"""
        input = """
        Let x, y, z:Number;
        Constant $x=2;
        Function foo(a){
            Return True;
        }
        Function foo1(a){
            Return;
        }
        Function main() {
            While(Call(foo,[z])){
                While(Call(foo,[x])){
                    While(Call(foo1,[y])){
                        Return;
                    }
                }
            }
        }
        """
        expect = "Type Cannot Be Inferred: While(CallExpr(Id(foo1),[Id(y)]),[Return()])"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        """Simple program: main"""
        input = """
        Let x[5], y, z:Number;
        Constant $x=2;
        Function foo(a){
            Return;
        }
        Function foo1(a){
            Return;
        }
        Function main() {
            For x Of {name: "Pham", age:21}{
                 While(Call(foo,[x])){
                     
                     }
            }
        }
        """
        expect = str(TypeCannotBeInferred( While(CallExpr(Id("foo"),[Id("x")]),[]) ))
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_d472(self):
        """Simple program: main"""
        input = """
        Let x:Number, y:JSON, z={ name: False};
        Constant $x=2;
        Function foo(a){
            a=2;
            Return 2;
        }
        Function main() {
            For x Of z {
                Let y=2;
                For d Of {name: "Pham", age:21} {
                    If(y){}
                 }
            }
        }
        """
        expect = str(TypeMismatchInStatement(
            If([(Id("y"),[])],[])
             ))
        self.assertTrue(TestChecker.test(input, expect, 472))

        
    def test_d473(self):
        """Simple program: main"""
        input = """
        Let a:Number;
        Function main() {
            Let b;
            If(True) {
                Let c;
                c = a;
            }
            c = b;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        """Simple program: main"""
        input = """
        Let x, y, z:Number;
        Constant $x=2;
        Function foo(a){
            a=2;
            Return True;
        }
        Function main() {
            While(Call(foo,[x])){
                 While(z){
                }
            }
        }
        """
        expect = str(TypeMismatchInStatement(While(Id("z"),[])))
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_75(self):
        """Simple program: main"""
        input = """
        Let x, y, z:Number;
        Constant $x=2;
        Function foo(a){
            a=2;
            Return True;
        }
        Function foo1(a){
            a=2;
            Return ;
        }
        Function main() {
            While(Call(foo,[x])){
                x=5;
                Let x:Boolean;
                x=Call(foo,[z]);
                x=2;
            }
        }
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),NumberLiteral(2.0))))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_76(self):
        """Simple program: main"""
        input = """
        Let x[5], y, z:Number;
        Constant $x=2;
        Function foo(a[5]){
            ##a=2;##
            Return True;
        }
        Function foo1(a){
            a=2;
            Return ;
        }
        Function main() {
            While(Call(foo,[x])){
                x[2]=5;
                Let x:JSON;
                x{"Name"}=3;
                x=2;
            }
        }
        """
        expect = str(TypeMismatchInStatement(
            Assign(Id("x"),NumberLiteral(2.0))
            ))
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        """Simple program: main"""
        input = """
        Let x, y, z:Number;
        Function main() {
            Call(print,[z]);
        }
        """
        expect = str(TypeMismatchInStatement(
            CallStmt(Id("print"),[Id("z")])
            ))
        self.assertTrue(TestChecker.test(input, expect, 477))


        def test_78(self):
            """Simple program: main"""
        input = """
        Let x[5,2], y, z:Boolean;
        Function foo(x){
            If(x){
                Return z;
            }
            Return x;
        }
        Function foo1(a[]){
        }
        Function main() {
            y=x[5,2,4];
        }
        """
        expect = str(TypeMismatchInExpression(\
            ArrayAccess(Id("x"),[NumberLiteral(5.0),NumberLiteral(2.0),NumberLiteral(4.0)])\
            ))
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        input = """
            Let x = 10.0;
            Function factorial(n)
            {
                If (n <= 1) {
                 Return n*Call(factorial,[n-1]);
                }
                Else {
                Return 1;
                } 
                
            }
            Function main()
            {
                Return Call(factorial,[]);
            }
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("factorial"),[])))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_80(self):
        """Simple program: main"""
        input = """
        Let x, y, z:Number;
        Constant $x=2;
        Function foo(a){
            a=2;
            Return True;
        }
        Function foo1(a){
            a=2;
            Return ;
        }
        Function main() {
            While(Call(foo,[x])){
                x=5;
                Let x:JSON;
                x={ name:"Pham", age:21};
                x{"age"}=3;
                x=2;
            }
        }
        """
        expect = str(TypeMismatchInStatement(
            Assign(Id("x"),NumberLiteral(2.0))
            ))
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        """ Scope """
        input = """
        Let a = {name: "Pham", age:21};
        Function foo(){
            Return [1, 2, 3];
        }
        Function main(a[5], i) {
            Let x;
            While (i < 5) {
                x = "HCMUT";
                For j In Call(foo, []){
                    Let a = x;
                    Let b:Boolean = a;

                }
            }
            x = "Pham VD";
            Return u;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),BooleanType,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_482(self):
        """ Scope """
        input = """
        Let a = {name: "Pham", age:21};
        Function foo(){
            Return True;
        }
        Function main(arr[5], i) {
            If(Call(foo, [])){
                Let a = True;
                If(a){
                    a = 100;
                }
            }
            Return u;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(a),NumberLiteral(100.0))"
        self.assertTrue(TestChecker.test(input,expect,482))


    def test_483(self):
        """ Scope """
        input = """
        Function main() {
            While(True){
                Let read = True;
                If(True){
                    Let c;
                }
            }
            Return u;
        }
        """
        expect = "Undeclared Identifier: u"
        self.assertTrue(TestChecker.test(input,expect,483))


    def test_484(self):
        """ Scope """
        input = """
        Let a;
        Function main() {
            Let a;
            For i In [1,2,3,4]{
                Let b;
                If(True){
                    Constant $c = 10;
                    While(True){
                        Let a;
                        a = 10;
                    }
                }
                b = 100;
                a = b;
            }
            a = "hcmut";
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(a),StringLiteral(hcmut))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_485(self):
        """ Scope """
        input = """
        Let a;
        Let b:String;
        Function main() {
            a = b;
            Let b:Number = a;
            
            Return a;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),NumberType,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        """Simple program: main"""
        input = """
        Let x;
        Let y;
        Constant $x:Number=2.0;
        Constant $x:Number=5.0;
        Function main() {
        }
        """
        expect = str(Redeclared(Constant(),"$x"))
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        """Simple program: main"""
        input = """
        Let x;
        Let y;
        Constant $x=2;
        Function foo(a,b,c,d,e,a){
        }
        Function main() {
        }
        """
        expect = str(Redeclared(Parameter(),"a"))
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        """Simple program: main"""
        input = """
        Let x;
        Constant $x=2;
        Function foo(a,b,c,d,e,x,y){
            a=True&&f;
        }
        Function main() {

        }
        """
        expect = str(Undeclared(Identifier(),"f"))
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        """Simple program: main"""
        input = """
        Let x;
        Constant $x=2;
        Function foo(a,b){
            a=f==2.3;
        }
        Function main() {
            Return;
        }
        """
        expect = str(Undeclared(Identifier(),"f"))
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        """Simple program: main"""
        input = """
        Let x;
        Constant $x=2;
        Function foo(a){
        }
        Function main() {
            If(x){
                Let k=$x;
            }
            Call(foo, [Call(foo, [k])] );
        }
        """
        expect = str(Undeclared(Identifier(),"k"))
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        """Simple program: main"""
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
                    Let m;
                }
            }
            Return m;
        }
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        """Simple program: main"""
        input = """
        Let x, y[5], z:Number;
        Constant $x=2;
        Function foo(a){
            a=2;
            Return 2;
        }
        Function main() {
            For x Of z {
            }
        }
        """
        expect = str(TypeMismatchInStatement(
            ForOf(Id("x"),Id("z"),[])
             ))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        """Simple program: main"""
        input = """
        Let x, y, z:Number;
        Constant $x=2;
        Function foo(a){
            a=2;
            Return True;
        }
        Function main() {
            While(Call(foo,[x])){
                 While(z){
                }
            }
        }
        """
        expect = str(TypeMismatchInStatement(While(Id("z"),[])))
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_94(self):
        """Simple program: main"""
        input = """
        Let x:Number, y:Boolean, z:String,t:JSON;
        Function foo(x){
            If(x){
                Return True;
            }
            Return x;
        }
        Function foo1(a[]){
        }
        Function main() {
            Let a,b;
            a=z==.z;
            b=a+.z;
        }
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("a"),Id("z"))))
        self.assertTrue(TestChecker.test(input, expect, 494))
    

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
            Call(printLn, []);
        }"""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function main() {
            Call(printLn, [Call(read, [10])]);
        }
        """
        expect = str(TypeMismatchInExpression(
            CallExpr(Id("read"), [NumberLiteral(10.0)])))
        self.assertTrue(TestChecker.test(input, expect, 497))


    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = """
        Function main() {
            Call(foo, []);
            Return a;
        }"""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input ="""
        Function main() {
            Call(printLn, [Call(read, [4.0])]);
            Return a;
        }
        """

        expect = str(TypeMismatchInExpression(
            CallExpr(Id("read"), [NumberLiteral(4.0)])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_no_entry_point1(self):
        """ Test 500 """
        input = """
        Function foo(a){
            Return [[1,2],[3,4]];
        }
        Function main(){
            Let a[2,2] = [[1,2],[3,4]];
            For i In a{
                i = 10;
            }
            Return 0;
        }
        """
        expect = "Type Mismatch In Statement: Assign(Id(i),NumberLiteral(10.0))"
        self.assertTrue(TestChecker.test(input,expect,500))
