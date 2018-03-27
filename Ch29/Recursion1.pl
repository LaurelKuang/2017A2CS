{\rtf1\ansi\ansicpg936\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 factorial(0,1).\
factorial(N,F):-\
           X is N-1,\
           factorial(X,Y),\
           F is N * Y.\
\
bunnyEars(0,0).\
bunnyEars(N,B):-\
           X is N-1,\
           bunnyEars(X,Y),\
           B is Y+2.\
\
fibonacci(0,0).\
fibonacci(1,1).\
fibonacci(2,1).\
fibonacci(N,F):-\
           X is N-1,\
           Y is N-2,\
           fibonacci(X,A),\
           fibonacci(Y,B),\
           F is A+B.\
\
even(X):-\
           0 is mod(X,2).\
odd(X):-\
           not(even(X)).\
\
bunnyEars2(0,0).\
bunnyEars2(N,B):-\
           even(N),\
           X is N-1,\
           bunnyEars2(X,A),\
           B is A+3.\
bunnyEars2(N,B):-\
           odd(N)\
           X is N-1,\
           bunnyEars2(X,A),\
           B is A+2.\
\
triangle(0,0).\
triangle(N,T):-\
	  X is N-1,\
	  triangle(X,A),\
	  T is A+N.\
\
sumDigits(N,S):-\
	  0 is N//10,\
	  S is N.\
sumDigits(N,S):-\
	  A is N//10,\
	  B is mod(N,10),\
	  sumDigits(A,C),\
	  S is B+C.\
\
count7(0,0).\
count7(N,C):-\
	  0 is N//10,\
	  7 is N,\
	  C is 1.\
count7(N,C):-\
          0 is N//10,\
	  7 is not N,\
	  C is 0.\
count7(N,C):-\
	  0 is not N//10,\
	  7 is mod(N,10),\
	  A is N//10,\
	  count7(A,D),\
	  C is 1+D.\
count7(N,C):-\
	  0 is not N//10,\
	  7 is not mod(N,10), \
	  A is N//10,\
	  count7(A,D),\
	  C is D.\
\
\
\
\
\
\
\
\
\
\
}