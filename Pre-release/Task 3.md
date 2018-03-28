Task 3

S3C2 Laurel



3.1

    character(habib).
    charcater_type(habib,explorer).
    has_skill(habib,timetravel).
    pet(habib,fish).



3.2

    OnlyAPet(X,Y):-
    	character(X),
    	animal(Y).



3.3

    character(laurel).
    character(angelina).
    
    animal(dog).
    animal(rabbit).
    
    pet(laurel,dog).
    pet(angelina,rabbit).
    
    has_skill(laurel,run).
    has_skill(angelina,jump).



3.4

princess

jim

invisibility

jim



3.5

    pet(jim,X).
    
    has_skill(X,fly).
    
    skill(X).
    
    pet(M,N):-
    	character_type(T,M),
    	pet(T,N).
    type_pet(princess,X).


