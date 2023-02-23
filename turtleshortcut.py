import turtle

class TurtleShortcut:
    
    def __init__(self, t):
        self.t = t

    def square(self, length):
        for i in range(0,4):
            self.t.forward(length)
            self.t.right(90)
    
    def triangle(self, length):
        for i in range(0,3):
            self.t.forward(length)
            self.t.right(120)

    def pentagon(self, length):
        for i in range(0,5):
            self.t.forward(length)
            self.t.right(360/5)
        
