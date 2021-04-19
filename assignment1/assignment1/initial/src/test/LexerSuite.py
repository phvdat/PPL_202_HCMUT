import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Let","Let,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Let x;","Let,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string1(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_id(self):
        self.assertTrue(TestLexer.checkLexeme("pham van dat", "pham,van,dat,<EOF>", 108))

    def test_id2(self):
        self.assertTrue(TestLexer.checkLexeme("1hai", "1,hai,<EOF>", 109))

    def test_id3(self):
        self.assertTrue(TestLexer.checkLexeme("Ppl", "Error Token P", 110))

    def test_id4(self):
        self.assertTrue(TestLexer.checkLexeme("ppl", "ppl,<EOF>", 111))

    def test_id5(self):
        self.assertTrue(TestLexer.checkLexeme("$ppl", "$ppl,<EOF>", 112))
    
    def test_id6(self):
        self.assertTrue(TestLexer.checkLexeme("$$ppl", "$,$ppl,<EOF>", 113))

    def test_id7(self):
        self.assertTrue(TestLexer.checkLexeme("_1ppl", "Error Token _", 114))
    
    def test_id8(self):
        self.assertTrue(TestLexer.checkLexeme("_$1ppl", "Error Token _", 115))

    def test_id9(self):
        self.assertTrue(TestLexer.checkLexeme("%#1ppl", "%,Error Token #", 116))
    
    def test_id10(self):
        self.assertTrue(TestLexer.checkLexeme("pp%*&l", "pp,%,*,Error Token &", 117))
        
    def test_numberlit(self):
        self.assertTrue(TestLexer.checkLexeme("12", "12,<EOF>", 118))
        
    def test_numberlit1(self):
        self.assertTrue(TestLexer.checkLexeme("12.", "12.,<EOF>", 119))
        
    def test_numberlit2(self):
        self.assertTrue(TestLexer.checkLexeme("12.34", "12.34,<EOF>", 120))
        
    def test_numberlit3(self):
        self.assertTrue(TestLexer.checkLexeme("12e-4", "12e-4,<EOF>", 121))

    def test_numberlit4(self):
        self.assertTrue(TestLexer.checkLexeme("12.e-4", "12.e-4,<EOF>", 122))

    def test_numberlit5(self):
        self.assertTrue(TestLexer.checkLexeme("12.34e-4", "12.34e-4,<EOF>", 123))

    def test_numberlit6(self):
        self.assertTrue(TestLexer.checkLexeme(".34e-4", ".,34e-4,<EOF>", 124))

    def test_numberlit7(self):
        self.assertTrue(TestLexer.checkLexeme("e-4", "e,-,4,<EOF>", 125))

    def test_numberlit8(self):
        self.assertTrue(TestLexer.checkLexeme("-12.e-4", "-,12.e-4,<EOF>", 126))

    def test_numberlit9(self):
        self.assertTrue(TestLexer.checkLexeme("+12.e-4", "+,12.e-4,<EOF>", 127))

    def test_boollit(self):
        self.assertTrue(TestLexer.checkLexeme("True", "True,<EOF>", 128))

    def test_boollit1(self):
        self.assertTrue(TestLexer.checkLexeme("False", "False,<EOF>", 129))

    def test_boollit2(self):
        self.assertTrue(TestLexer.checkLexeme("TRUE", "Error Token T", 130))

    def test_boollit3(self):
        self.assertTrue(TestLexer.checkLexeme("FALSE", "Error Token F", 131))

    def test_arraylit(self):
        self.assertTrue(TestLexer.checkLexeme("[ True, False ]", "[,True,,,False,],<EOF>", 132))

    def test_arraylit1(self):
        self.assertTrue(TestLexer.checkLexeme("[[True], [False] ]", "[,[,True,],,,[,False,],],<EOF>", 133))

    def test_arraylit2(self):
        self.assertTrue(TestLexer.checkLexeme("[[True], False ]", "[,[,True,],,,False,],<EOF>", 134))

    def test_variable_declare_10(self):
        self.assertTrue(TestLexer.checkLexeme("chi ak''","chi,ak,Error Token '",135))
    
    def test_stringlit(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab\t" ""","Unclosed String: This is a string containing tab",136))

    def test_illegal(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abch def"  ""","""abch def,<EOF>""",137))

    def test_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme("## jvdj/*a7236#//#$4&*##","<EOF>",138))

    def test_line_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("## Pham van dat\naa##","<EOF>",139))
    
    def test_comment_(self):
        self.assertTrue(TestLexer.checkLexeme("## x=a+117%5\n\t##","<EOF>",140))
    
    def test_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("## x=a+117%5\n##","<EOF>",141))
    
    def test_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("## Pham van dat##aa","aa,<EOF>",142))
    
    
    
    
    
    
    
    
    
    # hoicham
    def test_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme("## Pham v##an dat##","an,dat,Error Token #",143))
    
    def test_line_comment_6(self):
        self.assertTrue(TestLexer.checkLexeme("# # Pham van dat# #aa","Error Token #",144))
    
    def test_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("Break Continue If","Break,Continue,If,<EOF>",145))
    
    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("Elif Else While","Elif,Else,While,<EOF>",146))
    
    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("Function Let Number","Function,Let,Number,<EOF>",147))
    
    def test_operator(self):
        self.assertTrue(TestLexer.checkLexeme("+-*/%<<=>>=!===","+,-,*,/,%,<,<=,>,>=,!=,==,<EOF>",148))
    
    def test_seperator(self):
        self.assertTrue(TestLexer.checkLexeme("[](){};.:,","[,],(,),{,},;,.,:,,,<EOF>",149))

    def test_var(self):
        self.assertTrue(TestLexer.checkLexeme("Let x","Let,x,<EOF>",150))
    
    def test_var2(self):
        self.assertTrue(TestLexer.checkLexeme("Let Foo","Let,Error Token F",151))
    
    def test_var6(self):
        self.assertTrue(TestLexer.checkLexeme("Let $x","Let,$x,<EOF>",152))
        
    def test_var3(self):
        self.assertTrue(TestLexer.checkLexeme("Constant $x","Constant,$x,<EOF>",153))
            
    def test_var4(self):
        self.assertTrue(TestLexer.checkLexeme("Constant abc","Constant,abc,<EOF>",154))

    def test_var5(self):
        self.assertTrue(TestLexer.checkLexeme("Constant Abc","Constant,Error Token A",155))

    def test_key_word_1(self):
        self.assertTrue(TestLexer.checkLexeme("Boolean,Return,Break","Boolean,,,Return,,,Break,<EOF>",156))
    
    def test_keywords_2(self):
        self.assertTrue(TestLexer.checkLexeme("Let dat.pham2000@hcmut.edu.vn","Let,dat,.,pham2000,Error Token @",157))
    
    def test_variable_declare_1(self):
        self.assertTrue(TestLexer.checkLexeme("Let x,a[5]; Let x=5E3;","Let,x,,,a,[,5,],;,Let,x,=,5E3,;,<EOF>",158))
    
    def test_variable_declare_2(self):
        self.assertTrue(TestLexer.checkLexeme("String y=123","String,y,=,123,<EOF>",159))
    
    def test_variable_declare_3(self):
        self.assertTrue(TestLexer.checkLexeme("str='monday~'","str,=,Error Token '",160))
    
    def test_variable_declare_4(self):
        self.assertTrue(TestLexer.checkLexeme("1Let a=x==9","1,Let,a,=,x,==,9,<EOF>",161))    
    
    def test_variable_declare_5(self):
        self.assertTrue(TestLexer.checkLexeme("String str=2233","String,str,=,2233,<EOF>",162))    
    
    def test_variable_declare_6(self):
        self.assertTrue(TestLexer.checkLexeme("Let a[2][7];","Let,a,[,2,],[,7,],;,<EOF>",163))    
    
    def test_variable_declare_7(self):
        self.assertTrue(TestLexer.checkLexeme("bibang=int a=8;","bibang,=,int,a,=,8,;,<EOF>",164))    
    
    def test_variable_declare_8(self):
        self.assertTrue(TestLexer.checkLexeme("1+1=int a(foo(a[1]))+","1,+,1,=,int,a,(,foo,(,a,[,1,],),),+,<EOF>",165))    
    
    def test_variable_declare_9(self):
        self.assertTrue(TestLexer.checkLexeme("@abc hcmut , inflash","Error Token @",166))    
    
    def test_variable_declare_11(self):
        self.assertTrue(TestLexer.checkLexeme("*/+-!","*,/,+,-,!,<EOF>",167))

    def test_namsinh(self):
        self.assertTrue(TestLexer.checkLexeme("1999", "1999,<EOF>", 168))

    def test_loiA(self):
        self.assertTrue(TestLexer.checkLexeme("AFK", "Error Token A", 169))

    def test_bro(self):
        self.assertTrue(TestLexer.checkLexeme("bro", "bro,<EOF>", 170))

    def test_family(self):
        self.assertTrue(TestLexer.checkLexeme("family", "family,<EOF>", 171))

    def test_ham_la(self):
        self.assertTrue(TestLexer.checkLexeme("-3-9*7", "-,3,-,9,*,7,<EOF>", 172))

    def test_dau_la(self):
        self.assertTrue(TestLexer.checkLexeme(".,.,", ".,,,.,,,<EOF>", 173))

    def test_dau_kep(self):
        self.assertTrue(TestLexer.checkLexeme("><", ">,<,<EOF>", 174))

    def test_loi_(self):
        self.assertTrue(TestLexer.checkLexeme("_ab9", "Error Token _", 175))

    def test_bien(self):
        self.assertTrue(TestLexer.checkLexeme("ab9_9_9", "ab9_9_9,<EOF>", 176))

    def test_all_10(self):
        self.assertTrue(TestLexer.checkLexeme("a*b*c","a,*,b,*,c,<EOF>",177))

    def test_all_11(self):
        self.assertTrue(TestLexer.checkLexeme(""" &&==!=& ""","&&,==,!=,Error Token &",178))

    def test_all_12(self):
        self.assertTrue(TestLexer.checkLexeme(""" a<=b!c=d> ""","a,<=,b,!,c,=,d,>,<EOF>",179))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef""","""Unclosed String: abcdef""",180))
    
    def test_all_14(self):
        self.assertTrue(TestLexer.checkLexeme(""" "11-05=""99" ""","11-05=,99,<EOF>",181))

    def test_all_15(self):
        self.assertTrue(TestLexer.checkLexeme("a+-b/d*e/*tr+ew+*/tr+%%*/t/f*+d","a,+,-,b,/,d,*,e,/,*,tr,+,ew,+,*,/,tr,+,%,%,*,/,t,/,f,*,+,d,<EOF>",182))

    def test_all_16(self):
        self.assertTrue(TestLexer.checkLexeme(""" "i am Datt " ""","i am Datt ,<EOF>",183))

    def test_all_17(self):
        self.assertTrue(TestLexer.checkLexeme("!#$%^&*()","!,Error Token #",184))

    def test_all_18(self):
        self.assertTrue(TestLexer.checkLexeme("Let main(){if(x==5) y=10;}","Let,main,(,),{,if,(,x,==,5,),y,=,10,;,},<EOF>",185))

    def test_all_19(self):
        self.assertTrue(TestLexer.checkLexeme(""" (b==c) if (x==0) b>a else -a=2""","(,b,==,c,),if,(,x,==,0,),b,>,a,else,-,a,=,2,<EOF>",186))

    def test_all_20(self):
        self.assertTrue(TestLexer.checkLexeme("delta=b^2-4*a*c","delta,=,b,Error Token ^",187))

    def test_all_21(self):
        self.assertTrue(TestLexer.checkLexeme("if(x1=0) x2=-x3","if,(,x1,=,0,),x2,=,-,x3,<EOF>",188))

    def test_all_22(self):
       self.assertTrue(TestLexer.checkLexeme("int a,b,c; a^2+b^2=c^2;","int,a,,,b,,,c,;,a,Error Token ^",189))

    def test_all_23(self):
        self.assertTrue(TestLexer.checkLexeme("a<b+c if(abc=triangle)","a,<,b,+,c,if,(,abc,=,triangle,),<EOF>",190))
    
    def test_all_24(self):
        """test normal string with escape 1"""
        self.assertTrue(TestLexer.checkLexeme(""""ab ?'"c\\n def"  ""","""ab ?'"c\\n def,<EOF>""",191))

    def test_multiline_comment(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme("""##andn\n#anc\n#ahu\n##  ""","""<EOF>""",192))
    
    def test_boolean(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme("""True False""","""True,False,<EOF>""",193))

    def test_json(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme("""{ name: "VAN DAT", \n  age: 21  \n}""","""{,name,:,VAN DAT,,,age,:,21,},<EOF>""",194))
  
    def test_unlitmited_comt(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme("""##abc\n#a\n#""","""Unterminated Comment""",195))
    
    def test_unclosecmt(self):
         self.assertTrue(TestLexer.checkLexeme(""" ##ab  """, """Unterminated Comment""", 196))
  
    def test_array(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme("""[5     ,[5,6]]""","""[,5,,,[,5,,,6,],],<EOF>""",197))

    def test_all_28(self):
        self.assertTrue(TestLexer.checkLexeme("break; continue;","break,;,continue,;,<EOF>",198))

    def test_all_29(self):
        self.assertTrue(TestLexer.checkLexeme(";_{}if break;",";,Error Token _",199))

    def test_all_31(self):
        self.assertTrue(TestLexer.checkLexeme("123=/*2=","123,=,/,*,2,=,<EOF>",200))
