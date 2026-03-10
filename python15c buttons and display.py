import Py15C

#number_of_digits = 9 (maximum number of displayed digits after the period
class Buttons:
    def __init__(self):
        self.blue_mode = 0 #for blue button
        self.orange_mode = 0 #for orange button
        self.on_status = 0
        
    def on_button(self):
        if self.on_status == 0:
            self.on_status = 1
        else:
            self.on_status = 0
    
    def orange_button(self):
        if blue_mode = 1:
            blue_mode = 0
        if orange_mode == 1:
            orange_mode = 0 #not original behavior, the real hp15c doesnt let you cancel the modifier by pressing it again
        else:
            orange_mode = 1
            
    def blue_button(self):
        if orange_mode == 1:
            orange_mode = 0
        if blue_mode == 1: #not original behavior, the real hp15c doesnt let you cancel the modifier by pressing it again
            blue_mode = 0
        else:
            blue_mode = 1
            
class Display:
    def __init__(self):
        pass
   
    def can_display(self):
       if display_mode = 0:
           self.do_not_display()
       else:
           
           
   self.do_not_display(self):
       return {}
    
#if doing a ui, implement a 7 segment display using lists or even dictionaries
#{digit1:[0,0,0,1,1,1,1]} digit1=placement in the display, list=which elements in the display are activated