from math import sin, cos, tan, pi, degrees, radians

# print(round(sin(radians(90)), 0))
print('Welcome to this projectile motion simulator!')
print('Enter your starting velocity')
Vinitial = input()
print('Enter launch angle from the horizontal')
thetainput = float(input())

#variables

theta = radians(thetainput)
gy = -9.8
time = 0
Vinitialx = 0
Vinitialy = 0
Vfinalx = 0
Vfinaly = 0
AccelX = 0
AccelY = 0
Dinitialx = 0
Dinitialy = 0
Dfinalx = 0
Dfinaly = 0
rad_degree_conversion = 360/(2*pi)
#functions
def sinfunction(angle):
    global sindeg
#this function returns the sin of an angle in degrees
    sindeg = round(sin(angle), 3)
    # print(sindeg)

def cosfunction(angle):
    global cosdeg
#returns cosin of an angle in degrees
    cosdeg = round(cos(angle), 3)
    # print(cosdeg)

def velocity_x_component(Vi, costheta):
    global Vinitialx
#this function computes x component of initial velocity from angle and v initial
    Vinitialx = round(float(Vi)*costheta, 2)
    print('Velocity in x direction: '+ str(Vinitialx)+ ' meters per second')

def velocity_y_component(Vi, sintheta):
    global Vinitialy
# this function computes y component of initial velocity from angle and v initial
    Vinitialy = round(float(Vi)*sintheta, 2)
    print('Velocity in Y direction: '+ str(Vinitialy)+ ' meters per second')

def compute_time(Viy):
    global time
#computes time from y component of velocity and gravity
    global gy
    time = round(-Viy*2/gy, 2)
    print('time: '+ str(time)+ ' seconds')

def max_height(Viy, time, gy):
    global height
    #finds maximum height
    height_equation_1 = Viy**2
    height_equation_2 = 2*gy*-1
    height_calc = height_equation_1/height_equation_2
    height = round(height_calc, 2)
    print('maximum height: '+ str(height)+ ' meters')

def compute_distance(Vix, time):
    global distance
    #computes distance from velocity and time
    dist_equation1 = Vix*time
    calc_dist = dist_equation1
    distance = round(calc_dist, 2)
    print('horizontal distance: '+ str(distance)+ ' meters')

def instant_velocity_y():
    instant_Vy = Vinitialy**2 + 2*gy

sinfunction(theta)
cosfunction(theta)
velocity_x_component(Vinitial, cosdeg)
velocity_y_component(Vinitial, sindeg)
compute_time(Vinitialy)
max_height(Vinitialy, time, gy)
compute_distance(Vinitialx, time)

def time_function(time_length):
    time_variable = []
    for i in time_length:
        time_variable.append(i)
    print(time_variable)

print(range(len(str(time))))