#Python15C by averybaddev on github

import math
import random

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
        self.stack_lift()
        self.x = element
    
    def get_a_value(self):
        """
        Pushes the stack up then sets x to the input.
        This may be removed later.
        Used for functions that wait on user input before finishing execution.
        """
        #self.stack_lift()
        self.value = float(input())
        return self.value
    
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
        """
        Performs a stack drop.
        All values are dropped down, with t "duplicating".
        Example:
        x = 3
        y = 4
        z = 5
        t = 6
        stack_drop()
        x = 4
        y = 5
        z = 6
        t = 6
        """
        self.x = self.y
        self.y = self.z
        self.z = self.t
        
    def xy_swap(self):
        """
        Swaps the values of x and y.
        """
        self.x, self.y = self.y, self.x
    
    def roll_down(self):
        """
        Rolls down the stack.
        Example:
        x = 1
        y = 2
        z = 3
        t = 4
        roll_down()
        x = 2
        y = 3
        z = 4
        t = 1
        """
        self.x, self.y, self.z, self.t = self.y, self.z, self.t, self.x
        
    def roll_up(self):
        """
        Rolls down the stack.
        Example:
        x = 1
        y = 2
        z = 3
        t = 4
        roll_down()
        x = 4
        y = 1
        z = 2
        t = 3
        """
        self.x, self.y, self.z, self.t = self.t, self.x, self.y, self.z
        
    def last_x_implementation(self): #call this in later things such as additions and other operations
        """
        Stores x into last_x.
        Used when wanting to recall the previous value of x for certain calculations.
        No example.
        """
        self.last_x = self.x
        
    def enter(self):
        """
        Replicating the behavior of the enter key.
        Lifts the stack and duplicates x.
        Example:
        x = 1
        y = 0
        enter()
        x = 1
        y = 1
        """
        self.stack_lift()
        self.y = self.x
    
    def clear_x(self):
        """
        Sets x to 0.
        Used for the backspace key when a number has already been entered to the stack.
        """
        self.x = 0
        
    def replace_x(self,value):
        """
        Changes the value of x.
        Used when typing a number in while a number is already stored into x.
        """
        self.x = value
        
    def clear_stack(self):
        """
        Clears the entire stack.
        Will be used in later functions to help with resetting the calculator.
        """
        self.x,self.y,self.z,self.t = 0, 0, 0, 0
        
    def get_stack(self):
        """
        Gets every value in the stack.
        Might be used later when implementing a user interface to display the stack in real time.
        """
        return [self.t,self.z,self.y,self.x]
        
    def show_stack_for_debug(self):
        """
        As the name implies, shows the stack for debugging.
        This function is only really useful for me as the developer of this program.
        However, when it comes to being useful, it's a life saver.
        """
        print(self.t,self.z,self.y,self.x)
        print("t z y x")       

class MathOps:
    def __init__(self):
        """
        MathOps implements all operations in the numeric functions section of the manual.
        It initializes some constants such as pi.
        All functions implemented are implemented in the order they are mentioned in the manual.
        The comments such as NUMBER ALTERATION FUNCTIONS are titles directly from the manual.
        """
        self.pi = 3.141592653 #the HP manual states that the pi button places the first 10 digits of pi into the calculator.
        self.seed = 0 #needed for the display_seed function
        random.seed(self.seed) #the HP15C initializes its seed to 0 at startup.
    
    
    # NUMBER ALTERATION FUNCTIONS
    def integer(self):
        """
        Keeps only the integer part of x.
        """
        calc.stack.x = int(calc.stack.x)
        
    def frac(self):
        """
        Keeps only the fractional part of x.
        """
        calc.stack.x = calc.stack.x - int(calc.stack.x)
        
    def round_hp(self): #cant name this function round since python already comes with its own round.
        """
        Rounds down numbers to the number of digits specified in display_digits.
        Might need a rework. Unsure.
        """
        calc.stack.x = round(calc.stack.x, calc.display_digits)
    
    def absolute_value(self): #cant name this abs since python already has a function named abs
        """
        As the name implies, just gives the absolute value of x.
        """
        calc.stack.x = abs(calc.stack.x)
    
    
    # ONE NUMBER FUNCTIONS
    def reciprocal(self):
        """
        Calculates the reciprocal of x.
        """
        calc.stack.x = 1/calc.stack.x
        
    def factorial(self):
        """
        Calculates the factorial of x.
        In line with real behavior, the calculator does not calculate for negatives.
        For those wondering, surprisingly, the 15C could calculate factorials for rational numbers.
        """
        calc.stack.x = math.factorial(calc.stack.x)
        
    def gamma(self): #according to HP, this function calculates gamma(x+1), not gamma(x)
        """
        Calculates the gamma function of x+1 (not x).
        """
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
        """
        Calculates the sine of x, with the result adapting depending on the trig mode
        """
        if calc.trig_mode==0: #degrees mode
            calc.stack.x = math.sin(math.radians(calc.stack.x)) #converts the degrees to radians for the calculation
        elif calc.trig_mode==1: #radians mode
            calc.stack.x = math.sin(calc.stack.x)
        else: #gradians mode
            calc.stack.x = math.sin(calc.stack.x*self.pi/200) #the gradian to radian conversion (value*pi/200) was graciously provided by google
        
    def arcsine(self):
        """
        Calculates the arc sine of x, with the result adapting depending on the trig mode
        """
        if calc.trig_mode==0:
            calc.stack.x = math.asin(math.radians(calc.stack.x))
        if calc.trig_mode==1:
            calc.stack.x = math.asin(calc.stack.x)
        if calc.trig_mode==2:
            calc.stack.x = math.asin(calc.stack.x*self.pi/200)
    
    def cosine(self):
        """
        Calculates the cosine of x, with the result adapting depending on the trig mode
        """
        if calc.trig_mode==0:
            calc.stack.x = math.cos(math.radians(calc.stack.x))
        if calc.trig_mode==1:
            calc.stack.x = math.cos(calc.stack.x)
        if calc.trig_mode==2:
            calc.stack.x = math.cos(calc.stack.x*self.pi/200)
        
    def arccosine(self):
        """
        Calculates the arc cosine of x, with the result adapting depending on the trig mode
        """
        if calc.trig_mode==0:
            calc.stack.x = math.acos(math.radians(calc.stack.x))
        if calc.trig_mode==1:
            calc.stack.x = math.acos(calc.stack.x)
        if calc.trig_mode==2:
            calc.stack.x = math.acos(calc.stack.x*self.pi/200)
            
    def tangent(self):
        """
        Calculates the tangent of x, with the result adapting depending on the trig mode
        """
        if calc.trig_mode==0:
            calc.stack.x = math.tan(math.radians(calc.stack.x))
        if calc.trig_mode==1:
            calc.stack.x = math.tan(calc.stack.x)
        if calc.trig_mode==2:
            calc.stack.x = math.tan(calc.stack.x*self.pi/200)
        
    def arctangent(self):
        """
        Calculates the arc tangent of x, with the result adapting depending on the trig mode
        """
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
        Examples:
        INSERT EXAMPLE HERE LATER
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
        
    
    def to_h(self): #COMPLETELY UNFINISHED, PLACEHOLDER CODE. 
        """
        Converts the h.mmssxxxxx format to H.h (or decimal hours)
        Examples:
        x = 5.45
        to_h()
        x = 5.75
        ----
        x = 5.4515
        to_h()
        x = 5.7542
        """
        hours = int(calc.stack.x)
        the_rest = round(calc.stack.x - hours,10)
        if the_rest == 0:
            pass #if there are just hours in x, we don't have to convert hours to hours... so we dont.
        else:
            the_rest = str(the_rest)
            if len(the_rest)==3 or len(the_rest)==4: #checks if there are only minutes and not seconds/subseconds. The reason I check for 3 and 4, is because if calc.stack.x = 5.45,
                                                     #then the_rest = 0.45, which then gets converted to a string. The string would be the following: "0.45", which is 4 characters long because of the 0 and period.
                if len(the_rest)==4: #IMPLEMENT SOME LOGIC IF the_rest > 0.59, SO THAT IT GETS CONVERTED AS AN HOUR AND SOME EXTRA
                    minutes = round(float(the_rest)/60,10)*100
                else:
                    minutes = round(10*float(the_rest)/60,10)*100 #implement later
        calc.stack.x = hours + minutes #temporary placement and values.
        
    
    #LOGARITHMIC FUNCTIONS
    def natural_log(self):
        """
        Calculates the natural logarithm of x.
        """
        calc.stack.x = math.log(calc.stack.x) #while this looks like a regular log, this is indeed a natural log.
        #math.log() has a default base parameter, which is math.e (so euler's number), which makes it a natural logarithm.
    
    def natural_antilog(self):
        """
        Calculates the natural antilogarithm of x.
        """
        calc.stack.x = math.exp(calc.stack.x)
    
    def common_log(self):
        """
        Calculates the common logarithm of x.
        """
        calc.stack.x = math.log(calc.stack.x,10)
    
    def common_antilog(self):
        """
        Calculates the common antilogarithm of x.
        """
        calc.stack.x = 10**calc.stack.x
        
    #HYPERBOLIC FUNCTIONS
    def hyperbolic_sine(self):
        """
        Calculates the hyperbolic sine of x
        """
        calc.stack.x = math.sinh(calc.stack.x)
       
    def hyperbolic_arcsine(self):
        """
        Calculates the hyperbolic arc sine of x
        """
        calc.stack.x = math.asinh(calc.stack.x)
    
    def hyperbolic_cosine(self):
        """
        Calculates the hyperbolic cosine of x
        """
        calc.stack.x = math.cosh(calc.stack.x)
        
    def hyperbolic_arccosine(self):
        """
        Calculates the hyperbolic arc cosine of x
        """
        calc.stack.x = math.acosh(calc.stack.x)
            
    def hyperbolic_tangent(self):
        """
        Calculates the hyperbolic tangent of x
        """
        calc.stack.x = math.tanh(calc.stack.x)
        
    def hyperbolic_arctangent(self):
        """
        Calculates the hyperbolic arc tangent of x
        """
        calc.stack.x = math.atanh(calc.stack.x)
                
    #TWO NUMBER FUNCTIONS
    def addition(self):
        """
        Calculates x+y.
        """
        calc.stack.y = calc.stack.x + calc.stack.y
        calc.stack.stack_drop()
        
    def substraction(self):
        """
        Calculates y - x
        """
        calc.stack.y=calc.stack.y-calc.stack.x
        calc.stack.stack_drop()

    def multiplication(self):
        """
        Calculates x*y
        """
        calc.stack.y=calc.stack.x*calc.stack.y
        calc.stack.stack_drop()
        
    def division(self):
        """
        Calculates y/x.
        Has a safety check for division by 0.
        If x=0, it will set error_status to 0 (the value used for the division by 0 error in the HP15C)
        """
        if calc.stack.x==0:
            calc.error_status = 0 #official HP15C error code for division by 0
        else:
            calc.stack.y = calc.stack.y/calc.stack.x
            calc.stack.stack_drop()
    
    def power(self):
        """
        Calculates y to the power of x.
        """
        calc.stack.y = calc.stack.y**calc.stack.x
        calc.stack.stack_drop()
        
    def percent(self):
        """
        Calculates the specified percentage of a base number
        """
        calc.stack.x = calc.stack.x*0.01*calc.stack.y
        
    def percent_difference(self): 
        """
        Calculates the percent difference between two numbers.
        The manual calls this function "percent difference", however whilst trying to code this function,
        I found online that the correct formula (that gives the same results as the HP15C),
        is actually the formula for percent CHANGE. Not difference.
        Example from the HP manual:
        y = 15.76
        x = 14.12
        percent_difference()
        y = 15.65
        x = -10.4061
        (x is 10.4061 percent lower)
        """
        calc.stack.x = (calc.stack.x-calc.stack.y)/abs(calc.stack.y)*100
    
    #POLAR AND RECTANGULAR COORDINATE CONVERSIONS
    #all formulas used here were looked up on google. I do NOT know how to do these conversions without looking the formulas up.
    
    def polar_conversion(self):
        """
        Converts rectangular coordinates to polar coordinates.
        According to the manual the function works like this:
        y -> theta
        x -> r
        """
        r = math.sqrt(calc.stack.x**2+calc.stack.y**2)
        if calc.trig_mode==0: #unfortunately for me, this conversion gives different results depending on the trig mode... 
            theta = math.degrees(math.atan(calc.stack.y/calc.stack.x))
        elif calc.trig_mode==1:
            theta = math.atan(calc.stack.y/calc.stack.x)
        else:
            theta = math.atan((calc.stack.y/calc.stack.x)*self.pi/200)
        calc.stack.x,calc.stack.y = r,theta
    
    def rectangular_conversion(self):
        """
        Converts polar coordinates to rectangular coordinates.
        According to the manual, the function works like this:
        theta -> y
        r -> x
        """
        r,theta = calc.stack.x,calc.stack.y
        if calc.trig_mode==0:
            calc.stack.x = round(r*math.cos(math.radians(theta)),10)
            calc.stack.y = round(r*math.sin(math.radians(theta)),10)
        elif calc.trig_mode==1:
            calc.stack.x = round(r*math.cos(theta),10)
            calc.stack.y = round(r*math.sin(theta),10)
        else:
            calc.stack.x = round(r*math.cos(theta*self.pi/200),10)
            calc.stack.y = round(r*math.sin(theta*self.pi/200),10)
            
    #PROBABILITY CALCULATIONS
    def permutations(self):
        """
        Calculates the number of permutations of x in y.
        """
        calc.stack.y = math.perm(calc.stack.y,calc.stack.x)
        calc.stack.stack_drop()
        
    def combinations(self):
        """
        Calculates the number of combinations of x in y.
        """
        calc.stack.y = math.comb(calc.stack.y,calc.stack.x)
        calc.stack.stack_drop()
        
    #RANDOM NUMBER GENERATOR
    def random_number(self):
        """
        Generates a random number between 0 and 1 (1 excluded)
        This does not generate the same numbers as the HP15C, even with the same seed.
        This is likely due to differences in the random algorithms used.
        """
        calc.stack.x = random.random()
        
    def set_seed(self):
        """
        Sets the seed for random number generation.
        """
        calc.math.seed = calc.stack.x
        random.seed(calc.math.seed)
        
    def display_seed(self):
        """
        Displays the seed by putting it in x.
        """
        calc.stack.x = self.seed
            
class DataManipulation:
    def __init__(self):
        """
        This class will handle things such as storing and recalling data from the registers.
        """
        pass
    
    def store(self):
        """
        Stores x to one of the storage registers, chosen by inputting a number between 0 and 9 (for now)
        """
        to_store = calc.stack.x
        register = int(calc.stack.get_a_value())
        if register >= 0 and register <= 9:
            calc.registers[register]=to_store
        
    def recall(self):
        """
        Recalls the value inside one of the storage registers to x.
        Currently incomplete (no protection from index errors if the chosen register number exceeds 9 or -10)
        """
        register = int(calc.stack.get_a_value()) #implement a check where register >= 0 and register <= 9
        calc.stack.x = calc.registers[register] #the only thing stopping me from implementing this right now is that
        #calc.stack.get_a_value() lets numbers above 9 go in, meanwhile on the HP15C, it's not possible,
        #so i have to figure this out first before being truly able to implement this logic.
        #it may only be possible to implement it once I've also implemented some of the UI logic.
        
    def x_exchange(self):
        """
        Exchanges the value of x with a chosen register.
        Currently incomplete (no protection from index errors if the chosen register number exceeds 9 or -10)
        """
        register = int(calc.stack.get_a_value()) #same thing as recall()
        calc.stack.x,calc.registers[register] = calc.registers[register], calc.stack.x
        
    def clear_regs(self):
        """
        Resets all registers to their default value of 0.
        Will be used for the clear regs button, as well as a hard calculator reset.
        """
        self.registers = [0,0,0,0,0,0,0,0,0,0]
        
        
class HP15C:
    def __init__(self):
        """
        Initializes all the classes for use in the program.
        Also initializes some flags and variables, as well as the registers.
        """
        self.stack = Stack()
        self.math = MathOps()
        self.data = DataManipulation()
        #flags and variables
        self.error_status = None #set to None, if it's anything other than None, it will be detected in the display program, and display ERROR and the error number.
        self.display_digits = 5 #the hp15c has 5 digits displayed by default. cannot go to 0. #might need to be changed to digits after the period... come back later
        self.complex_numbers = False #if False, disable functionality entirely. same as flag 9 in the hp15c
        self.display_mode = 0 #0 for fixed (standard hp15c mode), 1 for scientific, 2 for engineering.
        self.trig_mode = 0 #0 for degrees (decimal, not minutes seconds), 1 for radians, 2 for gradians.
        #memory registers
        #self.r0,self.r1,self.r2,self.r3,self.r4,self.r5,self.s6,self.s7,self.s8,self.s9 = [0,0,0,0,0,0,0,0,0,0]
        self.registers = [0,0,0,0,0,0,0,0,0,0]
        self.index_register = 0
        self.expanded_registers = []

        
    def change_display_digits(self,number):
        """
        Allows the user to change how many digits are displayed in the UI's display.
        However there is currently no display or UI.
        """
        if number != 0 and number <= 9: #the HP15C display can show up to 9 digits after the period. #might need to be changed unsure
            self.display_digits = number

#"automated" stack testing area
calc = HP15C()
calc.math.random_number()
calc.stack.show_stack_for_debug()
calc.math.display_seed()
calc.stack.show_stack_for_debug()

#implement remaining math functionality
#currently missing:
#statistics, to_h() needs completion, gamma function

#implement memory
#currently missing:
#unfinished last x implementation, unfinished register implementation (register expansion), register arithmetics

#implement programmability
#currently missing:
#everything in relation to calculator programmability... damn.


#after finalization of the calculator:
#implement file based memory for stuff like variables and programmability.