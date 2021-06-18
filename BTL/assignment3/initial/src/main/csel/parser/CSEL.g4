//	Pham Van Dat
//	1811892
grammar CSEL;

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



/*********************PARSER**********************/

program:declaration+ EOF ;
declaration: 		var_declare| constant_declare | func_declare ;
// 2 .Variable let
var_declare:	LET vars_list SEMI;
// 2.1 Variable declaration
vars_list:		var_typ_asg COMMA vars_list | var_typ_asg;
var_typ_asg:	ID array_ref?  (COLON data_types)? (ASSIGN exp)? ;//a = 5 | a:Interger = i+5 | a | a:Interger


//2.2 Constant declaration
constant_declare:	CONSTANT constant_id_list SEMI; // Constant $a_b: String = "day la vi du";

//constant_id_list:	constant_assign  COMMA constant_id_list |constant_assign ; // $a_b: String = "day la vi du", $a:int = 10
constant_id_list:	constant_assign  (COMMA constant_assign)*; // $a_b: String = "day la vi du", $a:int = 10
constant_assign :	ID_WITH_DOLLAR array_ref? (COLON data_types)? ASSIGN exp; //$a_b: String = "day la vi du"   => fragment ????

// 2.1.0 Array declaration
array_ref:			LSB index_op? RSB;
data_types:			NUMBER | STRING | BOOLEAN | JSON; // Number, String

//2.3 Function declaration
func_declare:		FUNCTION ID LP params_list? RP  LCB statementsList? RCB;
params_list:		param (COMMA param)* ;
param:              (ID | ID_WITH_DOLLAR ) array_ref?;

/********************* STATEMENTS ***********************/

stmt
	: var_declare 
	| constant_declare
	| assign_stmt
	| if_stmt
	| for_stmt
	| while_stmt 
	| brk_stmt
	| cont_stmt
	| call_stmt
	| ret_stmt
	;
// assign
assign_stmt:        (ID | exp7) ASSIGN exp SEMI;
// IF
if_stmt:		IF LP exp RP LCB statementsList? RCB  elseif_list? (else_func)? ;
elseif_list:	elseif_func + ;
elseif_func:	ELIF LP exp RP LCB statementsList? RCB;
else_func:		ELSE LCB statementsList? RCB;
// Vòng lặp
while_stmt:		WHILE LP exp RP LCB	 statementsList? RCB ;
for_stmt:		for_in_stmt |	for_of_stmt;
for_in_stmt:	FOR ID IN exp  LCB statementsList? RCB;
for_of_stmt:	FOR ID OF exp  LCB statementsList? RCB ;
// break, continue, return
brk_stmt:		BREAK SEMI ;
cont_stmt:		CONTINUE SEMI ;
ret_stmt:		ret_stmt_func | ret_stmt_proc ;
ret_stmt_proc:	RETURN SEMI ;
ret_stmt_func:	RETURN exp SEMI ;
// Call
call_stmt:		CALL LP ID COMMA LSB exps_list? RSB RP SEMI;
statementsList: stmt statementsList| stmt;

 
/********************* EXPRESSIONS ***********************/

exp : exp1 (ADDS|EQS) exp1
    | exp1;
exp1: exp2 relation exp2
    | exp2;
exp2: exp2 (AND | OR) exp3
    | exp3;
exp3: exp3 (ADD | SUB ) exp4
    | exp4;
exp4: exp4 (MUL| DIV | MOD) exp5
    | exp5;
exp5: NOT exp5
    | exp6;
exp6: SUB exp6
    | exp7;
exp7: exp7 LSB index_op RSB
    | exp7 key_op
    | exp8;
exp8: funcall
	| operands;


operands:			LP exp RP | ID | ID_WITH_DOLLAR | literal ;
relation:			EQ | NEQ | GT | LT | GTE | LTE ;

index_op:			exp | exp COMMA index_op;
key_op: 			LCB exp RCB
					| key_op LCB exp RCB ;

funcall: 		CALL LP ID COMMA LSB exps_list? RSB RP ;
exps_list:		exp (COMMA exp)*;	// 5,2

literal:		NUMBER_LIT | STRING_LIT | BOOLEAN_LIT | json_lit | array_lit;	//12.4e-3 |	"string" | True

/********************* LITERALS ***********************/

array_lit: LSB array_list? RSB;
array_list: literal COMMA array_list |literal;
// json
json_lit:			LCB json_elems_list? RCB;
json_elems_list:	json_elems COMMA json_elems_list| json_elems;
json_elems:			ID COLON literal;


NUMBER_LIT:Digit+ (Decpart? Expo? | Decpart Expo);

fragment Decpart: '.'Digit*;
fragment Digit : [0-9];
fragment Expo: [eE] (SUB|ADD)? Digit+;

// boolean
BOOLEAN_LIT:	TRUE | FALSE ;

// String
STRING_LIT: '"' STR_CHAR* '"'
    {
        self.text = self.text[1:-1];
    }
;

fragment STR_CHAR: STR_CHAR_NORMAL
        | STR_CHAR_QUOTE;
fragment STR_CHAR_NORMAL:~[\n\f\r'"\\]
               | ESC_SEQ;
fragment ESC_SEQ: '\\' [btnfr'\\];
fragment STR_CHAR_QUOTE: '\'"';

/********************* KEY WORDS **********************/

BREAK:      'Break';
CONTINUE:   'Continue';
IF:         'If';
ELIF:       'Elif';
ELSE:       'Else';
WHILE:      'While';
FOR:        'For';
OF:         'Of';
IN:         'In';
FUNCTION:   'Function';
LET:        'Let';
TRUE:       'True';
FALSE:      'False';
CALL:       'Call';
RETURN:     'Return';
NUMBER:     'Number';
BOOLEAN:    'Boolean';
STRING:     'String';
JSON:       'JSON';
ARRAY:      'Array';
CONSTANT:   'Constant';

/********************* OPERATORS **********************/

ADD:    '+';
SUB:    '-';
MUL:    '*';
DIV:    '/';
MOD:    '%';
NOT:    '!';
AND:    '&&';
OR :    '||';
ASSIGN:  '=';
EQ :    '==';
NEQ:    '!=';
LT :    '<' ;
GT :    '>' ;
LTE:    '<=';
GTE:    '>=';
ADDS:   '+.';
EQS:    '==.';

/******************** SEPARATORS **********************/

LP:     '(';
RP:     ')';
LSB:    '[';
RSB:    ']';
COLON:  ':';
DOT:    '.';
COMMA:  ',';
SEMI:   ';';
LCB: 	'{';
RCB: 	'}';
DF:		'"';


/******************** IDENTIFIERS *********************/

ID:     [a-z][_a-zA-Z0-9]*  ;
ID_WITH_DOLLAR: '$'[_a-zA-Z0-9]*;

/*********************** SKIP *************************/

WS :    [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines
BLOCK_COMMENT: '##' .*? '##' -> skip ;

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"'(STR_CHAR)* (EOF|[\n\f\r]){self.text=self.text[1:] };
ILLEGAL_ESCAPE: '"'(STR_CHAR)* '\\' ~([brnft] | '"' | '\\') { raise IllegalEscape(self.text[1:])};
UNTERMINATED_COMMENT: '##'('#'?(~[#])+)*;