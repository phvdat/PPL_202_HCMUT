# Generated from c:\Users\S540\OneDrive\Máy tính\Ki_202\nguyen ly ngon ngu lap trinh\programing_code\chuong_2\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("+\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\6\4\36\n\4\r\4\16\4\37\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\3")
        buf.write("\5\2\13\f\17\17\"\"\2+\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\3\21\3\2\2\2\5\30\3\2\2\2\7\35\3\2\2\2\t#\3\2\2\2\13")
        buf.write("%\3\2\2\2\r\'\3\2\2\2\17)\3\2\2\2\21\22\7k\2\2\22\23\7")
        buf.write("p\2\2\23\24\7v\2\2\24\25\7k\2\2\25\26\7p\2\2\26\27\7v")
        buf.write("\2\2\27\4\3\2\2\2\30\31\7k\2\2\31\32\7p\2\2\32\33\7v\2")
        buf.write("\2\33\6\3\2\2\2\34\36\t\2\2\2\35\34\3\2\2\2\36\37\3\2")
        buf.write("\2\2\37\35\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\b\4\2\2\"")
        buf.write("\b\3\2\2\2#$\13\2\2\2$\n\3\2\2\2%&\13\2\2\2&\f\3\2\2\2")
        buf.write("\'(\13\2\2\2(\16\3\2\2\2)*\13\2\2\2*\20\3\2\2\2\4\2\37")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WS = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6
    UNTERMINATED_COMMENT = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'intint'", "'int'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


