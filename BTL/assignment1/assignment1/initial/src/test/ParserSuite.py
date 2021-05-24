import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Let x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Let ;"""
        expect = "Error on line 1 col 4: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_var_gan_bien(self):
        input = """Let x = 8;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_var_sai(self):
        input = """Let x; y;"""
        expect = "Error on line 1 col 7: y"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_sai_var(self):
        input = """Let $a;"""
        expect = "Error on line 1 col 4: $a"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_var_thieu_dau_cham_phay(self):
        input = """Let m = n;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_var_mang(self):
        input = """Let a:Number;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_sai_dau_var(self):
        input = """Let a Number"""
        expect = "Error on line 1 col 6: Number"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_var_nhieu_bien(self):
        input = """Let a =2.E-4, b=9e-2, c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_gan_sai_var(self):
        input = """Let a != 1;"""
        expect = "Error on line 1 col 6: !="
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_var_sai_2(self):
        input = """Constant $arr[2] = [1,2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_bien_dau(self):
        input = """Let a = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_var_str(self):
        input = """Let a= "day la chuoi";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_var_gan(self):
        input = """Let a = a + b * c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_var_bth(self):
        input = """Let aBC = %True;"""
        expect = "Error on line 1 col 10: %"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_var_so(self):
        input = """let a;"""
        expect = "Error on line 1 col 0: let"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_var_constant(self):
        input = """Constant a = 5;"""
        expect = "Error on line 1 col 9: a"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_var_constant1(self):
        input = """Constant $a;"""
        expect = "Error on line 1 col 11: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_var_constant2(self):
        input = """Constant $a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_var_constant3(self):
        input = "Constant $a = 12.3;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_var_constant4(self):
        input = """Constant $a = b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_var_constant5(self):
        input = """Constant $a = $b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_var_constant6(self):
        input = """Constant $a = [5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_var_constant7(self):
        input = """Constant $a = a[8];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))
    # lỗi tiếp Error on line 1 col 24: [2]
    def test_var_constant8(self):
        input = """Constant $a = Call(foo, [2]);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))
    # lỗi Error on line 1 col 17: ["Name"]
    def test_var_constant9(self):
        input = """Constant $a =json["Name"];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_var_constant10(self):
        input = """Constant $a = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))
    # lai loi Error on line 1 col 5: [10]
    def test_array_declare(self):
        input = """Let a[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))
    # lỗi Error on line 1 col 5: [2]
    def test_array_declare1(self):
        input = """Let a[2]:Number;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_array_declare2(self):
        input = """Constant $a[10] = 7;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_array_declare3(self):
        input = """Let a[True];"""
        expect = """Error on line 1 col 6: True"""
        self.assertTrue(TestParser.checkParser(input, expect, 231))
    # loi
    def test_json(self):
        input = """
        Let a = {
            name: 6,
            address: "Chinese Forbidden City",
            surface: 10.2,
            people: ["Empress Xiaoxianchun", "Yongzheng Emperor"]
        };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_json2(self):
        input = """Function foo(a, b) {
                        x = 4>0;
                        y= !a + b % c * -d;
                        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_contant_nhieu_bien(self):
        input = """
                Constant $a = True, $b=6.E-2;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))
    # loi Error on line 2 col 29: 5
    def test_contant3(self):
        input = """
                Constant $a =5;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))
    # loi Error on line 2 col 16: If
    def test_if_x(self):
        input = """
                Function foo(a, b) {
                    If(a==b){
                        Return true;
                    }
                    Else{
                        Return false;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))
     # lỗi Error on line 2 col 16: While
    def test_if_and(self):
        input = """
                Function foo(a[5], b) {
                    If(a==b){
                        Return True;
                    }
                    Elif(a>20){
                        a = 20;
                    }
                    Elif(a){
                        a = 210;
                    }
                    Else{
                        Return False;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))
    
    def test_if_hoac(self):
        input = """
                Function foo(a[5], b) {
                    If(a==b){
                        Return True;
                    }
                    Elif(a>20){
                        a = 20;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_if_ham(self):
        input = """
                Let x;
                Function foo(a[5], b) {
                    Let i = 0;
                    While (i < 5) {
                        a[i] = b + 1;
                        Let u: Number = i + 1;
                        If (a[u] == 10) {
                            Return a[i];
                        }
                    }
                    Return -1;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_if_fail(self):
        input = """Let a[2+5]:Number;"""
        expect = "Error on line 1 col 7: +"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_thieu_then(self):
        input = """Function foo(a, b) {
                        f = a > b < c != d == e;}

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_ham_k_ts(self):
        input = """
                Let x;
                Function foo{
                    Let b =a;
                    }
                """
        expect = "Error on line 3 col 28: {"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_if_sai_dk(self):
        input = """
                Let x;
                Function foo(){
                    Let b =a;
                    Return b;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_if_sai_dk2(self):
        input = """
                Let x;
                Function foo(){
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_if_bth(self):
        input = """
                Let x;
                Function foo(){
                    Constant $js ;
                    Return js;
                }
                """
        expect = "Error on line 4 col 33: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_sai_trong_if(self):
        input = """
                Let x;
                Function foo(){
                    Let arr[] = [3];
                    Return arr;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_if_dung(self):
        input = """
                Function foo();
                """
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_arr1(self):
        input = """
                Let x;
                Function foo(){
                    Let arr[4] = [5];
                    Return arr;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_arr(self):
        input = """
                Let x;
                Function foo(){
                    Let arr[4] = [2,3];
                    Return arr;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_a_sub(self):
        input = """
                Let x;
                Function foo(){
                    Function foo(){
                        Return a;
                    }
                    Call(foo2, [b,c]);
                }
                
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_for(self):
        input = """
                Function foo(){
                    Return "tra ve 1 chuoi";
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_for2(self):
        input = """
                Let x;
                Function foo(){
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_for_chua_gan(self):
        input = """
                Let x;
                Function foo(){
                    Constant $cons = True;
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_for_thieu_gioi_hang(self):
        input = """
                Let x;
                Function foo(){
                    Let abc;
                    While(True){
                        abc=abc+1;
                    }
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_for_true(self):
        input = """
                Let x;
                Function foo(){
                    Let abc;
                    While(){
                        abc=abc+1;
                    }
                    Return True;
                }
                """
        expect = "Error on line 5 col 26: )"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_while_dung(self):
        input = """
                ##cmt
                  cmt
                  cmt
                  cmt##
                Let x;
                Function foo(){
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_while_dung2(self):
        input = """
                Function foo(){
                    Let abc;
                    While(2){
                        abc=abc+1;
                    }
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_while_no_do(self):
        input = """
                Function foo(){
                    Let abc;
                    While(2+2){
                        abc=abc+1;
                    }
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_while_sai_dk(self):
        input = """
                Function foo(){
                    a[Call(foo, [2])] = a[b["name"]["first"]] + 4;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_while_thieu_cham(self):
        input = """
                Function foo(){
                    Let abc;
                    While(Call(foo,[2,3+x])){
                        abc=abc+.1;
                    }
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_while_thieu_cham_phay(self):
        input = """
                Function foo(){
                    Let abc;
                    While(arr[2]){
                        abc=abc+1;
                    }
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_while_in_while(self):
        input = """
                Function foo(){
                    Let abc;
                    While(js["name"]){
                        abc=abc+1;
                    }
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_if_in_while(self):
        input = """
                Function foo(){
                    Let a = js["name"];
                    Return a;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_while_do(self):
        input = """Function foo(a, b) {
                    Let a[5],b[5],c[5];
                    Let a[5],b[5],c;
                    
                        c = a[] + b[1]; 
                }
        """
        expect = "Error on line 5 col 30: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_while_sai(self):
        input = """Function foo(a, b) {
                    js["name"] = 3;
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_endwhile(self):
        input = """Function foo(a, b) {
                    js["name"] =arr[10,3];
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_sai_dk_while(self):
        input = """Function foo(a, b) {
                        x = True;
                        y = False;
                        z = a > b <= c != d == e;
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_do_while(self):
        input = """
                Function foo(){
                    Let abc;
                    While(!!True){
                        abc=abc+1;
                    }
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_do_while2(self):
        input = """
                Function foo(){
                    Let abc;
                    While(a+b==c){
                        abc=abc+1;
                    }
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_do_while_thieu_hai_cham(self):
        input = """
                Function foo(){
                    Let abc;
                    For i In [1,2,3,4,5]{
                        abc= abc +1;
                    }
                    Return abc;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_do_while_du(self):
        input = """
                Function foo(){
                    Let abc;
                    For i In $arr{
                        abc= abc +1;
                    }
                    Return abc;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_do_while_du2(self):
        input = """
                Function foo(){
                    Let abc;
                    For i In {a:1,b:2,c:3}{
                        abc= abc + 1;
                    }
                    Return abc;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_do_while_sai_dk(self):
        input = """
                Function foo(){
                    Let abc;
                    For i Of {a:1,b:2,c:3}{
                        abc= abc +1;
                    }
                    Return abc;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_do_while_du_dau(self):
        input = """
                Function foo(){
                    Let abc;
                    For i Of Call(foo,[2]){
                        abc= abc +1;
                    }
                    Return abc;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_do_while_thieu_while(self):
        input = """
                Function foo(){
                    Let abc;
                    For i Of js{
                        abc= abc +1;
                    }
                    Return abc;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_do_while_thieu_do(self):
        input = """
                Function foo(){
                    Call(foo, [2 + x, 4 / y]);
                    Break;
                    Return abc;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_dowhile_in_dowhile(self):
        input = """
                Let js = {};
                Let a[] = [1,2,[3,4]];
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_callfun(self):
        input = """
                Function foo(){
                    Return Call(foo,[2]);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_return02(self):
        input = """
            Function foo(){    
                Return !True;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_return01(self):
        input = """
                Function foo(Call(foo,[4])){    
                Return True;
                }
                """
        expect = "Error on line 2 col 29: Call"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_json0(self):
        input = """
                Let a:JSON = {
                    name: "Yanxi Place",
                    address: "Chinese Forbidden City",
                    surface: 10.2,
                    people: ["Empress Xiaoxianchun", "Yongzheng Emperor"]
                    };
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_json01(self):
        input = """
                Let a = {
                    name: "Yanxi Place",
                    address: "Chinese Forbidden City",
                    surface: 10.2,
                    people: ["Empress Xiaoxianchun", "Yongzheng Emperor"]
                    };
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_json002(self):
        input = """
                Let a = {
                    name= "Yanxi Place",
                    address: "Chinese Forbidden City",
                    surface: 10.2,
                    people: ["Empress Xiaoxianchun", "Yongzheng Emperor"]
                    };
                """
        expect = "Error on line 3 col 24: ="
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_json03(self):
        input = """
                Let a = {
                    : "Yanxi Place",
                    address: "Chinese Forbidden City",
                    surface: 10.2,
                    people: ["Empress Xiaoxianchun", "Yongzheng Emperor"]
                    };
                """
        expect = "Error on line 3 col 20: :"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_arr03(self):
        input = """Function foo(a, b) {
                         c = [1.,2];
                         d = a || b && c;}

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_for01(self):
        input = """
                Let x;
                Function foo(){
                    Let abc;
                    While(a){
                        For i In arr{
                            For k Of js{
                                
                            }
                        }
                    }
                    Return True;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_while02(self):
        input = """
                Function foo(a[5], b) {
                    Let i = 0;
                    While (i < 5) {
                        a[i] = b + 1;
                        Let u: Number = i + 1;
                        If (a[u] == 10) {
                            Return a[i];
                        }
                    }
                    Return -1;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_whil(self):
        input = """
                Function foo(a[5], b) {
                    Let i = 0;
                    While (i < 5) {
                        a[i] = b + 1;
                        Let u: Number = i + 1;
                        If (a[u] == 10) {
                            Return a[i];
                        }
                    }
                    Return {name:"dat",age:4};
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_writeln(self):
        input = """
                Function foo(a[5], b) {
                    Let i = 0;
                    While (i < 5) {
                        a[i] = b + 1;
                        Let u: Number = i + 1;
                        If (a[u] == c[10]) {
                            Return a[i];
                        }
                    }
                    Return {name:"dat",age:4};
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_print(self):
        input = """Let arr[10] = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_read(self):
        input = """Let js , arr[10],a="pham";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_json10(self):
        input = """Let $js;"""
        expect = "Error on line 1 col 4: $js"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_int2(self):
        input = """Let r[10] = 10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_float(self):
        input = """Let r[] = 10, v[2]=[3,4];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_float2(self):
        input = """Let r = 10, v;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_float_loi(self):
        input = """
                Function foo(){
                    Let a:JSON = {
                    name: "Yanxi Place",
                    address: "Chinese Forbidden City",
                    surface: 10.2,
                    people: ["Empress Xiaoxianchun", "Yongzheng Emperor"]
                    };
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_var_so4(self):
        input = """Let a = arr[2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_var_so3(self):
        input = """Let a = arr["Name"];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_var_so1(self):
        input = """Let a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_var_so2(self):
        input = """
            Function foo(){
            Let x=[5]+[5,6];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))
