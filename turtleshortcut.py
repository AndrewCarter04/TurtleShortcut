import turtle

class TurtleShortcut:
    
    def __init__(self, t):
        self.t = t

    def square(self, length):
        for i in range(0,4):
            self.t.forward(length)
            self.t.right(90)
    
