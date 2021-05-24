from main.csel.utils.AST import ArrayAccess, ArrayLiteral, BinaryOp, BooleanLiteral, CallStmt, ForIn, FuncDecl, JSONAccess, JSONLiteral, JSONType, NumberLiteral, NumberType, StringLiteral, VarDecl
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_var_1(self):
        """Simple program: int main() {} """
        input = """Let x:Number;"""
        expect = Program([VarDecl(Id("x"), None, NumberType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))
    def test_var_2(self):
        """Simple program: int main() {} """
        input = """Let x=5;"""
        expect = Program([VarDecl(Id("x"), None, NoneType(), NumberLiteral(float(5)))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))
    def test_var_3(self):
        """Simple program: int main() {} """
        input = """Let x=True;"""
        expect = Program([VarDecl(Id("x"), None, NoneType(), BooleanLiteral("True"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))
    def test_var_4(self):
        """Simple program: int main() {} """
        input = """Let x:String="5";"""
        expect = Program([VarDecl(Id("x"), None, StringType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))
    def test_var_5(self):
        """Simple program: int main() {} """
        input = """Let x=[True,1,[2,5]];"""
        expect = Program([VarDecl(Id("x"), None, NoneType(), ArrayLiteral([BooleanLiteral("True"),NumberLiteral(float(1)),ArrayLiteral([NumberLiteral(float(2)),NumberLiteral(float(5))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))
    def test_var_6(self):
        """Simple program: int main() {} """
        input = """Let x[2]="5";"""
        expect = Program([VarDecl(Id("x"), [NumberLiteral(float(2))], NoneType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))
    def test_var_7(self):
        """Simple program: int main() {} """
        input = """Let x[3,2]=[True,1,[2,5]];"""
        expect = Program([VarDecl(Id("x"), [NumberLiteral(float(3)),NumberLiteral(float(2))], NoneType(), ArrayLiteral([BooleanLiteral("True"),NumberLiteral(float(1)),ArrayLiteral([NumberLiteral(float(2)),NumberLiteral(float(5))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))
    def test_var_8(self):
        """Simple program: int main() {} """
        input = """Let x:String="5";"""
        expect = Program([VarDecl(Id("x"), None, StringType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))
    def test_var_9(self):
        """Simple program: int main() {} """
        input = """Let x:String="5",y;"""
        expect = Program([VarDecl(Id("x"), None, StringType(), StringLiteral("5")),VarDecl(Id("y"),None,NoneType(),None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))
    def test_var_10(self):
        """Simple program: int main() {} """
        input = """Let x[3,2]={name:"hao",age:21};"""
        expect = Program([VarDecl(Id("x"), [NumberLiteral(float(3)),NumberLiteral(float(2))], NoneType(), JSONLiteral([(Id("name"),StringLiteral("hao")),(Id("age"),NumberLiteral(21.0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))
    def test_const_1(self):
        """Simple program: int main() {} """
        input = """Constant $x:Number=5;"""
        expect = Program([ConstDecl(Id("$x"), None, NumberType(), NumberLiteral(float(5)))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))
    def test_const_2(self):
        """Simple program: int main() {} """
        input = """Constant $x=5;"""
        expect = Program([ConstDecl(Id("$x"), None, NoneType(), NumberLiteral(float(5)))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))
    def test_const_3(self):
        """Simple program: int main() {} """
        input = """Constant $x=True;"""
        expect = Program([ConstDecl(Id("$x"), None, NoneType(), BooleanLiteral("True"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))
    def test_const_4(self):
        """Simple program: int main() {} """
        input = """Constant $x:String="5";"""
        expect = Program([ConstDecl(Id("$x"), None, StringType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))
    def test_const_5(self):
        """Simple program: int main() {} """
        input = """Constant $x=[True,1,[2,5]];"""
        expect = Program([ConstDecl(Id("$x"), None, NoneType(), ArrayLiteral([BooleanLiteral("True"),NumberLiteral(float(1)),ArrayLiteral([NumberLiteral(float(2)),NumberLiteral(float(5))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))
    def test_const_6(self):
        """Simple program: int main() {} """
        input = """Constant $x[2]="5";"""
        expect = Program([ConstDecl(Id("$x"), [NumberLiteral(float(2))], NoneType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))
    def test_const_7(self):
        """Simple program: int main() {} """
        input = """Constant $x[3,2]=[True,1,[2,5]];"""
        expect = Program([ConstDecl(Id("$x"), [NumberLiteral(float(3)),NumberLiteral(float(2))], NoneType(), ArrayLiteral([BooleanLiteral("True"),NumberLiteral(float(1)),ArrayLiteral([NumberLiteral(float(2)),NumberLiteral(float(5))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))
    def test_const_8(self):
        """Simple program: int main() {} """
        input = """Constant $x:String="5";"""
        expect = Program([ConstDecl(Id("$x"), None, StringType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
    def test_const_9(self):
        """Simple program: int main() {} """
        input = """Constant $x:String="5",$y=[2,1];"""
        expect = Program([ConstDecl(Id("$x"), None, StringType(), StringLiteral("5")),ConstDecl(Id("$y"),None,NoneType(),ArrayLiteral([NumberLiteral(float(2)),NumberLiteral(float(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))
    def test_const_10(self):
        """Simple program: int main() {} """
        input = """Constant $x[3,2]:JSON={name:"hao",age:21};"""
        expect = Program([ConstDecl(Id("$x"), [NumberLiteral(float(3)),NumberLiteral(float(2))], JSONType(), JSONLiteral([(Id("name"),StringLiteral("hao")),(Id("age"),NumberLiteral(21.0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))
    def test_func_1(self):
        """Simple program: int main() {} """
        input = """Function x(){ }"""
        expect = Program([FuncDecl(Id("x"),[],[])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))
    def test_func_2(self):
        """Simple program: int main() {} """
        input = """Function x(a){ }"""
        expect = Program([FuncDecl(Id("x"),[VarDecl(Id("a"),None,NoneType(),None)],[])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))
    def test_func_3(self):
            """Simple program: int main() {} """
            input = """Function x(a,b){ }"""
            expect = Program([FuncDecl(Id("x"),[VarDecl(Id("a"),None,NoneType(),None),VarDecl(Id("b"),None,NoneType(),None)],[])])
            self.assertTrue(TestAST.checkASTGen(input, expect, 323))
    def test_func_4(self):
            """Simple program: int main() {} """
            input = """Function x(a[]){ }"""
            expect = Program([FuncDecl(Id("x"),[VarDecl(Id("a"),[],NoneType(),None)],[])])
            self.assertTrue(TestAST.checkASTGen(input, expect, 324))
    def test_func_5(self):
            """Simple program: int main() {} """
            input = """Function x(a[],b[5,6],y){ }"""
            expect = Program([FuncDecl(Id("x"),[VarDecl(Id("a"),[],NoneType(),None),VarDecl(Id("b"),[NumberLiteral(float(5)),NumberLiteral(float(6))],NoneType(),None),VarDecl(Id("y"),None,NoneType(),None)],[])])
            self.assertTrue(TestAST.checkASTGen(input, expect, 325))
    def test_func_6(self):
            """Simple program: int main() {} """
            input = """Function x(a[],b[5,6],y){
                Let z:String=5;
            }"""
            expect = Program([FuncDecl(Id("x"),[VarDecl(Id("a"),[],NoneType(),None),VarDecl(Id("b"),[NumberLiteral(float(5)),NumberLiteral(float(6))],NoneType(),None),VarDecl(Id("y"),None,NoneType(),None)],[VarDecl(Id("z"),None,StringType(),NumberLiteral(float(5)))])])
            self.assertTrue(TestAST.checkASTGen(input, expect, 326))
    def test_func_8(self):
        """Simple program: int main() {} """
        input = """Function main() {
                    a[5, 3] = 5;
                }"""
        expect = Program([FuncDecl(Id("main"),[],[Assign(ArrayAccess(Id("a"),[NumberLiteral(5.0),NumberLiteral(3.0)]),NumberLiteral(5.0))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
    def test_func_7(self):
        """Simple program: int main() {} """
        input = """
        Let a=5;
        Function x(a,b){
            Let z:String=5;
            Constant $a=5;
         }"""
        expect = Program([VarDecl(Id("a"),None, NoneType(),NumberLiteral(float(5))),FuncDecl(Id("x"),[VarDecl(Id("a"),None,NoneType(),None),VarDecl(Id("b"),None,NoneType(),None)],[VarDecl(Id("z"),None,StringType(),NumberLiteral(float(5))),ConstDecl(Id("$a"),None,NoneType(),NumberLiteral(float(5)))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))
    def test_exp_1(self):
        """Simple program: int main() {} """
        input = """
            Let x=2+5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("+",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))
    def test_exp_2(self):
        """Simple program: int main() {} """
        input = """
            Let x=2-5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("-",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))
    def test_exp_3(self):
        """Simple program: int main() {} """
        input = """
            Let x=2*5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("*",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))
    def test_exp_4(self):
        """Simple program: int main() {} """
        input = """
            Let x=2/5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("/",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))
    def test_exp_5(self):
        """Simple program: int main() {} """
        input = """
            Let x=2%5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("%",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))
    def test_exp_6(self):
        """Simple program: int main() {} """
        input = """
            Let x=2&&5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("&&",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))
    def test_exp_7(self):
        """Simple program: int main() {} """
        input = """
            Let x=2||5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("||",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))
    def test_exp_8(self):
        """Simple program: int main() {} """
        input = """
            Let x=2==5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("==",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))
    def test_exp_9(self):
        """Simple program: int main() {} """
        input = """
            Let x=2<5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("<",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))
    def test_exp_10(self):
        """Simple program: int main() {} """
        input = """
            Let x=2>=5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp(">=",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))
    def test_exp_11(self):
        """Simple program: int main() {} """
        input = """
            Let x=2==.5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("==.",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))
    def test_exp_12(self):
        """Simple program: int main() {} """
        input = """
            Let x=!True;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),UnaryOp("!",BooleanLiteral(True)))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))
    def test_exp_13(self):
        """Simple program: int main() {} """
        input = """
            Let x=-5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),UnaryOp("-",NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))
    def test_exp_14(self):
        """Simple program: int main() {} """
        input = """
            Let x=-a{name }{firstname};
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),UnaryOp("-",JSONAccess(Id("a"),[Id("name"),Id("firstname")])))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))
    def test_exp_15(self):
        """Simple program: int main() {} """
        input = """
            Let x=-a[2,3];
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),UnaryOp("-",ArrayAccess(Id("a"),[NumberLiteral(2.0),NumberLiteral(3.0)])))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))
    def test_exp_16(self):
        """Simple program: int main() {} """
        input = """
            Let x=-a[2+3,True];
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),UnaryOp("-",ArrayAccess(Id("a"),[BinaryOp("+",NumberLiteral(2.0),NumberLiteral(3.0)),BooleanLiteral(True)])))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))
    def test_exp_17(self):
        """Simple program: int main() {} """
        input = """
            Let x="5"- (2+3);
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("-",StringLiteral("5"),BinaryOp("+",NumberLiteral(2.0),NumberLiteral(3.0))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))
    def test_exp_18(self):
        """Simple program: int main() {} """
        input = """
            Let x="5"- (2+3);
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("-",StringLiteral("5"),BinaryOp("+",NumberLiteral(2.0),NumberLiteral(3.0))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))
    def test_exp_19(self):
        """Simple program: int main() {} """
        input = """
            Let x=Call(x,[]);
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),CallExpr(Id("x"),[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))
    def test_exp_20(self):
        """Simple program: int main() {} """
        input = """
            Let x=-2*3+5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("+",BinaryOp("*",UnaryOp("-",NumberLiteral(2.0)),NumberLiteral(3.0)),NumberLiteral(5.0)))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))
    def test_exp_21(self):
        """Simple program: int main() {} """
        input = """
            Let x=-Call(x,[])*5;
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("*",UnaryOp("-",CallExpr(Id("x"),[])),NumberLiteral(5.0)))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))
    
    def test_exp_22(self):
        """Simple program: int main() {} """
        input = """
            Let x=a[3+1,4]/Call(bool2str,[!3<2]);
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("/",ArrayAccess(Id("a"),[BinaryOp("+",NumberLiteral(3.0),NumberLiteral(1.0)),NumberLiteral(4.0)]),CallExpr(Id("bool2str"),[BinaryOp("<",UnaryOp("!",NumberLiteral(3.0)),NumberLiteral(2.0))])))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))
    
    
    def test_exp_23(self):
        """Simple program: int main() {} """
        input = """
            Let x=-Call(x,[])*5+a[3+1,4]/Call(bool2str,[!3<2]);
         }"""
        expect = Program([VarDecl(Id("x"),None,NoneType(), BinaryOp("+",BinaryOp("*",UnaryOp("-",CallExpr(Id("x"),[])),NumberLiteral(5.0)),BinaryOp("/",ArrayAccess(Id("a"),[BinaryOp("+",NumberLiteral(3.0),NumberLiteral(1.0)),NumberLiteral(4.0)]),CallExpr(Id("bool2str"),[BinaryOp("<",UnaryOp("!",NumberLiteral(3.0)),NumberLiteral(2.0))])))
)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))


    def test_if_1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
                If(a==1){ a=4;}
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[If([(BinaryOp("==",Id("a"),NumberLiteral(1.0)),[Assign(Id("a"),NumberLiteral(4.0))])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))
    def test_if_2(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
                If(a==1){ a=4;}
                Else{}
         }"""
        expect = Program([FuncDecl(Id("main"),[],[If([(BinaryOp("==",Id("a"),NumberLiteral(1.0)),[Assign(Id("a"),NumberLiteral(4.0))])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))
    def test_if_3(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
                If(a==1){ a=4;}
                Else{a=10;}
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[If([(BinaryOp("==",Id("a"),NumberLiteral(1.0)),[Assign(Id("a"),NumberLiteral(4.0))])],[Assign(Id("a"),NumberLiteral(10.0))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))
    def test_if_4(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
                If(a==1){ a=4;}
                Elif(a==2){a=5;}
                Else{a=10;}
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[If([(BinaryOp("==",Id("a"),NumberLiteral(1.0)),[Assign(Id("a"),NumberLiteral(4.0))]),(BinaryOp("==",Id("a"),NumberLiteral(2.0)),[Assign(Id("a"),NumberLiteral(5.0))])],[Assign(Id("a"),NumberLiteral(10.0))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))
    def test_if_5(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
                If(a==1){ a=4;}
                Elif(a==2){a=5;}
                Elif(a==3){a=8;}
                Else{a=10;}
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[If([(BinaryOp("==",Id("a"),NumberLiteral(1.0)),[Assign(Id("a"),NumberLiteral(4.0))]),(BinaryOp("==",Id("a"),NumberLiteral(2.0)),[Assign(Id("a"),NumberLiteral(5.0))]),(BinaryOp("==",Id("a"),NumberLiteral(3.0)),[Assign(Id("a"),NumberLiteral(8.0))])],[Assign(Id("a"),NumberLiteral(10.0))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))
    def test_if_6(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
                If(a==1){ a=4;}
                Elif(a==2){a=5;}
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[If([(BinaryOp("==",Id("a"),NumberLiteral(1.0)),[Assign(Id("a"),NumberLiteral(4.0))]),(BinaryOp("==",Id("a"),NumberLiteral(2.0)),[Assign(Id("a"),NumberLiteral(5.0))])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))
    def test_if_7(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
                If(a==1){ a=4;}
                Elif(a==2){a=5;}
                Elif(a==3){a=8;}
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[If([(BinaryOp("==",Id("a"),NumberLiteral(1.0)),[Assign(Id("a"),NumberLiteral(4.0))]),(BinaryOp("==",Id("a"),NumberLiteral(2.0)),[Assign(Id("a"),NumberLiteral(5.0))]),(BinaryOp("==",Id("a"),NumberLiteral(3.0)),[Assign(Id("a"),NumberLiteral(8.0))])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))
    def test_For_in_1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               For x In []{

               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[ForIn(Id("x"),ArrayLiteral([]),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))
    def test_For_in_2(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               For x In [1,[2,34]]{

               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[ForIn(Id("x"),ArrayLiteral([NumberLiteral(1.0),ArrayLiteral([NumberLiteral(2.0),NumberLiteral(34.0)])]),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    def test_For_in_3(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               For x In ab{

               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[ForIn(Id("x"),Id("ab"),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))
    def test_For_in_4(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               For x In ab{
                   c[x]=x*x;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[ForIn(Id("x"),Id("ab"),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))
    def test_For_of_1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               For x Of y{

               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[ForOf(Id("x"),Id("y"),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))
    def test_For_of_2(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               For x Of {y : 2}{

               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[ForOf(Id("x"),JSONLiteral([(Id("y"),NumberLiteral(2.0))]),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))
    def test_For_of_3(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               For x Of { name:"hao",age:21 }{

               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[ForOf(Id("x"),JSONLiteral([(Id("name"),StringLiteral("hao")),(Id("age"),NumberLiteral(21.0))]),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))
    def test_For_of_4(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               For x Of y{
                   c[x]=x*x;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[ForOf(Id("x"),Id("y"),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))
    def test_While_1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While (y){
                   c[x]=x*x;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(Id("y"),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))
    def test_While_2(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While(a==b){
                   c[x]=x*x;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(BinaryOp("==",Id("a"),Id("b")),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))
    def test_While_3(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While(a==b){
                   c[x]=x*x;
                   c[x]=x*x;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(BinaryOp("==",Id("a"),Id("b")),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x"))),Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))
    def test_Continue_1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While (y){
                   c[x]=x*x;
               }
               Continue;
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(Id("y"),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))]),Continue()])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))
    def test_Continue_2(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While(a==b){
                   c[x]=x*x;
                   Continue;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(BinaryOp("==",Id("a"),Id("b")),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x"))),Continue()])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))
    def test_Break_1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While (y){
                   c[x]=x*x;
               }
               Break;
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(Id("y"),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))]),Break()])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))
    def test_Break_2(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While(a==b){
                   c[x]=x*x;
                   Break;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(BinaryOp("==",Id("a"),Id("b")),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x"))),Break()])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))
    def test_Callstm_1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While (y){
                   c[x]=x*x;
               }
            Call(print,["iloveu"]);
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(Id("y"),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))]),CallStmt(Id("print"),[StringLiteral("iloveu")])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))
    def test_Callstm_2(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While(a==b){
                   c[x]=x*x;
                   Call(print,["iloveu"]);
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(BinaryOp("==",Id("a"),Id("b")),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x"))),CallStmt(Id("print"),[StringLiteral("iloveu")])])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))
    def test_return_1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While (y){
                   c[x]=x*x;
               }
               Return;
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(Id("y"),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))]),Return(None)])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    def test_return_2(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While(a==b){
                   c[x]=x*x;
                   Return;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(BinaryOp("==",Id("a"),Id("b")),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x"))),Return(None)])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))
    def test_return_3(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While (y){
                   c[x]=x*x;
               }
               Return y+1;
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(Id("y"),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))]),Return(BinaryOp("+",Id("y"),NumberLiteral(1.0)))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))
    def test_return_4(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While(a==b){
                   c[x]=x*x;
                   Return y+1;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[While(BinaryOp("==",Id("a"),Id("b")),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x"))),Return(BinaryOp("+",Id("y"),NumberLiteral(1.0)))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))
    def test_promgram1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
                Let a=2,b=3+a;
               While(a<b){
                   c[x]=x*x;
                   Return y+1;
               }
            
         }"""
        expect = Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),None,NoneType(),NumberLiteral(2.0)),VarDecl(Id("b"),None,NoneType(),BinaryOp("+",NumberLiteral(3.0),Id("a"))),While(BinaryOp("<",Id("a"),Id("b")),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x"))),Return(BinaryOp("+",Id("y"),NumberLiteral(1.0)))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))