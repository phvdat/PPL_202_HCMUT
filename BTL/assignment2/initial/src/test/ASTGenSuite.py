import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """Let a[2];"""
        expect = Program([VarDecl(Id("a"), [NumberLiteral(2.0)], NoneType(),None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))
    
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """Let a[True];"""
        expect = Program([VarDecl(Id("a"), [BooleanLiteral(True)], NoneType(),None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))


    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """Let a[2]: Boolean;"""
        expect = Program([VarDecl(Id("a"), [NumberLiteral(2.0)], BooleanType(),None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_simple_program4(self):
        """Simple program: int main() {} """
        input = """Let a[5]: Number;"""
        expect = Program([VarDecl(Id("a"), [NumberLiteral(5.0)], NumberType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_simple_program5(self):
        """Simple program: int main() {} """
        input = """Let a[5]: JSON;"""
        expect = Program([VarDecl(Id("a"), [NumberLiteral(5.0)], JSONType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_simple_program6(self):
        """Simple program: int main() {} """
        input = """Let a[5]: Number = 10;"""
        expect = Program([VarDecl(Id("a"), [NumberLiteral(5.0)], NumberType(), NumberLiteral(10.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_simple_program7(self):
        """Simple program: int main() {} """
        input = """Let a[5]: Boolean = True;"""
        expect = Program([VarDecl(Id("a"), [NumberLiteral(5.0)], BooleanType(), BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_simple_program8(self):
        """Simple program: int main() {} """
        input = """Let a: String = "string";"""
        expect = Program([VarDecl(Id("a"), None, StringType(), StringLiteral("string"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_simple_program9(self):
        """Simple program: int main() {} """
        input = """
                Let a[5]: Boolean = True;
                Let b = 5;
                """
        expect = Program([
            VarDecl(Id("a"), [NumberLiteral(5.0)], BooleanType(), BooleanLiteral(True)),
            VarDecl(Id("b"), None, NoneType(), NumberLiteral(5.0))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_simple_program10(self):
        """Simple program: int main() {} """
        input = """
                Let a[5]: Boolean = True;
                Let b = 5;
                Let c:Number;
                """
        expect = Program([
            VarDecl(Id("a"), [NumberLiteral(5.0)], BooleanType(), BooleanLiteral(True)),
            VarDecl(Id("b"), None, NoneType(), NumberLiteral(5.0)),
            VarDecl(Id("c"), None, NumberType(), None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_simple_program11(self):
        """Simple program: int main() {} """
        input = """
                Let a[5]: Boolean = True,b = 5.43, c:Number;
                """
        expect = Program([
            VarDecl(Id("a"), [NumberLiteral(5.0)], BooleanType(), BooleanLiteral(True)),
            VarDecl(Id("b"), None, NoneType(), NumberLiteral(5.43)),
            VarDecl(Id("c"), None, NumberType(), None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_simple_program12(self):
        """Simple program: int main() {} """
        input = """Constant $a = 100;"""
        expect = Program([ConstDecl(Id("$a"), None, NoneType(),NumberLiteral(100.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_simple_program13(self):
        """Simple program: int main() {} """
        input = """Constant $a[10] = 100;"""
        expect = Program([ConstDecl(Id("$a"), [NumberLiteral(10.0)], NoneType(),NumberLiteral(100.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_simple_program14(self):
        """Simple program: int main() {} """
        input = """Constant $a:String = 100;"""
        expect = Program([ConstDecl(Id("$a"), None, StringType(),NumberLiteral(100.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))


    def test_simple_program15(self):
        """Simple program: int main() {} """
        input = """Constant $a:Boolean = 100;"""
        expect = Program([ConstDecl(Id("$a"), None, BooleanType(),NumberLiteral(100.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))


    def test_simple_program16(self):
        """Simple program: int main() {} """
        input = """Constant $a[10]: Number = 100;"""
        expect = Program([ConstDecl(Id("$a"), [NumberLiteral(10.0)], NumberType(),NumberLiteral(100.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_simple_program17(self):
        """Simple program: int main() {} """
        input = """Constant $a[10]: String = "Pham Van Dat";"""
        expect = Program([ConstDecl(Id("$a"), [NumberLiteral(10.0)], StringType(),StringLiteral("Pham Van Dat"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_simple_program18(self):
        """Simple program: int main() {} """
        input = """Constant $x[2]:Boolean = 5, $y = True, $z[1] = 40;"""
        expect = Program([
            ConstDecl(Id("$x"), [NumberLiteral(2.0)], BooleanType(),NumberLiteral(5.0)),
            ConstDecl(Id("$y"), None, NoneType(),BooleanLiteral(True)),
            ConstDecl(Id("$z"), [NumberLiteral(1.0)], NoneType(),NumberLiteral(40.0))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_simple_program19(self):
        """Simple program: int main() {} """
        input = """
            Constant $x[2]:Boolean = 5;
            Constant $y = True;
            Constant $z[1] = 40;"""
        expect = Program([
            ConstDecl(Id("$x"), [NumberLiteral(2.0)], BooleanType(),NumberLiteral(5.0)),
            ConstDecl(Id("$y"), None, NoneType(),BooleanLiteral(True)),
            ConstDecl(Id("$z"), [NumberLiteral(1.0)], NoneType(),NumberLiteral(40.0))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_simple_program20(self):
        """Simple program: int main() {} """
        input = """
            Constant $x[2]:Boolean = 5;
            Let y = True;
            """
        expect = Program([
            ConstDecl(Id("$x"), [NumberLiteral(2.0)], BooleanType(),NumberLiteral(5.0)),
            VarDecl(Id("y"), None, NoneType(),BooleanLiteral(True))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_simple_program21(self):
        """Simple program: int main() {} """
        input = """
            Constant $x[2]:Boolean = 5;
            Let y = 2+2;
            """
        expect = Program([
            ConstDecl(Id("$x"), [NumberLiteral(2.0)], BooleanType(),NumberLiteral(5.0)),
            VarDecl(Id("y"), None, NoneType(),BinaryOp("+",NumberLiteral(2.0),NumberLiteral(2.0)))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_simple_program22(self):
        """Simple program: int main() {} """
        input = """
            Constant $x[2]:Boolean = 5;
            Let y = 2+"string";
            """
        expect = Program([
            ConstDecl(Id("$x"), [NumberLiteral(2.0)], BooleanType(),NumberLiteral(5.0)),
            VarDecl(Id("y"), None, NoneType(),BinaryOp("+",NumberLiteral(2.0),StringLiteral("string")))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_simple_program23(self):
        """Simple program: int main() {} """
        input = """
            Constant $x[2]:Boolean = 2>3;
            Let y = 2+"Pham";
            """
        expect = Program([
            ConstDecl(Id("$x"), [NumberLiteral(2.0)], BooleanType(),BinaryOp(">",NumberLiteral(2.0),NumberLiteral(3.0))),
            VarDecl(Id("y"), None, NoneType(),BinaryOp("+",NumberLiteral(2.0),StringLiteral("Pham")))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_simple_program24(self):
        """Simple program: int main() {} """
        input = """
            Constant $x[2]:Boolean = 100 > !3;
            """
        expect = Program([
            ConstDecl(Id("$x"), [NumberLiteral(2.0)], BooleanType(),BinaryOp(">",NumberLiteral(100.0),UnaryOp("!",NumberLiteral(3.0))))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_simple_program25(self):
        """Simple program: int main() {} """
        input = """
            Constant $x[2]:Boolean = -"Dat" > !10;
            """
        expect = Program([
            ConstDecl(Id("$x"), [NumberLiteral(2.0)], BooleanType(),BinaryOp(">",UnaryOp("-",StringLiteral("Dat")),UnaryOp("!",NumberLiteral(10.0))))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_simple_program26(self):
        """Simple program: int main() {} """
        input = """
            Let x[2]:Boolean = !!!10;
            """
        expect = Program([
            VarDecl(Id("x"), [NumberLiteral(2.0)], BooleanType(),UnaryOp("!",UnaryOp("!",UnaryOp("!",NumberLiteral(10.0)))))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))
    
    def test_simple_program27(self):
        """Simple program: int main() {} """
        input = """
            Let x:Number = 100-10;
            """
        expect = Program([
            VarDecl(Id("x"), None, NumberType(),BinaryOp('-',NumberLiteral(100.0),NumberLiteral(10.0)))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))
    
    def test_simple_program28(self):
        """Simple program: int main() {} """
        input = """
            Let x:Number = 100*10;
            """
        expect = Program([
            VarDecl(Id("x"), None, NumberType(),BinaryOp('*',NumberLiteral(100.0),NumberLiteral(10.0)))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))
    
    def test_simple_program29(self):
        """Simple program: int main() {} """
        input = """
            Let x:Number = 100/10;
            """
        expect = Program([
            VarDecl(Id("x"), None, NumberType(),BinaryOp('/',NumberLiteral(100.0),NumberLiteral(10.0)))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_simple_program30(self):
        """Simple program: int main() {} """
        input = """
            Let x:Number = 100%10;
            """
        expect = Program([
            VarDecl(Id("x"), None, NumberType(),BinaryOp('%',NumberLiteral(100.0),NumberLiteral(10.0)))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))
    
    def test_simple_program31(self):
        """Simple program: int main() {} """
        input = """
            Let x:Number = a[10];
            """
        expect = Program([
            VarDecl(Id("x"), None, NumberType(),ArrayAccess(Id("a"), [NumberLiteral(10.0)]))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_simple_program32(self):
        """Simple program: int main() {} """
        input = """
            Let x:Number = a{"name"};
            """
        expect = Program([
            VarDecl(Id("x"), None, NumberType(),JSONAccess(Id("a"), [StringLiteral("name")]))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))
    
    def test_simple_program33(self):
        """Simple program: int main() {} """
        input = """
            Let x:Number = !(a+b);
            """
        expect = Program([
            VarDecl(Id("x"), None, NumberType(),UnaryOp("!",BinaryOp("+", Id("a"), Id("b"))))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_simple_program34(self):
        """Simple program: int main() {} """
        input = """
            Let x:Number = !a+b;
            """
        expect = Program([
            VarDecl(Id("x"), None, NumberType(),BinaryOp("+", UnaryOp("!",Id("a")), Id("b")))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_simple_program35(self):
        """Simple program: int main() {} """
        input = """
            Let x:Number = Call(foo, [2,3]);
            """
        expect = Program([
            VarDecl(Id("x"), None, NumberType(),CallExpr(Id("foo"), [NumberLiteral(2.0), NumberLiteral(3.0)]))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    # ..........................................................
    # .......................Func...............................
    # ..........................................................
    def test_Func_simple(self):
        input = """
        Function main(a,b){
            x = 10;
            }
        """
        expect = Program([
            FuncDecl(Id("main"),[VarDecl(Id("a"), [], NoneType(), None), VarDecl(Id("b"), [], NoneType(), None)],
            [ Assign(Id("x"),NumberLiteral(10.0))])
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_Func_var_simple(self):
        input = """Let x:Number;
        Function foo(a){
            x = 10;
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"),[VarDecl(Id("a"), [], NoneType(), None)] ,
            [Assign(Id("x"),NumberLiteral(10.0))])
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_Func_var_simple1(self):
        input = """Let x:Number;
        Function foo(){
            x = 10;
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [],
            [Assign(Id("x"),NumberLiteral(10.0))])
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_Func_var_simple2(self):
        input = """Let x:Number;
        Function foo(){
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [],
            [])
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_Func_var_simple2(self):
        input = """Let x:Number;
        Function foo(a[10]){
            x = 100;
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [Assign(Id("x"),NumberLiteral(100.0))])
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_Func_var_simple3(self):
        input = """Let x:Number;
        Function foo(a[10]){
            b = 100;
            Let x:Number =10;
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [Assign(Id("b"),NumberLiteral(100.0)),VarDecl(Id("x"), None ,NumberType(), NumberLiteral(10.0))])
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_Func_var_simple4(self):
        input = """Let x:Number;
        Function foo(a[10]){
            b = 100;
            Constant $x:Number =10;
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [Assign(Id("b"),NumberLiteral(100.0)),ConstDecl(Id("$x"), None ,NumberType(), NumberLiteral(10.0))])
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_Func_var_simple5(self):
        input = """Let x:Number;
        Function foo(a[10]){
            b = 100;
            Let x:Number =10;
            Constant $y:Number =10;
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [Assign(Id("b"),NumberLiteral(100.0)),
            VarDecl(Id("x"), None ,NumberType(), NumberLiteral(10.0)),
            ConstDecl(Id("$y"), None ,NumberType(), NumberLiteral(10.0))])
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_Func_var_simple6(self):
        input = """Let x:Number;
        Function foo(a[10]){
            b = 100;
            Let x:Number =10+!5;
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [Assign(Id("b"),NumberLiteral(100.0)),
            VarDecl(Id("x"), None ,NumberType(), BinaryOp("+", NumberLiteral(10.0), UnaryOp("!", NumberLiteral(5.0))))])
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_Func_var_simple7(self):
        input = """Let x:Number;
        Function foo(a[10]){
            b = 100;
            Let x:Number =10+!5;
        }

        Function foo2(a[10]){
            b = 100;
            Let x:Number =10;
            Constant $y:Number =10;
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [Assign(Id("b"),NumberLiteral(100.0)),
            VarDecl(Id("x"), None ,NumberType(), BinaryOp("+", NumberLiteral(10.0), UnaryOp("!", NumberLiteral(5.0))))]),
            
            FuncDecl(Id("foo2"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [Assign(Id("b"),NumberLiteral(100.0)),
            VarDecl(Id("x"), None ,NumberType(), NumberLiteral(10.0)),
            ConstDecl(Id("$y"), None ,NumberType(), NumberLiteral(10.0))])
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    # ..........................................................
    # .....................Statements...........................
    # ..........................................................

    # #Assign
    def test_if_statement(self):
        input = """Let x:Number;
        Function foo(a[10]){
            If(5){
                a = 100;
            }
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [If( [(NumberLiteral(5.0), [Assign(Id("a"), NumberLiteral(100.0))])], [])]
            )
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_if_statement1(self):
        input = """Let x:Number;
        Function foo(a[10]){
            If(5){
                Constant $a:Number = 100;
            }
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [If( [(NumberLiteral(5.0), [ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0))])], [])]
            )
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_if_statement2(self):
        input = """Let x:Number;
        Function foo(a[10]){
            If(5){
                a = 100;
                b = a;
                c = b;
            }
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [If( [(NumberLiteral(5.0), [Assign(Id("a"), NumberLiteral(100.0)), Assign(Id("b"), Id("a")), Assign(Id("c"), Id("b"))])], [])]
            )
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_if_statement3(self):
        input = """Let x:Number;
        Function foo(a[10]){
            If(5){
                Constant $a:Number = 100;
                Let b:String = "hcmut";
            }
        }
        """
        expect = Program([
            VarDecl(Id("x"), None,NumberType(), None),
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [If( [(NumberLiteral(5.0), [ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)),
                                        VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut"))])], [])]
            )
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_if_statement4(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(a>=b){
                Constant $a:Number = 100;
                Let b:String = "hcmut";
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [(BinaryOp('>=', Id('a'), Id('b')),[ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)),
                                        VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut"))])], [])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    
    def test_if_statement5(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(a>=b){
                Constant $a:Number = 100;
                Let b:String = "hcmut";
            }
            Elif(a!=10){
                a = 30;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [   (BinaryOp('>=', Id('a'), Id('b')),[ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)), VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut"))]),
                        (BinaryOp('!=', Id('a'), NumberLiteral(10.0)), [Assign( Id("a"), NumberLiteral(30.0))])], [])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_if_statement6(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(a>=b){
                Constant $a:Number = 100;
                Let b:String = "hcmut";
            }
            Elif(a!=10){
                a = 30;
            }
            Elif( love ==. "string"){
                crush = hcmut;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [   (BinaryOp('>=', Id('a'), Id('b')),[ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)), VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut"))]),
                        (BinaryOp('!=', Id('a'), NumberLiteral(10.0)), [Assign( Id("a"), NumberLiteral(30.0))]),
                        (BinaryOp('==.', Id('love'), StringLiteral("string")), [Assign( Id("crush"), Id("hcmut"))])], [])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_if_statement7(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(a>=b){
                Constant $a:Number = 100;
                Let b:String = "hcmut";
            }
            Elif(a!=10){
                a = 30;
            }
            Elif( love ==. "string"){
                crush = hcmut;
            }
            Else{
                like = love;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [   (BinaryOp('>=', Id('a'), Id('b')),[ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)), VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut"))]),
                        (BinaryOp('!=', Id('a'), NumberLiteral(10.0)), [Assign( Id("a"), NumberLiteral(30.0))]),
                        (BinaryOp('==.', Id('love'), StringLiteral("string")), [Assign( Id("crush"), Id("hcmut"))])],
                    [ Assign(Id("like"), Id("love"))])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_if_statement8(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(love ==. "string"){
                crush = hcmut;
            }
            Else{
                like = love;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [ (BinaryOp('==.', Id('love'), StringLiteral("string")), [Assign( Id("crush"), Id("hcmut"))])],
                    [ Assign(Id("like"), Id("love"))])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    
    def test_if_statement9(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(love ==. "string"){
                crush = hcmut;
            }
            Else{
                like = love;
            }
            Constant $cons = 10;
            If(love == "crush"){
                crush = crush*2;
            }
            Else{
                love = like;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [ (BinaryOp('==.', Id('love'), StringLiteral("string")), [Assign( Id("crush"), Id("hcmut"))])],
                    [ Assign(Id("like"), Id("love"))]),
                ConstDecl(Id("$cons"), None, NoneType(), NumberLiteral(10.0)),
                If( [ (BinaryOp('==', Id('love'), StringLiteral("crush")), [Assign( Id("crush"), BinaryOp("*",Id("crush"), NumberLiteral(2.0)))])],
                    [ Assign(Id("love"), Id("like"))]),
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_Json_01(self):
        input = """
                Function main() {
                    Call(foo, [1,2]){"name"} = "Pham Van Dat";
                }
        """
        expect = Program([FuncDecl(
            Id("main"),
            [],
            [Assign(JSONAccess(CallExpr(Id("foo"), [NumberLiteral(1.0), NumberLiteral(2.0)]),[StringLiteral("name")]),StringLiteral("Pham Van Dat"))]
            )])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))


    def test_if_statement11(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(love ==. "string"){
                crush = hcmut;
                If(crush == "crush"){
                    status = "Yes";
                }
                Else{
                    status = "No";
                }
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [
                        (BinaryOp('==.', Id('love'), StringLiteral("string")), 
                        [Assign( Id("crush"), Id("hcmut")),
                        If( [ (BinaryOp('==', Id('crush'), StringLiteral("crush")), [Assign( Id("status"), StringLiteral("Yes"))])],
                    [ Assign(Id("status"), StringLiteral("No"))])
                    ])],[])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_while_statement1(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            While(crush == "crush"){
                status = "Yes";
                action = "No";
            }
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                While( BinaryOp('==', Id('crush'), StringLiteral("crush")), [Assign( Id("status"), StringLiteral("Yes")), Assign(Id("action"), StringLiteral("No"))])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_while_statement2(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            While(crush == "crush"){
                status = "Yes";
                action = "No";
            }
            While(age>18){
                mode = "Fboy";
            }
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                While( BinaryOp('==', Id('crush'), StringLiteral("crush")), [Assign( Id("status"), StringLiteral("Yes")), Assign(Id("action"), StringLiteral("No"))]),
                While( BinaryOp('>', Id('age'), NumberLiteral(18.0)), [Assign( Id("mode"), StringLiteral("Fboy"))])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_while_statement3(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            While(crush == "crush"){
                status = "Yes";
                action = "No";
                While(age>18){
                    mode = "Fboy";
                }
            }
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                While( BinaryOp('==', Id('crush'), StringLiteral("crush")), [Assign( Id("status"), StringLiteral("Yes")),
                                                                            Assign(Id("action"), StringLiteral("No")),
                                                                            While( BinaryOp('>', Id('age'), NumberLiteral(18.0)), [Assign( Id("mode"), StringLiteral("Fboy"))])])
                
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_Call_Func(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            Call(foo, [c,2+3]);
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                CallStmt(Id("foo"), [Id("c"), BinaryOp("+", NumberLiteral(2.0), NumberLiteral(3.0))])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))


    def test_Call_Func1(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = Call(foo, [c,2+3]);
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), CallExpr(Id("foo"), [Id("c"), BinaryOp("+", NumberLiteral(2.0), NumberLiteral(3.0))]))
                
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_Break(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            While(crush == "crush"){
                status = "Yes";
                action = "No";
                Break;
            }
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                While( BinaryOp('==', Id('crush'), StringLiteral("crush")), [Assign( Id("status"), StringLiteral("Yes")), Assign(Id("action"), StringLiteral("No")),Break()])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_Break2(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            Break;
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                Break()
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_Continue(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            Continue;
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                Continue()
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_Continue2(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(a>=b){
                Constant $a:Number = 100;
                Let b:String = "hcmut";
                Continue;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [(BinaryOp('>=', Id('a'), Id('b')),[ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)),
                                        VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut")), Continue()])], [])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    
    def test_Return_stmt(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(a>=b){
                Constant $a:Number = 100;
                Let b:String = "hcmut";
                Return ;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [(BinaryOp('>=', Id('a'), Id('b')),[ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)),
                                        VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut")), Return(None)])], [])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    
    def test_Return_stmt1(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            Return a;
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                Return(Id("a"))
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_Return_stmt2(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            Return a+3;
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                Return(BinaryOp("+",Id("a"), NumberLiteral(3.0)))
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    
    def test_Return_stmt3(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            Return a[10];
        
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                Return(ArrayAccess(Id("a"), [NumberLiteral(10.0)]))
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    
    def test_Return_stmt4(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(a>=b){
                Constant $a:Number = 100;
                Let b:String = "hcmut";
                Return;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [(BinaryOp('>=', Id('a'), Id('b')),[ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)),
                                        VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut")), Return(None)])], [])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    
    def test_Return_stmt4(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            If(a>=b){
                Constant $a:Number = 100;
                Let b:String = "hcmut";
                Return "i love you";
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],

            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                If( [(BinaryOp('>=', Id('a'), Id('b')),[ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)),
                                        VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut")), Return(StringLiteral("i love you"))])], [])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_For_In(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            For i In arr{
                Let a;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                ForIn( Id("i"), Id("arr"), [VarDecl(Id("a"), None, NoneType(), None)])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_For_In1(self):
        input = """
        Function foo(a[10]){
            For i In [1, 2, 3] {
                Call(printLn, [i]);
            }

        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [
                ForIn( Id("i"),
                    ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)]),
                    [CallStmt(Id("printLn"), [Id("i")])]

                    )
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_For_In2(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            For i In arr{
                a =10;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                ForIn( Id("i"), Id("arr"), [Assign(Id("a"), NumberLiteral(10.0))])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_For_In3(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            For i In arr{
                Constant $a:Number = 100;
                Let b:String = "hcmut";
                Return "i love you";
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                ForIn( Id("i"), Id("arr"), [ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)),
                                        VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut")), Return(StringLiteral("i love you"))])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_For_Of(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            For i Of json{
                Let a;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                ForOf( Id("i"), Id("json"), [VarDecl(Id("a"), None, NoneType(), None)])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))


    def test_For_Of2(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            For i Of json{
                a =10;
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                ForOf( Id("i"), Id("json"), [Assign(Id("a"), NumberLiteral(10.0))])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_For_Of3(self):
        input = """
        Function foo(a[10]){
            Let a:Number = 20;
            Let b:Number = 10;
            For i Of json{
                Constant $a:Number = 100;
                Let b:String = "hcmut";
                Return "i love you";
            }
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [
                VarDecl(Id("a"), None,NumberType(), NumberLiteral(20.0)),
                VarDecl(Id("b"), None,NumberType(), NumberLiteral(10.0)),
                ForOf( Id("i"), Id("json"), [ConstDecl(Id("$a"),None, NumberType(), NumberLiteral(100.0)),
                                        VarDecl(Id("b"), None, StringType(),StringLiteral("hcmut")), Return(StringLiteral("i love you"))])
            ])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    
    def test_Function_1(self):
        input = """
        Function foo(a[10]){
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"),
            [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_Callstmt_1(self):
        input = """
        Function foo(a[10]){
            Call(bool2str,[!3<2]);
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"),
            [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [CallStmt(Id("bool2str"),[BinaryOp("<",UnaryOp("!",NumberLiteral(3.0)),NumberLiteral(2.0))])])
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_Callstmt_2(self):
        input = """
        Function foo(a[10]){
            Call(foo,[]);
        }
        """
        expect = Program([
            
            FuncDecl(Id("foo"),
            [VarDecl(Id("a"), [NumberLiteral(10.0)], NoneType(), None)],
            [CallStmt(Id("foo"),[])]
            )
            
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))


    def test_Callstm_1(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While (y){
                   c[x]=x*x;
               }
            Call(print,["iloveu"]);
        }
         """
        expect = Program([FuncDecl(Id("main"),[],[While(Id("y"),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x")))]),CallStmt(Id("print"),[StringLiteral("iloveu")])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_Callstm_2(self):
        """Simple program: int main() {} """
        input = """
            Function main(){
               While(a==b){
                   c[x]=x*x;
                   Call(print,["iloveu"]);
               }
            }
            
         """
        expect = Program([FuncDecl(Id("main"),[],[While(BinaryOp("==",Id("a"),Id("b")),[Assign(ArrayAccess(Id("c"),[Id("x")]),BinaryOp("*",Id("x"),Id("x"))),CallStmt(Id("print"),[StringLiteral("iloveu")])])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))
    
    def test_exp_24(self):
        """Simple program: int main() {} """
        input = """
            Let x=Call(x,[]);
         """
        expect = Program([
            VarDecl(Id("x"),None,NoneType(),CallExpr(Id("x"), []),
                )
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))


    def test_exp_23(self):
        """Simple program: int main() {} """
        input = """
            Let x=-Call(x,[1])*5+a[3+1,4]/Call(bool2str,[!3<2]);
         """
        expect = Program([
            VarDecl(Id("x"),None,NoneType(),
            BinaryOp("+",
                    BinaryOp("*", UnaryOp("-", CallExpr(Id("x"), [NumberLiteral(1.0)])), NumberLiteral(5.0)),
                    BinaryOp("/", ArrayAccess(Id("a"), [BinaryOp("+", NumberLiteral(3.0), NumberLiteral(1.0)), NumberLiteral(4.0)]), CallExpr(Id("bool2str"),[BinaryOp("<",UnaryOp("!",NumberLiteral(3.0)),NumberLiteral(2.0))]))           
                    )
            )
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    # CALLSTATEMENT OR CALLEXPR
    def test_exp_22(self):
        """Simple program: int main() {} """
        input = """
            Let x=a[3+1,4]/Call(bool2str,[!3<2]);
         """
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("/",ArrayAccess(Id("a"),[BinaryOp("+",NumberLiteral(3.0),NumberLiteral(1.0)),NumberLiteral(4.0)]),CallExpr(Id("bool2str"),[BinaryOp("<",UnaryOp("!",NumberLiteral(3.0)),NumberLiteral(2.0))])))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_exp_8(self):
        """Simple program: int main() {} """
        input = """
            Let x=2==5;
        """
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("==",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_exp_5(self):
        """Simple program: int main() {} """
        input = """
            Let x=2||5;
        """
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("||",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_exp_6(self):
        """Simple program: int main() {} """
        input = """
            Let x=2&&5;
        """
        expect = Program([VarDecl(Id("x"),None,NoneType(),BinaryOp("&&",NumberLiteral(float(2)),NumberLiteral(float(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_Func_var_simple_07(self):
        input = """Let x:Number = {name: "Pham Van Dat", age: 21};
        """
        expect = Program([
            VarDecl(Id("x"), None ,NumberType(), JSONLiteral([(Id("name"),StringLiteral("Pham Van Dat")), (Id("age"), NumberLiteral(21.0))]))
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_Func_var_simple_06(self):
        input = """
                Function main() {
                    a{"name"}{"id"} = 5;
                }
        """
        expect = Program([FuncDecl(
            Id("main"),
            [],
            [Assign(JSONAccess(Id("a"),[StringLiteral("name"),StringLiteral("id")]),NumberLiteral(5.0))]
            )])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_Func_var_simple_05(self):
        input = """Let x:Number = {name: "Pham Van Dat"};
        """
        expect = Program([
            VarDecl(Id("x"), None ,NumberType(), JSONLiteral([(Id("name"),StringLiteral("Pham Van Dat"))]))
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_Func_var_simple_04(self):
        input = """Let x:Number = [1,2,3];
        """
        expect = Program([
            VarDecl(Id("x"), None ,NumberType(), ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0),NumberLiteral(3.0)]))
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_93(self):
        input = """Function main(){
            a{"name"}[1]{"first"}[2] = 1;
        }"""
        expect = Program([
            FuncDecl(Id("main"), [], [
            Assign(
                ArrayAccess( JSONAccess( ArrayAccess(JSONAccess(Id('a'),[StringLiteral("name")]), [NumberLiteral(1.0)]),[StringLiteral("first")]),[NumberLiteral(2.0)]),
                NumberLiteral(1.0)),
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_Elearning2(self):
        input = """
            Let x;
            Function main(x[10], y) {}
        """
        expect = Program([VarDecl(Id("x"), None,NoneType(), None),
                        FuncDecl(Id("main"),[VarDecl(Id("x"),[NumberLiteral(10.0)],NoneType(), None),VarDecl(Id("y"),None, NoneType(), None)],[])])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

        
    def test_95(self):
        input = """Function main(){
            a{"name"}[1] =1;
        }"""
        expect = Program([
            FuncDecl(Id("main"), [], [
                Assign(
                    ArrayAccess(
                        JSONAccess(Id('a'),[StringLiteral("name")]),
                        [NumberLiteral(1.0)]
                    ),
                    NumberLiteral(1.0)
                )
            ])
        ])
        
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))
    def test_Elearning(self):
        input = """
            Let x;
            Constant $y: Number = 10;
            Function main(x[], y) {}
        """
        expect = Program([VarDecl(Id("x"), None,NoneType(), None),
                        ConstDecl(Id("$y"), None,NumberType(),NumberLiteral(10.0)),
                        FuncDecl(Id("main"),[VarDecl(Id("x"),[],NoneType(), None),VarDecl(Id("y"), [],NoneType(), None)],[])])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_Func_var_simple_03(self):
        input = """Let x:Number = 10+11+12;
        """
        expect = Program([
            VarDecl(Id("x"), None ,NumberType(), BinaryOp("+",  BinaryOp("+",NumberLiteral(10.0), NumberLiteral(11.0)),NumberLiteral(12.0)))
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_Func_var_simple_02(self):
        input = """Let x:Number = 10*11*12;
        """
        expect = Program([
            VarDecl(Id("x"), None ,NumberType(), BinaryOp("*",  BinaryOp("*",NumberLiteral(10.0), NumberLiteral(11.0)),NumberLiteral(12.0)))
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_Func_var_simple_01(self):
        input = """Let x:Number = 10*11+12;
        """
        expect = Program([
            VarDecl(Id("x"), None ,NumberType(), BinaryOp("+",  BinaryOp("*",NumberLiteral(10.0), NumberLiteral(11.0)),NumberLiteral(12.0)))
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_Func_var_simple_0(self):
        input = """Let x:Number = 10+11*12;
        """
        expect = Program([
            VarDecl(Id("x"), None ,NumberType(), BinaryOp("+", NumberLiteral(10.0), BinaryOp("*", NumberLiteral(11.0),NumberLiteral(12.0))))
                ])
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
