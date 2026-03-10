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
        """
        self.pi = 3.141592653 #the HP manual states that the pi button places the first 10 digits of pi into the calculator.
        
    def integer(self):
        calc.stack.x = int(calc.stack.x)
        
    def frac(self):
        calc.stack.x = calc.stack.x - int(calc.stack.x)
        
    def round_hp(self): #cant name this function round since python already comes with its own round.
        calc.stack.x = round(calc.stack.x, calc.display_digits)
    
    def absolute_value(self): #cant name this abs since python already has a function named abs
        calc.stack.x = abs(calc.stack.x)
    
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
calc.stack.add_element_to_stack(3)
calc.stack.add_element_to_stack(5)
calc.stack.show_stack_for_debug()
calc.math.addition()
calc.stack.show_stack_for_debug()