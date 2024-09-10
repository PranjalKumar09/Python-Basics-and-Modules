""" 
 pygame.init()
    initialize all imported pygame modules
    init() -> (numpass, numfail)

    Initialize all imported pygame modules. No exceptions will be raised if a module fails, but the total number if successful and failed inits will be returned as a tuple
    
 pygame.display.set_mode((size))
    Initialize a window or screen for display
    set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
 pygame.event.get()
    get events from the queue
    get(eventtype=None) -> Eventlist
    get(eventtype=None, pump=True) -> Eventlist
    get(eventtype=None, pump=True, exclude=None) -> Eventlist

pygame.event.get() => [x1 , x2, x3 , x4, x5, x6, x7 ...]
it return list of x where x.type can be , KEYDOWN ,	KEYUP, MOUSEBUTTONUP ,MOUSEBUTTONDOWN , MOUSEMOTION, QUIT

KEYDOWN event is occurred 

where in x.pos in case of mouse button is (x,y)
x.key can be K_RIGHT  , K_LEFT , K_UP , K_DOWN 
(arrow keys)



pygame.draw.rect
	    rectangle
pygame.draw.polygon
	    polygon
pygame.draw.circle
	    circle
pygame.draw.ellipse
	    ellipse
pygame.draw.arc
	    elliptical arc
pygame.draw.line
	    straight line
pygame.draw.lines
    multiple contiguous straight line segments
pygame.draw.aaline
	    straight antialiased line
pygame.draw.aalines
	draw multiple contiguous straight antialiased line segments



 pygame.draw.rect()
    draw a rectangle
    rect(surface, color, rect) -> Rect
    rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1

Parameters
        surface (Surface) -- surface to draw on
        color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
        rect (Rect) -- rectangle to draw, position and dimensions
        width (int) --
        (optional) 
            if width == 0, (default) fill the rectangle
            if width > 0, used for line thickness
            if width < 0, nothing will be drawn

        border_radius (int) -- (optional) used for drawing rectangle with rounded corners. The supported range is [0, min(height, width) / 2], with 0 representing a rectangle without rounded corners.
        border_top_left_radius (int) -- (optional)
        border_top_right_radius (int) -- (optional)
        border_bottom_left_radius (int) -- (optional) 
        border_bottom_right_radius (int) -- (optional) 
            if border_radius < 1 it will draw rectangle without rounded corners
            if any of border radii has the value < 0 it will use value of the border_radius
            If sum of radii on the same side of the rectangle is greater than the rect size the radii
            will get scaled

Returns
    a rect bounding the changed pixels, if nothing is drawn the bounding rect's position will be the position of the given rect parameter and its width and height will be 0
Return type

    
    
    
     pygame.draw.circle()
    draw a circle
    circle(surface, color, center, radius, width=0, draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None) -> Rect

    Parameters
            surface (Surface) -- surface to draw on
            center (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- center point of the circle as a sequence of 2 ints/floats, e.g. (x, y)
            radius (int or float) -- radius of the circle, measured from the center parameter, nothing will be drawn if the radius is less than 1


 pygame.time.wait()
    pause the program for an amount of time
    
    
    
 pygame.font.SysFont()
    create a Font object from the system fonts
    SysFont(name, size, bold=False, italic=False) -
    

myfont.render(<text>, 1, <color>)


The `1` indicates that antialiasing is enabled for the rendered text (smooth graphics)
screen.blit is a method used to draw one surface onto another
screen.blit(source, dest)

screen.fill(color) => fills the color 





 pygame.draw.line()
    Draws a straight line on the given surface. There are no endcaps. For thick lines the ends are squared off.

    Parameters

            surface (Surface) -- surface to draw on

            color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])

            start_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- start position of the line, (x, y)

            end_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- end position of the line, (x, y)

            width (int) --

            (optional) used for line thickness
            if width >= 1, used for line thickness (default is 1)
            if width < 1, nothing will be drawn





"""


""" 
    pygame.time.wait ( <n> )
    pygame.time.get_ticks ()
    pygame.time.delay (<n>)  => use processor instead of sleeping for accurate (simlar to wait)
    pygame.time.Clock
    
    Clock = pygame.time.Clock

     
    Clock.tick(<n>):alled once per frame. It will compute how many milliseconds have passed since the previous call. if we pass 10 as argument the program will never run at more than 10 frames per second.

    Clock.get_time():It is used to obtain a number of milliseconds used between two tick().

    Clock.get_fps():it gives information regarding the clock frame rate. it returns the output in floating-point value.

    
    all take in input in milliseconds (1000 = 1 second)
    return also in millisecond
    
    
    
    
     get_rawtime()
    actual time used in the previous tick
    get_rawtime() -> milliseconds

    Similar to Clock.get_time(), but does not include any time used while Clock.tick() was delaying to limit the framerate.




pygame.display.set_caption("Window new title")


"""