{\rtf1\ansi\ansicpg936\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\froman\fcharset0 Times-Roman;\f1\ftech\fcharset77 Symbol;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 # S3C2 Laurel Kuang\
\
1a\
\pard\pardeftab720
\cf0 \expnd0\expndtw0\kerning0
Iteration consists of statements that repeat zero or more times. \
Recursion is a function or procedure defined in terms of itself.\
\
1b\
One of the advantages is that recursive subroutines are simpler and shorter than other subroutines that are not recursive. \
One of the disadvantages is that \expnd0\expndtw0\kerning0
recursive subroutines may occupy too much memory space when the recursion is executed for many times.\
\
2a\
A function or procedure defined in terms of itself.\expnd0\expndtw0\kerning0
\
\
2b\
Call Number        Procedure Call        Exponent=0          Result               Return\
1                           Power(2,4)                  False                 \
2\expnd0\expndtw0\kerning0
                           Power(2,3)                  False\expnd0\expndtw0\kerning0
\
3\expnd0\expndtw0\kerning0
                           Power(2,2)                  False\expnd0\expndtw0\kerning0
\
4\expnd0\expndtw0\kerning0
                           Power(2,1)                  False\expnd0\expndtw0\kerning0
\
5\expnd0\expndtw0\kerning0
                           Power(2,0)                  True                     1                        1\expnd0\expndtw0\kerning0
\
(4)                         Power(2,1)                                       2*Power(2,0)           2\
(3)\expnd0\expndtw0\kerning0
                         Power(2,2)                                       2*Power(2,1)           4\expnd0\expndtw0\kerning0
\
(2)\expnd0\expndtw0\kerning0
                         Power(2,3)                                       2*Power(2,2)           8\expnd0\expndtw0\kerning0
\
(1)\expnd0\expndtw0\kerning0
                         Power(2,4)                                       2*Power(2,3)          16\
\
2c\
Every time the procedure of \'93Power\'94 is called, the return address and local variable are stored in the stack. When the base case of \'93Exponent=0\'94 turns to be true, the result of Power(2,0) is stored in the stack. As the procedure calls unwind, the return return address and local variable are taken off the stack. The procedure calls stop unwinding when Power(2,4) is returned.\
\
2e\
FUNCTION Power (Base: INTEGER, Exponent: INTEGER) RETURN INTEGER\
    Result 
\f1 \uc0\u8592 
\f0  1\
    WHILE Exponent>0\
          Result 
\f1 \uc0\u8592  
\f0 Result*Base\
          Exponent 
\f1 \uc0\u8592  
\f0 Exponent-1\
    ENDWHILE\
    RETURN Result\
ENDFUNCTION\
\
2f i\
Non-recursive function will not occupy too much memory space when it is executed for many times.\
\
2f ii\
Recursive function is simpler and shorter than other non-recursive functions, especially under mathematical circumstances which are recursive originally.\
\
3a i\
Line 04\
\
3a ii\
Line 06\
\
3b\
Call Number        Procedure Call         n=0 OR n=1                       Result                          Return\
1                           Fibonacci(4)                 False               \
2                           Fibonacci(3)                 False                \
3                           Fibonacci(2)                 False                  \
4                           Fibonacci(1)                 True                                  1                                     1\
5                           Fibonacci(0)                 True                                  1                                     1\
(3)                        Fibonacci(2)                                        Fibonacci(1)+ Fibonacci(0)              2\
6                           Fibonacci(1)                 True                                  1                                     1              \
(2)                         Fibonacci(3)                                       Fibonacci(2)+ Fibonacci(1)              3                \
7                           Fibonacci(2)                 False                                      \
8                           Fibonacci(1)                 True                                  1                                     1\
9                           Fibonacci(0)                 True                                  1                                     1\
(7)                         Fibonacci(2)                                        Fibonacci(1)+ Fibonacci(0)             2\
(1)                         Fibonacci(4)                                        Fibonacci(3)+ Fibonacci(2)             5\
\
\
\
}