#in python you can track mouse movement by BIND method
import tkinter
window = tkinter.Tk()
def doSomething(event):
    print("you done something")
    print ()
    print ("Mouse coordinates: ")
    print(" X coordinates {}".format(event.x))
    print(" Y coordinates {}".format(event.y))


#window.bind("<Button-1>" , doSomething)
#window.bind("<Button-2>" , doSomething)
#window.bind("<Button-3>" , doSomething)
#window.bind("<ButtonRelease>" , doSomething) # when mouse released
#window.bind("<Enter>" , doSomething) # where you entered mouse normally boundary
#window.bind("<Leave>" , doSomething) # where you leaved mouse normally boundary
window.bind("<Motion>" , doSomething) # where you move throughout the window every point at stationary it stops

"""<Button> - The element was clicked
<Double-Button> - The element was double clicked
<Triple-Button> - The element was triple clicked
<ButtonPress> - A click on the element has begun
<ButtonRelease> - A click on the element was released"""




#only works in left click

#<Button-2> work on wheel not on right or left click
#<Button-3> work on on right click






window.mainloop()