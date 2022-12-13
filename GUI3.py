from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import random
class mapBuild:
    
    def __init__(self,root):
        self.canvas = Canvas(root, width=1600 , height= 1600)
        self.canvas.pack()
        # self.canvas.create_line(400,250,800,250,fill="green",width=5) #centre_Square
        self.canvas.create_line(400,250,580,250,fill="green",width=5)
        self.canvas.create_line(600,250,800,250,fill="green",width=5)
        self.canvas.create_line(800,250,980,250,fill="green",width=5) 
        self.canvas.create_line(1020,250,1200,250,fill="green",width=5) 
        self.canvas.create_line(1200,250,1200,355,fill="green",width=5)
        self.canvas.create_line(1200,375,1200,500,fill="green",width=5)
        self.canvas.create_line(1200,500,1200,750,fill="green",width=5)
        self.canvas.create_line(400,750,535,750,fill="green",width=5)
        self.canvas.create_line(555,750,700,750,fill="green",width=5)
        self.canvas.create_line(700,750,780,750,fill="green",width=5)
        self.canvas.create_line(800,750,900,750,fill="green",width=5)
        self.canvas.create_line(900,750,1030,750,fill="green",width=5)
        self.canvas.create_line(1050,750,1200,750,fill="green",width=5)
        self.canvas.create_line(400,250,400,355,fill="green",width=5) 
        self.canvas.create_line(400,500,400,605,fill="green",width=5)
        self.canvas.create_line(400,625,400,750,fill="green",width=5)
        self.canvas.create_line(400,375,400,500,fill="green",width=5)##
        self.canvas.create_line(700,500,900,500,fill="black",width=100) #Obstacle
        self.canvas.create_line(400,0,800,0,fill="green",width=5) #upper_rooms
        self.canvas.create_line(400,0,400,250,fill="green",width=5)
        self.canvas.create_line(800,0,1200,0,fill="green",width=5)
        self.canvas.create_line(1200,0,1200,250,fill="green",width=5)
        self.canvas.create_line(800,125,800,250,fill="green",width=5) 
        self.canvas.create_line(800,0,800,105,fill="green",width=5)##
        self.canvas.create_line(200,250,400,250,fill="green",width=5) #Left_rooms
        self.canvas.create_line(200,500,400,500,fill="green",width=5)
        self.canvas.create_line(200,250,200,500,fill="green",width=5)
        self.canvas.create_line(200,500,200,750,fill="green",width=5)
        self.canvas.create_line(200,750,400,750,fill="green",width=5)##
        self.canvas.create_line(400,750,400,1000,fill="green",width=5)# Down_rooms
        self.canvas.create_line(400,1000,1200,1000,fill="green",width=5)
        self.canvas.create_line(700,1000,700,750,fill="green",width=5)
        self.canvas.create_line(900,1000,900,750,fill="green",width=5)
        self.canvas.create_line(1200,1000,1200,750,fill="green",width=5)##
        self.canvas.create_line(1200,250,1400,250,fill="green",width=5)#Exit_room
        self.canvas.create_line(1400,250,1400,355,fill="green",width=5)
        self.canvas.create_line(1400,375,1400,500,fill="green",width=5) 
        self.canvas.create_line(1400,500,1200,500,fill="green",width=5)#
        
        
root = Tk()
root.geometry("2000x2000")
world = mapBuild(root)
mainloop()