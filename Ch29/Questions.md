## Chapter 29 Exam-style Questions

S3C2 Laurel

1

a  i

```python
cityin(london,uk).
```

a ii

```python
iVisited(strasbourg).
```



1

b

```python
chile, argentina
```



1

c

```python
countriesIVisited(Country) :-
	iVisited(City),
	cityIn(City,Country).
```



2

a  i

clause 01

a  ii

clause 15



2

b  i

Who=jack.

b  ii

False

b  iii

False



2

c  i

```python
qualifiedDriver(Driver,car).
```



c ii

```python
theoryOnly(X) :-
	passedTheoryTest(X),
	not(passedDrivingTest(X)).
```



2

d

Clause 11 (true), clause 01 (instantiates L as 18), clause 05 (instantiates A as 17), clause 15 ( A >= L is false) result is false.