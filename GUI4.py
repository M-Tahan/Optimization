from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import random
class mapBuild:
    
    def __init__(self,root):
        self.canvas = Canvas(root, width=1200 , height= 900)
        self.canvas.pack()
        self.canvas.create_line(0,0,900,0,fill="green",width=5) #centre_Square
        self.canvas.create_line(1200,0,1200,800,fill="green",width=5)
        self.canvas.create_line(1200,900,0,900,fill="green",width=5)
        self.canvas.create_line(0,0,0,880,fill="green",width=5) #
        self.canvas.create_line(400,80,400,0,fill="green",width=5) #Upper rooms
        self.canvas.create_line(400,120,400,200,fill="green",width=5)
        self.canvas.create_line(0,200,400,200,fill="green",width=5) 
        self.canvas.create_line(800,0,800,80,fill="green",width=5) 
        self.canvas.create_line(800,120,800,200,fill="green",width=5)
        self.canvas.create_line(800,200,1200,200,fill="green",width=5)##
        self.canvas.create_line(200,350,200,700,fill="black",width=70)#obstacles 
        self.canvas.create_line(600,350,600,700,fill="black",width=70)
        self.canvas.create_line(1000,350,1000,700,fill="black",width=70)
        self.canvas.create_line(300,750,300,850,fill="black",width=100)
        self.canvas.create_line(900,750,900,850,fill="black",width=100)
        
        
root = Tk()
root.geometry("1100x700")
world = mapBuild(root)
mainloop()