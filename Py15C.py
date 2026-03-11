#Python15C by averybaddev on github

import math
import random
#flags


#global vars
last_x = None


class Stack:
    def __init__(self):
        """
        Stack is a class that implements all stack manipulation functionality required by an HP15C.
        Initializes the stack and last_x
        """
        self.x,self.y,self.z,self.t = 0, 0, 0, 0
        self.last_x = 0
        self.stack_lift_on = True
        
            
    def add_element_to_stack(self,element): # the below code might be unnecessary due to x_replace. make sure to check
        """
        Pushes the stack up then sets x to the element
        """
        assert type(element)==float or type(element)==int
        self.stack_lift()
        self.x = element

        
    def stack_lift(self):
        """
        Lifts the stack after an operation as with default HP15C behavior.
        All elements go up in the stack, with the last element being lost.
        new_value allows functions that call stack_lift() to enter the result of the operation into the stack.
        """
        self.t = self.z
        self.z = self.y
        self.y = self.x
        self.x = 0
        
    def stack_drop(self):
        self.x = self.y
        self.y = self.z
        self.z = self.t
        
    def xy_swap(self):
        self.x, self.y = self.y, self.x
    
    def roll_down(self):
        self.x, self.y, self.z, self.t = self.y, self.z, self.t, self.x
        
    def roll_up(self):
        self.x, self.y, self.z, self.t = self.t, self.x, self.y, self.z
        
    def last_x_implementation(self): #call this in later things such as additions and other operations
        self.last_x = self.x
        
    def enter(self):
        self.stack_lift()
        self.y = self.x
    
    def clear_x(self):
        self.x = 0
        
    def replace_x(self,value):
        self.x = value
        
    def clear_stack(self):
        self.x,self.y,self.z,self.t = 0, 0, 0, 0
        
    def get_stack(self):
        return [self.t,self.z,self.y,self.x]
        
    def show_stack_for_debug(self):
        print(self.t,self.z,self.y,self.x)
        print("t z y x")       

class MathOps:
    def __init__(self):
        """
        MathOps implements all math operations in the HP15C.
        It initializes some constants such as pi.
        All functions implemented are implemented in the order they are mentioned in the manual.
        The comments such as NUMBER ALTERATION FUNCTIONS are titles directly from the manual.
        """
        self.pi = 3.141592653 #the HP manual states that the pi button places the first 10 digits of pi into the calculator.
    
    
    # NUMBER ALTERATION FUNCTIONS
    def integer(self):
        calc.stack.x = int(calc.stack.x)
        
    def frac(self):
        calc.stack.x = calc.stack.x - int(calc.stack.x)
        
    def round_hp(self): #cant name this function round since python already comes with its own round.
        calc.stack.x = round(calc.stack.x, calc.display_digits)
    
    def absolute_value(self): #cant name this abs since python already has a function named abs
        calc.stack.x = abs(calc.stack.x)
    
    
    # ONE NUMBER FUNCTIONS
    def reciprocal(self):
        calc.stack.x = 1/calc.stack.x
        
    def factorial(self):
        """
        Calculates the factorial of x.
        In line with real behavior, the calculator does not calculate for negatives.
        For those wondering, surprisingly, the 15C could calculate factorials for rational numbers.
        """
        calc.stack.x = math.factorial(calc.stack.x)
        
    def gamma(self): #according to HP, this function calculates gamma(x+1), not gamma(x)
        pass #i do not know how to implement this, come back later
        
    def square_root(self):
        """
        Calculates the square root of x.
        With the complex number flag not set, the HP15C returns error 0, which is replicated here.
        """
        if calc.stack.x < 0:
            calc.error_status = 0
        else:
            calc.stack.x = math.sqrt(calc.stack.x)
            
    def squaring(self):
        """
        Calculates the square of x.
        """
        calc.stack.x = calc.stack.x ** calc.stack.x
        
        
    # TRIGONOMETRY
    def sine(self):
        if calc.trig_mode==0: #degrees mode
            calc.stack.x = math.sin(math.radians(calc.stack.x)) #converts the degrees to radians for the calculation
        elif calc.trig_mode==1: #radians mode
            calc.stack.x = math.sin(calc.stack.x)
        else: #gradians mode
            calc.stack.x = math.sin(calc.stack.x*self.pi/200) #the gradian to radian conversion (value*pi/200) was graciously provided by google
        
    def arcsine(self):
        if calc.trig_mode==0:
            calc.stack.x = math.asin(math.radians(calc.stack.x))
        if calc.trig_mode==1:
            calc.stack.x = math.asin(calc.stack.x)
        if calc.trig_mode==2:
            calc.stack.x = math.asin(calc.stack.x*self.pi/200)
    
    def cosine(self):
        if calc.trig_mode==0:
            calc.stack.x = math.cos(math.radians(calc.stack.x))
        if calc.trig_mode==1:
            calc.stack.x = math.cos(calc.stack.x)
        if calc.trig_mode==2:
            calc.stack.x = math.cos(calc.stack.x*self.pi/200)
        
    def arccosine(self):
        if calc.trig_mode==0:
            calc.stack.x = math.acos(math.radians(calc.stack.x))
        if calc.trig_mode==1:
            calc.stack.x = math.acos(calc.stack.x)
        if calc.trig_mode==2:
            calc.stack.x = math.acos(calc.stack.x*self.pi/200)
            
    def tangent(self):
        if calc.trig_mode==0:
            calc.stack.x = math.tan(math.radians(calc.stack.x))
        if calc.trig_mode==1:
            calc.stack.x = math.tan(calc.stack.x)
        if calc.trig_mode==2:
            calc.stack.x = math.tan(calc.stack.x*self.pi/200)
        
    def arctangent(self):
        if calc.trig_mode==0:
            calc.stack.x = math.atan(math.radians(calc.stack.x))
        if calc.trig_mode==1:
            calc.stack.x = math.atan(calc.stack.x)
        if calc.trig_mode==2:
            calc.stack.x = math.atan(calc.stack.x*self.pi/200)
        
    # TIME AND ANGLE CONVERSIONS
    def to_hms(self): #real struggle to get working, floating points are so finnicky, which is the reason why there are so many rounds.
        """
        Converts a decimal hour value into Hours Minutes and Seconds.
        The following format is used: h.mmssxxxxx
        x is for the sub second values.
        Since this function was a mess to write, I will explain the entirety of it with comments.
        """
        hours = int(calc.stack.x) #if the value is 1.5 decimal hours, it will grab just the 1.
        the_rest = round(calc.stack.x - hours,10) #in this case, if the value is 1.5, it will do 1.5 - the number of hours, which we saw previously is 1, so 1.5-1 = 0.5. The round is there just because of python floating point nonsense.
        if the_rest == 0: #if there are no decimals, and just the hour, it will set everything to 0. example: 3 decimal hours = 3.000000000 after the function runs. 
            minutes, seconds, below_seconds = 0, 0, 0 #setting the variables to 0 (if they arent set, there will be an error when running the final line)
        else: #however, if there are decimals in the number, so for example 1.5, it will proceed with the next steps of the conversion.
            minutes  = round(the_rest*60,10) #it sets the number of minutes by taking the rest, and multiplying it by 60.
            if round(minutes-int(minutes),10)!=0: #but its possible for the value to minutes to have a decimal. that means we have to continue further with the conversion
                seconds = round((minutes - int(minutes))*60,10) #it sets the number of seconds by taking the fractional part of minutes, and multiplying it by 60
                minutes = int(minutes) # this removes the fractional part of minutes since that fractional part has now been turned into seconds.
                if round(seconds-int(seconds),10)!=0: #if the seconds have a fractional part, it will proceed for the conversion to subseconds
                    below_seconds = round(seconds-int(seconds),10) #this will go down to the hundred thousandth of a second, as it is stated to be the maximum accuracy of this conversion in the HP15C manual.
                else: #if there is no fractional part to seconds, it will simply set below_seconds to 0
                    below_seconds = 0 #this is set to 0 to prevent errors with the last line.
            else: #if the minutes dont have a fractional part, it will set seconds and below_seconds to 0
                seconds, below_seconds = 0,0 #these are set to 0 to prevent errors with the last line
        calc.stack.x = round(hours + minutes * 0.01 + seconds * 0.0001 + below_seconds * 0.000000001,9) #sets the value of x to the h.mmssxxxxx format.
        
    
    def to_hh(self): #conversion to decimal hours
        pass
    
    def addition(self):
        """
        This function adds x and y together, with the output ending up in x.
        Firstly it stores the output into y, as if it is put into x,
        it has incorrect behavior (compared to the real calculator),
        and leaves the original value of y
        """
        calc.stack.y = calc.stack.x + calc.stack.y
        calc.stack.stack_drop()
        
    def substraction(self):
        calc.stack.y=calc.stack.x-calc.stack.y
        calc.stack.stack_drop()

    def multiplication(self):
        calc.stack.y=calc.stack.x*calc.stack.y
        calc.stack.stack_drop()
        
    def division(self):
        if calc.stack.x==0:
            calc.error_status = 0 #official HP15C error code for division by 0
        else:
            calc.stack.y = calc.stack.y/calc.stack.x
            calc.stack.stack_drop()
            
class HP15C:
    def __init__(self):
        self.stack = Stack()
        self.math = MathOps()
        #flags and variables
        self.error_status = None #set to None, if it's anything other than None, it will be detected in the display program, and display ERROR and the error number.
        self.display_digits = 5 #the hp15c has 5 digits displayed by default. cannot go to 0. #might need to be changed to digits after the period... come back later
        self.complex_numbers = False #if False, disable functionality entirely. same as flag 9 in the hp15c
        self.display_mode = 0 #0 for fixed (standard hp15c mode), 1 for scientific, 2 for engineering.
        self.trig_mode = 0 #0 for degrees (decimal, not minutes seconds), 1 for radians, 2 for gradians.

        
    def change_display_digits(self,number):
        if number != 0 and number <= 9: #the HP15C display can show up to 9 digits after the period. #might need to be changed unsure
            self.display_digits = number

#implement remaining math functionality
#implement memory
#implement programmability 


#after finalization of the calculator:
#implement file based memory for stuff like variables and programmability.

#"automated" stack testing area
calc = HP15C()
calc.stack.add_element_to_stack(1.0166666666667)
calc.math.to_hms()
calc.stack.show_stack_for_debug()