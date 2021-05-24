# Generated from c:\Users\S540\Documents (2)\BK course\Ki_202\nguyen ly ngon ngu lap trinh\PPL_202_HCMUT\programing_code\CH2_3_Lexer\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("\u00ae\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\3\3\3\7\3.\n\3\f\3\16\3\61\13")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\7\6A\n\6\f\6\16\6D\13\6\3\7\3\7\3\7\3\7\5\7J\n\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\7\bT\n\b\f\b\16\bW\13")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\7\n^\n\n\f\n\16\na\13\n\3\13\3")
        buf.write("\13\3\13\5\13f\n\13\3\f\3\f\3\f\5\fk\n\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17}\n\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u0085")
        buf.write("\n\20\f\20\16\20\u0088\13\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u0090\n\21\f\21\16\21\u0093\13\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u009a\n\22\3\23\3\23\3\23\7\23\u009f")
        buf.write("\n\23\f\23\16\23\u00a2\13\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u00ac\n\24\3\24\2\4\36 \25\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&\2\4\3\2\4\5\3\2")
        buf.write("\22\23\2\u00ad\2(\3\2\2\2\4/\3\2\2\2\6\62\3\2\2\2\b9\3")
        buf.write("\2\2\2\n=\3\2\2\2\fE\3\2\2\2\16P\3\2\2\2\20X\3\2\2\2\22")
        buf.write("_\3\2\2\2\24e\3\2\2\2\26g\3\2\2\2\30n\3\2\2\2\32r\3\2")
        buf.write("\2\2\34|\3\2\2\2\36~\3\2\2\2 \u0089\3\2\2\2\"\u0099\3")
        buf.write("\2\2\2$\u009b\3\2\2\2&\u00ab\3\2\2\2()\5\4\3\2)*\7\2\2")
        buf.write("\3*\3\3\2\2\2+.\5\b\5\2,.\5\6\4\2-+\3\2\2\2-,\3\2\2\2")
        buf.write(".\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\5\3\2\2\2\61/\3")
        buf.write("\2\2\2\62\63\7\4\2\2\63\64\7\25\2\2\64\65\7\16\2\2\65")
        buf.write("\66\7\26\2\2\66\67\7\17\2\2\678\7\7\2\28\7\3\2\2\29:\t")
        buf.write("\2\2\2:;\5\n\6\2;<\7\7\2\2<\t\3\2\2\2=B\7\25\2\2>?\7\b")
        buf.write("\2\2?A\7\25\2\2@>\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2")
        buf.write("\2C\13\3\2\2\2DB\3\2\2\2EF\t\2\2\2FG\7\25\2\2GI\7\f\2")
        buf.write("\2HJ\5\16\b\2IH\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\7\r\2\2")
        buf.write("LM\7\n\2\2MN\5\22\n\2NO\7\13\2\2O\r\3\2\2\2PU\5\20\t\2")
        buf.write("QR\7\7\2\2RT\5\20\t\2SQ\3\2\2\2TW\3\2\2\2US\3\2\2\2UV")
        buf.write("\3\2\2\2V\17\3\2\2\2WU\3\2\2\2XY\t\2\2\2YZ\5\n\6\2Z\21")
        buf.write("\3\2\2\2[^\5\b\5\2\\^\5\24\13\2][\3\2\2\2]\\\3\2\2\2^")
        buf.write("a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\23\3\2\2\2a_\3\2\2\2bf")
        buf.write("\5\32\16\2cf\5\26\f\2df\5\30\r\2eb\3\2\2\2ec\3\2\2\2e")
        buf.write("d\3\2\2\2f\25\3\2\2\2gh\7\25\2\2hj\7\f\2\2ik\5$\23\2j")
        buf.write("i\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\7\r\2\2m\27\3\2\2\2no")
        buf.write("\7\6\2\2op\5\34\17\2pq\7\7\2\2q\31\3\2\2\2rs\7\25\2\2")
        buf.write("st\7\24\2\2tu\5\34\17\2uv\7\7\2\2v\33\3\2\2\2wx\5\36\20")
        buf.write("\2xy\7\20\2\2yz\5\34\17\2z}\3\2\2\2{}\5\36\20\2|w\3\2")
        buf.write("\2\2|{\3\2\2\2}\35\3\2\2\2~\177\b\20\1\2\177\u0080\5 ")
        buf.write("\21\2\u0080\u0086\3\2\2\2\u0081\u0082\f\4\2\2\u0082\u0083")
        buf.write("\7\21\2\2\u0083\u0085\5\36\20\5\u0084\u0081\3\2\2\2\u0085")
        buf.write("\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2")
        buf.write("\u0087\37\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008a\b\21")
        buf.write("\1\2\u008a\u008b\5\"\22\2\u008b\u0091\3\2\2\2\u008c\u008d")
        buf.write("\f\4\2\2\u008d\u008e\t\3\2\2\u008e\u0090\5\"\22\2\u008f")
        buf.write("\u008c\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092!\3\2\2\2\u0093\u0091\3\2\2")
        buf.write("\2\u0094\u0095\7\n\2\2\u0095\u0096\5\34\17\2\u0096\u0097")
        buf.write("\7\13\2\2\u0097\u009a\3\2\2\2\u0098\u009a\5&\24\2\u0099")
        buf.write("\u0094\3\2\2\2\u0099\u0098\3\2\2\2\u009a#\3\2\2\2\u009b")
        buf.write("\u00a0\5\34\17\2\u009c\u009d\7\b\2\2\u009d\u009f\5\34")
        buf.write("\17\2\u009e\u009c\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1%\3\2\2\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a3\u00ac\7\27\2\2\u00a4\u00ac\7\26\2\2\u00a5")
        buf.write("\u00ac\7\25\2\2\u00a6\u00ac\5\26\f\2\u00a7\u00a8\7\f\2")
        buf.write("\2\u00a8\u00a9\5\34\17\2\u00a9\u00aa\7\13\2\2\u00aa\u00ac")
        buf.write("\3\2\2\2\u00ab\u00a3\3\2\2\2\u00ab\u00a4\3\2\2\2\u00ab")
        buf.write("\u00a5\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00a7\3\2\2\2")
        buf.write("\u00ac\'\3\2\2\2\21-/BIU]_ej|\u0086\u0091\u0099\u00a0")
        buf.write("\u00ab")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'int'", "'float'", "'return'", 
                     "';'", "','", "'.'", "'{'", "'}'", "'('", "')'", "'['", 
                     "']'", "'+'", "'-'", "'*'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "NUMBER_LIT", "INT", "FLOAT", "RETURN", 
                      "SM", "CM", "DOT", "LB", "RB", "LP", "RP", "LSB", 
                      "RSB", "ADD", "SUB", "MUL", "DIV", "EQ", "ID", "INTLIT", 
                      "FLOATLIT", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_declarations = 1
    RULE_var_arr = 2
    RULE_vardecl = 3
    RULE_ids_list = 4
    RULE_funcdecl = 5
    RULE_parameterlist = 6
    RULE_parameter = 7
    RULE_body = 8
    RULE_statement = 9
    RULE_call_stm = 10
    RULE_return_stm = 11
    RULE_assignment_stm = 12
    RULE_expression = 13
    RULE_expression1 = 14
    RULE_expression2 = 15
    RULE_expression3 = 16
    RULE_expressionlist = 17
    RULE_operands = 18

    ruleNames =  [ "program", "declarations", "var_arr", "vardecl", "ids_list", 
                   "funcdecl", "parameterlist", "parameter", "body", "statement", 
                   "call_stm", "return_stm", "assignment_stm", "expression", 
                   "expression1", "expression2", "expression3", "expressionlist", 
                   "operands" ]

    EOF = Token.EOF
    NUMBER_LIT=1
    INT=2
    FLOAT=3
    RETURN=4
    SM=5
    CM=6
    DOT=7
    LB=8
    RB=9
    LP=10
    RP=11
    LSB=12
    RSB=13
    ADD=14
    SUB=15
    MUL=16
    DIV=17
    EQ=18
    ID=19
    INTLIT=20
    FLOATLIT=21
    COMMENT=22
    WS=23
    ERROR_CHAR=24
    UNCLOSE_STRING=25
    ILLEGAL_ESCAPE=26
    UNTERMINATED_COMMENT=27

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




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.declarations()
            self.state = 39
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




    def declarations(self):

        localctx = BKITParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.INT or _la==BKITParser.FLOAT:
                self.state = 43
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 41
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 42
                    self.var_arr()
                    pass


                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_arr




    def var_arr(self):

        localctx = BKITParser.Var_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(BKITParser.INT)
            self.state = 49
            self.match(BKITParser.ID)
            self.state = 50
            self.match(BKITParser.LSB)
            self.state = 51
            self.match(BKITParser.INTLIT)
            self.state = 52
            self.match(BKITParser.RSB)
            self.state = 53
            self.match(BKITParser.SM)
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

        def ids_list(self):
            return self.getTypedRuleContext(BKITParser.Ids_listContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_vardecl




    def vardecl(self):

        localctx = BKITParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 56
            self.ids_list()
            self.state = 57
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_ids_list




    def ids_list(self):

        localctx = BKITParser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ids_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(BKITParser.ID)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 60
                self.match(BKITParser.CM)
                self.state = 61
                self.match(BKITParser.ID)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(BKITParser.ParameterlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKITParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 68
            self.match(BKITParser.ID)
            self.state = 69
            self.match(BKITParser.LP)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.INT or _la==BKITParser.FLOAT:
                self.state = 70
                self.parameterlist()


            self.state = 73
            self.match(BKITParser.RP)
            self.state = 74
            self.match(BKITParser.LB)
            self.state = 75
            self.body()
            self.state = 76
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ParameterContext)
            else:
                return self.getTypedRuleContext(BKITParser.ParameterContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SM)
            else:
                return self.getToken(BKITParser.SM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_parameterlist




    def parameterlist(self):

        localctx = BKITParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameterlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.parameter()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.SM:
                self.state = 79
                self.match(BKITParser.SM)
                self.state = 80
                self.parameter()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_list(self):
            return self.getTypedRuleContext(BKITParser.Ids_listContext,0)


        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_parameter




    def parameter(self):

        localctx = BKITParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 87
            self.ids_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.VardeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT) | (1 << BKITParser.FLOAT) | (1 << BKITParser.RETURN) | (1 << BKITParser.ID))) != 0):
                self.state = 91
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.INT, BKITParser.FLOAT]:
                    self.state = 89
                    self.vardecl()
                    pass
                elif token in [BKITParser.RETURN, BKITParser.ID]:
                    self.state = 90
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stm(self):
            return self.getTypedRuleContext(BKITParser.Assignment_stmContext,0)


        def call_stm(self):
            return self.getTypedRuleContext(BKITParser.Call_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(BKITParser.Return_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 96
                self.assignment_stm()
                pass

            elif la_ == 2:
                self.state = 97
                self.call_stm()
                pass

            elif la_ == 3:
                self.state = 98
                self.return_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(BKITParser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stm




    def call_stm(self):

        localctx = BKITParser.Call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_call_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(BKITParser.ID)
            self.state = 102
            self.match(BKITParser.LP)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.ID) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT))) != 0):
                self.state = 103
                self.expressionlist()


            self.state = 106
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_return_stm




    def return_stm(self):

        localctx = BKITParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(BKITParser.RETURN)
            self.state = 109
            self.expression()
            self.state = 110
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assignment_stm




    def assignment_stm(self):

        localctx = BKITParser.Assignment_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(BKITParser.ID)
            self.state = 113
            self.match(BKITParser.EQ)
            self.state = 114
            self.expression()
            self.state = 115
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(BKITParser.Expression1Context,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.expression1(0)
                self.state = 118
                self.match(BKITParser.ADD)
                self.state = 119
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.expression1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(BKITParser.Expression2Context,0)


        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expression1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Expression1Context,i)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression1



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 127
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 128
                    self.match(BKITParser.SUB)
                    self.state = 129
                    self.expression1(3) 
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(BKITParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(BKITParser.Expression2Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.expression3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 138
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 139
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.MUL or _la==BKITParser.DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 140
                    self.expression3() 
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression3




    def expression3(self):

        localctx = BKITParser.Expression3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression3)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(BKITParser.LB)
                self.state = 147
                self.expression()
                self.state = 148
                self.match(BKITParser.RB)
                pass
            elif token in [BKITParser.LP, BKITParser.ID, BKITParser.INTLIT, BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_expressionlist




    def expressionlist(self):

        localctx = BKITParser.ExpressionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expressionlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.expression()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 154
                self.match(BKITParser.CM)
                self.state = 155
                self.expression()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def call_stm(self):
            return self.getTypedRuleContext(BKITParser.Call_stmContext,0)


        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operands




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_operands)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(BKITParser.FLOATLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(BKITParser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.match(BKITParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.call_stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.match(BKITParser.LP)
                self.state = 166
                self.expression()
                self.state = 167
                self.match(BKITParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression1_sempred
        self._predicates[15] = self.expression2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




