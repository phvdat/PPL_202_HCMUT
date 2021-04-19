# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\31\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3")
        buf.write("\3\7\3\20\n\3\f\3\16\3\23\13\3\3\4\3\4\3\5\3\5\3\5\2\2")
        buf.write("\6\2\4\6\b\2\2\2\26\2\n\3\2\2\2\4\21\3\2\2\2\6\24\3\2")
        buf.write("\2\2\b\26\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2\3\f\3\3\2\2")
        buf.write("\2\r\20\5\6\4\2\16\20\5\b\5\2\17\r\3\2\2\2\17\16\3\2\2")
        buf.write("\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\5\3\2")
        buf.write("\2\2\23\21\3\2\2\2\24\25\7\3\2\2\25\7\3\2\2\2\26\27\7")
        buf.write("\4\2\2\27\t\3\2\2\2\4\17\21")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'intint'", "'int'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_declarations = 1
    RULE_vardecl = 2
    RULE_var_arr = 3

    ruleNames =  [ "program", "declarations", "vardecl", "var_arr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    ERROR_CHAR=4
    UNCLOSE_STRING=5
    ILLEGAL_ESCAPE=6
    UNTERMINATED_COMMENT=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarations(self):
            return self.getTypedRuleContext(BKITParser.DeclarationsContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.declarations()
            self.state = 9
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.VardeclContext,i)


        def var_arr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_arrContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_arrContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = BKITParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.T__0 or _la==BKITParser.T__1:
                self.state = 13
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.T__0]:
                    self.state = 11
                    self.vardecl()
                    pass
                elif token in [BKITParser.T__1]:
                    self.state = 12
                    self.var_arr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKITParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(BKITParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_arrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_var_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_arr" ):
                return visitor.visitVar_arr(self)
            else:
                return visitor.visitChildren(self)




    def var_arr(self):

        localctx = BKITParser.Var_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(BKITParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





