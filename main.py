import sys
import math
import pygame
import traceback


#The function below will be graphed visually by this program
function = lambda x: (x**3)
#function = lambda x: (x*4/math.sqrt(x))
#function = lambda x: (math.log(x)/(2 * math.sqrt(x)))
#function = lambda x: ((x**3) + (2*x) -1)
#function = lambda x: (x + (math.sqrt(9 - x)))
#function = lambda x: ((4*(x**3)) + (24 * (x**2)))


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

#returns the derivative function
def derivative(f):
    """
    Computes the numerical derivative of a function.
    """
    def df(x, h=0.000000000001):  # h = 0.1e-5
        return ( f(x+h/2) - f(x-h/2) )/h
    return df

#derives the function at X and returns the approximate slope of the tanget line
def get_tangent_line_slope(function,x):
    first_derivative_function = derivative(function)

    slope = first_derivative_function(x)
    return slope


def get_second_derivative_value(function,x):
   first_derivative_function = lambda h: ((function(x + h) - function(x)) / h)
   second_derivative_function = lambda h: ((first_derivative_function(x + h) - first_derivative_function(x)) / h)
   second_derivative_value = second_derivative_function(0.000000000001)
   return second_derivative_value



# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


pygame.init()
size = width, height = 1000, 800

center = width / 2, height / 2

speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()



x_scale = 100
y_scale = 100

while 1:
    #clear screen
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.dict['button'] == 4:
                #print "scroll up"
                x_scale += 10
                y_scale += 10
                #print x_scale, y_scale
            elif event.dict['button'] == 5:
                #print "scroll down"
                x_scale -= 10
                y_scale -= 10
                #print x_scale, y_scale

    #Draw X Axis
    pygame.draw.line(screen, WHITE, [0,center[1]], [width,center[1]], 1)

    #Draw Y Axis
    pygame.draw.line(screen, WHITE, [center[0],0], [center[0],height], 1)

    #Draw tangent lines from points of the function at intervals of 0.1 between -10 and 10
    for x_val in drange(-10,10,.1):
        try:
            y_val = function(x_val)

            derivative_function = derivative(function)
            tangent_slope = derivative_function(x_val)

            if round(tangent_slope,4) == 0.0000:
                print "critical point at " + str(x_val)
                print "y val: " + str(y_val)

            #Calculate second derivative to find inflection points
            first_derivative_function = derivative(function)
            second_derivative_function = derivative(first_derivative_function)  # == derivative(derivative(g))
            # second derivative
            second_derivative_value = second_derivative_function(x_val)
            print 'second derivative'
            print second_derivative_value

            if second_derivative_value == 0.0:
                print second_derivative_value, x_val

            #Point slope form
            #y - y1 = m(x - x1)
            #y = (m*x) - (m*x1) + y1
            line_function = lambda x: ((tangent_slope * x) - (tangent_slope * x_val) + y_val)

            #Get a point a little to the left
            line_start_x = x_val - 10
            line_start_y = line_function(line_start_x)

            #Get a point a little to the right
            line_end_x = x_val + 10
            line_end_y = line_function(line_end_x)

            #Scale the points
            line_start_x *= x_scale
            line_start_y *= y_scale * -1

            line_end_x *= x_scale
            line_end_y *= y_scale * -1

            #Draw the tangent line
            pygame.draw.line(screen,BLUE,[int(line_start_x + center[0]),int(line_start_y + center[1])],[int(line_end_x + center[0]),int(line_end_y + center[1])],1)

            #scale point
            x_val *= x_scale
            y_val *= y_scale

            #flip y_val so graph displays properly
            y_val *= -1

            #draw this point on graph
            pygame.draw.circle(screen,GREEN,[int(x_val + center[0]),int(y_val + center[1])],1)
        except:
            #print traceback.print_exc()
            pass

    pygame.display.flip()







