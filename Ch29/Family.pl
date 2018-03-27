#S3C2 Laurel

male(gmh).
male(ymb).
male(yac).
male(tpz).
male(bob).
male(jerry).

female(laurel).
female(zdg).
female(jenny).
female(kris).
female(tmw).
female(zoe).

parent(gmh,laurel).
parent(ymb,zdg).
parent(yac,jenny).
parent(tpz,kris).
parent(bob,tmw).
parent(jerry,zoe).
parent(yac,jenny).
parent(bob,kris).
parent(tpz,zoe).



brother(X,Y):- 
	male(X),
	male(Y),
	parent(A,X),
	parent(A,Y),
	not(X=Y).

sister(X,Y):- 
	female(X),
	female(Y),
	parent(A,X),
	parent(A,Y),
	not(X=Y).

son(S,P):-
	parent(P,S),
	male(S).

daughter(X,Y):-
	parent(Y,X),
	female(Y).

mother(X,Y):-
	parent(X,Y),
	female(X).

married(X,Y):-
	parent(X,A),
	parent(Y,A),
	not(X=Y).

ancestor(X,Y):-
	parent(X,Y).

ancestor(X,Y):-
	parent(X,A),
	parent(A,Y).
