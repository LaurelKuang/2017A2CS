# Pre-release Material

S3C2 Laurel Kuang



1.1

JSP structure diagrams help to design a program, as it gives a structure of the data the intended program will handle.



1.2

An asterisk represents repetition, making the components repeat. It consists of one part that repeats zero or more times.

A circle represents selection, where only one is chosen. It consists of two or more parts, only one of which is selected.



1.3

WHILE TRUE

​    CALL ReadSalary()

​    IF Salary>50

​        THEN

​            IF Salary>=90

​                THEN

​                    Role←ProjectManager

​                 ELSE

​                    Role←LeadDeveloper

​            ENDIF

​         ELSE

​             Role←Manager

​     ENDIF    

ENDWHILE   



1.4

​                     Salary>50

FALSE                                  True

Assign Manager             Salary>70

​                              FALSE                  TRUE

​                     Lead Developer       Salary>=90

​                                             FALSE                     TRUE

​                                           Consultant             Project Manager



1.5

WHILE TRUE

​    CALL ReadSalary()

​    IF Salary>50

​        THEN

​            IF Salary>70

​                THEN

​                    IF Salary>=90

​                        THEN

​                            Role←ProjectManager

​                        ELSE

​                            Role←Consultant

​                    ENDIF

​               ELSE

​                   Role←LeadDeveloper

​             ENDIF    

​        ELSE

​            Role←Manager

​    ENDIF

ENDWHILE   



1.6

```python
def Role(Salary):
    if Salary>50:
        if Salary>70:
            if Salary>=90:
                RoleTitle=ProjectManager
            else:
                RoleTitle=Consultant
        else:
            RoleTitle=LeadDeveloper
    else:
        RoleTitle=Manager
    return RoleTitle


```

