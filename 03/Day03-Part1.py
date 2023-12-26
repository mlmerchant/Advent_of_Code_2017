#!/bin/env python3

challenge = 361527

x=0
y=0

count=0
heading='R'
jump=2

def left():
    global heading
    if heading == 'R':
        heading = 'U'
    elif heading == 'U':
	    heading = 'L'
    elif heading == 'L':
        heading = 'D'
    else:
        heading = 'R'

def move():
    global x
    global y
    global count
    if heading == 'U':
        y += 1
    elif heading == 'D':
        y -= 1
    elif heading == 'R':
        x += 1
    else:
        x -= 1
    count += 1
    if count == challenge:
        print(abs(x )+abs( y) - 1)
        exit()
    
move()
left()
move()
left()

while True:
    for _ in range(jump):
	    move()
    left()
    for _ in range(jump):
	    move()
    left()
    jump += 1
	
	# 326 is the correct answer!