; Helloworld.j

; Generated by ClassFileAnalyzer (Can)
; Analyzer and Disassembler for Java class files
; (Jasmin syntax 2, http://jasmin.sourceforge.net)
;
; ClassFileAnalyzer, version 0.7.0 


.bytecode 55.0
.source Helloworld.java
.class public Helloworld
.super java/lang/Object

.method public <init>()V
  .limit stack 1
  .limit locals 1
  .line 1
  0: aload_0
  1: invokespecial java/lang/Object/<init>()V
  4: return
.end method

.method public static main([Ljava/lang/String;)V
  .limit stack 2
  .limit locals 3
  .line 3
  0: bipush 11
  2: istore_1
  .line 4
  3: iload_1
  4: invokestatic java/lang/Integer/toString(I)Ljava/lang/String;
  7: astore_2
  .line 5
  8: getstatic java/lang/System/out Ljava/io/PrintStream;
  11: aload_2
  12: invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
  .line 6
  15: return
.end method

