{\rtf1\ansi\ansicpg936\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 # S3C2 Laurel\
\
Len([],0).\
Len([_|T],L):-\
      len(T,N),\
      L is N+1.\
\
Mymember(I,[I|_]).\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural
\cf0 Mymember(I,[J|T]):-\
      Mymember(I,T).\
\
Last(X,[X]).\
Last(X,[_|T]):-\
      Last(N,T),\
      X is N.\
\
Second_last(H,[H|T]):-\
      Len(X,T),\
      X is 1.\
Second_last(M,[_|T):-\
      Second_last(Y,T),\
      M is Y.\
\
FindK([A|_],1,A).\
FindK([_|T],M,N):-\
      FindK(T,X,N),\
      M is X+1.\
\
Number([],0).\
Number([_|T],N):-\
      Number(T,X),\
      N is X+1.\
\
Myappend([],L,L).\
Myappend([H|T],L,[H|R]):-\
      Myappend(T,L,R).\
\
Reverse([],X,X).\
Reverse([H|T],R,L):-\
      Reverse(T,R,[H|L]).\
\
Palindrome(X):-\
      Reverse(X,Y,[]),\
Y==X\
}