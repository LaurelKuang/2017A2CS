# S3C2 Laurel Kuang

def Events():
    print("A:PressStartButton B:EnterPin C:ActivateSensor")
    
def PressStartButton(state):
    if state==SystemInactive:
        state=SystemActive
    print(state)
    return state

def EnterPin(state, timer):
    if state==SystemActive:
        state=SystemInactive
    elif state==AlertMode:
        state=SystemInactive
        timer=0
    elif state==AlarmBellRinging:
        state=SystemInactive
    print(state)
    return state
    return timer

def ActivateSensor(state):
    if state==SystemActive:
        state=AlertMode
    print(state)
    return state

def 2MinutesPass():
    for i in range(240):
        print(end="")

def Timer(state, timer):
    if state==AlertMode:
        timer=timer+1
    return timer

def Bell(state, timer):
    if state==AlertMode and timer==2:
        state=AlarmBellRinging
    print(state)

timer=0
state=SystemInactive
Events()
Event=input("Enter the event please.")
if Event=="A":
    state=PressStartButton(state)
elif Event=="B":
    state,timer=EnterPin(state, timer)
elif Event=="C":
    state=ActivateSensor(state)
2MinutesPass()
timer=Timer(state, timer)
state=Bell(state, timer)





