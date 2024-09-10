""" 
in tutle center index is 0,0 
and like x , y axis rest index also



turtle_screen_object.tracer(0)  # line disables automatic screen updates.
By default, turtle graphics will update the screen after each turtle movement, which can result in flickering and slow performance for more complex drawings or animations. By turning off automatic updates with wn.tracer(0), you can manually update the screen when needed using the wn.update() function. 

turtle_screen_object.listen() #  function is used to set up window to listen for keyboard input
turtle_screen_object.onkeypress( command_function , key)


"""




import turtle 
skk = turtle.Turtle()

wn = turtle.Screen()

wn.title("Pong by Kumar")
wn.bgcolor("grey")
wn.setup(width=800, height=600)

""" 
Turtle()	        None	            Creates and returns a new turtle object
forward()	        amount	            Moves turtle forward by the specified amount
backward()	        amount	            Moves turtle backward by the specified amount
right()	            angle               Turns turtle clockwise
left()	            angle               Turns turtle counterclockwise
penup()	            None	            Picks up the turtles Pen
pendown()	        None	            Puts down the turtles Pen
up()	            None	            Picks up the turtles Pen
down()	            None	            Puts down the turtles Pen
color()	            Color name          Changes color of the turtles pen
fillcolor()	        Color name	        Changes color of the turtle will use to fill a polygon
heading()	        None	            Returns current heading
position()	        None	            Returns current position
goto()	            x, y                Move the turtle to position x,y
begin_fill()        None    	        Remember the starting point for a filled polygon
end_fill()	        None	            Close the polygon and fill with the current fill color
dot()	            None                Leave the dot at the current position
stamp()	            None	            Leaves impression of turtle shape at the current location
shape()	            shapename	        Should be arrow, classic, turtle or circle , square


shapesize()  
    stretch_wid: change size of turtle vertically (up and down).
    stretch_len: change size of  turtle horizontally (left and right).
    outline: change width size of outline of the turtle icon.

.dx , .dy                               Used to control the speed and direction of the ball's movement  in x and y direction
setx(<new_x_postion>) ,setx(<new_y_postion>) For setting new postion of  x and y coordinate 





.hideturtle() to your turtle name or to turtle directly and it will hide the turtle.
    turtle.hideturtle()
.showturtle()
showturtle() to bring it back. Otherwise it will remain visible.
    turtle.showturtle()




turtle.write(arg, move=False, align= 'left', font=('Arial', 8, 'normal')) 

arg	Info, which is to be written to the TurtleScreen
move	True/False
align	One of the strings “left”, “center” or right”
font	A tuple (fontname, fontsize, fonttype)

    If move set to False (the default), turtle will not move while writing. It will stay in its current position, and the text will be displayed at that location.

    If move set to True, turtle will move while writing. The distance the turtle moves is determined by the spacing between characters in the text
    
    .



"""

 
for i in range(4):
    skk.forward(50)
    skk.right(90)
     
turtle.done()


""" 
Turtle:
    drawing entity 
    It is a "pen" that moves around the screen and leaves a trail as it moves, creating drawings.
    attributes like position, heading (direction it's facing), and a pen (used for drawing).
    Methods associated with a turtle include forward(), backward(), right(), left(), etc., which control its movement and drawing actions.

Screen:
    graphical environment in which the turtle moves and draws.
    provides a canvas or drawing area where the turtle performs its actions.
    attributes like size, background color, title, etc., control appearance of drawing area.
    Methods associated with a screen include bgcolor(), title(), setup(), etc., which control the properties of drawing environment.


"""

