# Python15C
A recreation of the HP15C calculator in python. Not 100% accurate to the original, but that is not the intention. 

100% human written code, no AI written code here.  
However, I did use AI to review some of my code in moments of doubt.  
Whenever asking it to review my code, I did specifically ask it to not provide any code, and only the solution using words.  

The HP15C is an RPN (Reverse Polish Notation) calculator.
It doesn't work like the typical calculator where you just write your operation and it executes (ex: 1+1).  
Instead, it uses a stack with 4 different registers, x, y, z and t.  
To do 1+1, the user needs to do the following input sequence:   

**1  
Enter  
1  
+**

So if you find yourself confused using this calculator, that's normal. It's not your typical calculator.

If you want a user manual of the HP15C, please head here:
https://h10032.www1.hp.com/ctg/Manual/c03030589.pdf


This project currently consists of just 2 files.  
Py15C is the logic for the calculator.  
python15c buttons and display is for... well, the buttons and display. However this file is currently completely useless and is just mostly random code that will probably be obsolete by the time I finish Py15C.  
Its purpose will be the UI and some small logic that will interact with the main calculator logic (most notably clearing error messages at the press of any key).  


For now this program stores all variables and settings temporarily, however I plan on adding permanent variable and setting storage (whilst respecting the HP15C's original storage conditions).

The program is currently not meant to be used.
The only way it can be used is by directly calling functions.
The 1+1 example from before can be performed with the following sequence:
calc.stack.add_element_to_stack(1)
calc.stack.add_element_to_stack(1)
calc.math.addition()
(and optionally, since there is no display for now, you can do calc.stack.show_stack_for_debug() to show the result of the addition in the stack)

There is no function for enter, as this has to be implemented later when the UI and display logic is going to be coded
