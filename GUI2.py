from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import random
import time
class mapBuild:
    def __init__(self,root):
        self.canvas = Canvas(root, width=1400 , height= 1400)
        self.canvas.pack()
        self.canvas.create_line(0,0,200,0,fill="green",width=5)
        self.canvas.create_line(200,0,400,0,fill="green",width=5)
        self.canvas.create_line(0,0,0,400,fill="green",width=5)
        self.canvas.create_line(0,400,80,400,fill="green",width=5)
        self.canvas.create_line(120,400,200,400,fill="green",width=5) 
        self.canvas.create_line(200,400,200,200,fill="green",width=5)
        self.canvas.create_line(200,400,280,400,fill="green",width=5)
        self.canvas.create_line(320,400,400,400,fill="green",width=5)
        self.canvas.create_line(400,320,400,400,fill="green",width=5)
        self.canvas.create_line(400,200,400,280,fill="green",width=5)
        self.canvas.create_line(400,200,400,120,fill="green",width=5)
        self.canvas.create_line(400,80,400,0,fill="green",width=5)
        self.canvas.create_line(200,200,400,200,fill="green",width=5)
        self.canvas.create_line(200,200,200,80,fill="green",width=5)
        self.canvas.create_line(200,120,200,0,fill="green",width=5)
        self.canvas.create_line(400,400,580,400,fill="green",width=5)
        self.canvas.create_line(620,400,800,400,fill="green",width=5)
        self.canvas.create_line(800,800,800,400,fill="green",width=5)
        self.canvas.create_line(200,0,400,0,fill="green",width=5)
        self.canvas.create_line(400,0,800,0,fill="green",width=5)
        self.canvas.create_line(800,0,800,180,fill="green",width=5)
        self.canvas.create_line(800,220,800,400,fill="green",width=5) 
        self.canvas.create_line(0,400,0,800,fill="green",width=5)
        self.canvas.create_line(0,800,400,800,fill="green",width=5)
        self.canvas.create_line(400,800,400,400,fill="green",width=5)
        self.canvas.create_line(400,800,800,800,fill="green",width=5)
        self.canvas.create_line(800,0,1200,0,fill="green",width=5)
        self.canvas.create_line(1200,0,1200,380,fill="green",width=5)
        self.canvas.create_line(800,800,1200,800,fill="green",width=5)
        self.canvas.create_line(1200,420,1200,800,fill="green",width=5)
        
        
root = Tk()
root.geometry("1400x1400")
world = mapBuild(root)
mainloop()