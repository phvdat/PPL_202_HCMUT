grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

// TUAN 2
// program  :EOF ;
//(vardecl | fimcdecl)*
// ID: [a-z][a-z0-9]* ;

// fragment INTPART : [0-9]+ ;
// fragment FRACPACT : '.' [0-9]+ ;
// fragment EXPART : 'e' '-'? [0-9]+ ;
// REAL: INTPART (FRACPACT EXPART? | EXPART) ;


// fragment STRINGQ: '\'' ;
// STRING: STRINGQ (~('\'') | (STRINGQ STRINGQ))*  STRINGQ ;

//TUAN 3
program  :declarations EOF ;
declarations:(vardecl |var_arr)*;
vardecl: 'intint';
var_arr: 'int';
// var_arr: INT ID LSB INTLIT RSB SM;
// vardecl:    (INT|FLOAT) ids_list SM ; 
// ids_list:   ID (CM ID)*;

// funcdecl:       (INT|FLOAT) ID LP parameterlist? RP LB body RB;
// parameterlist:  parameter(SM parameter)* ;
// parameter:      (INT|FLOAT) ids_list;
// body:           (vardecl|statement)*;
// statement:      (assignment_stm|call_stm|return_stm);
// call_stm:       ID LP expressionlist? RP;
// return_stm:     RETURN expression SM;
// assignment_stm: ID EQ expression SM;

// NUMBER_LIT:SUB? Digit+ DOT?	// 12 | -12.
// 		|  SUB? Digit+ DOT Digit+ Expo? // 12.34 | 12.34E-56
//         |  SUB? Digit+ DOT? Expo; // -12.E-2 | 12E-4

// fragment Digit : [0-9];
// fragment Expo: [eE] (SUB|ADD)? Digit+;

// expression:     expression1 ADD expression |expression1;
// expression1:    expression1 SUB expression1|expression2;
// expression2:    expression2 (MUL|DIV) expression3|expression3;
// expression3:    LB expression RB | operands;
// expressionlist: expression (CM expression)*;
// operands:       FLOATLIT|INTLIT|ID|call_stm|LP expression RB;
// //key word
// INT     : 'int';
// FLOAT   : 'float';
// RETURN  : 'return';

// // Specific characters
// SM: ';';
// CM: ',';
// DOT: '.';
// LB: '{';
// RB: '}';
// LP: '(';
// RP: ')';
// LSB: '[';
// RSB:']';
// ADD: '+';
// SUB: '-';
// MUL: '*';
// DIV: '/';

// EQ: '=';

// ID:         [a-zA-Z]+;
// INTLIT:     [1-9][0-9]*|'0';
// FLOATLIT:   INTLIT[.]INTLIT;





WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;