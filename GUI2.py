from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import random
class mapBuild():
    def nodes_creator_room1(self):
        l = random.randint(1,3)
        self.nodes = np.array([[0 for _ in range(3)] for _ in range(8)])
        self.nodes[7][0],self.nodes[7][1],self.nodes[7][2]= 80 , 400 , 0
        self.nodes[1][1],self.nodes[1][1],self.nodes[1][2]= 50 , 50 , random.randint(1,3)
        self.nodes[2][0],self.nodes[2][1],self.nodes[2][2]= 100 ,100 , random.randint(1,3)
        self.nodes[3][0],self.nodes[3][1],self.nodes[3][2]= 50 , 100 , random.randint(1,3)
        self.nodes[4][0],self.nodes[4][1],self.nodes[4][2]= 100 , 50 , random.randint(1,3)
        self.nodes[5][0],self.nodes[5][1],self.nodes[5][2]= 50 , 150 , random.randint(1,3)
        self.nodes[6][0],self.nodes[6][1],self.nodes[6][2]= 100 , 150 , random.randint(1,3)
        color = ""
        for i in range(8):
            if self.nodes[i][2] == 0:
                color = 'black'
            elif self.nodes[i][2] == 1:
                color ='green'
            elif self.nodes[i][2] == 2:
                color ='orange'
            elif self.nodes[i][2] == 3:
                color ='yellow'
            elif self.nodes[i][2] == 4:
                color ='red'
            elif self.nodes[i][2] == 5:
                color ='brown'
        for i in range(8):
            self.canvas.create_oval((self.nodes[i][0]-3),(self.nodes[i][1]-3),(self.nodes[i][0]+3),(self.nodes[i][1]+3),fill=color)
            self.canvas.create_text((self.nodes[i][0]-3),(self.nodes[i][1]-3), text=i)   
        return(self.nodes)
    def nodes_creator_room2(self):
        l = random.randint(1,3)
        self.nodes = np.array([[0 for _ in range(3)] for _ in range(8)])
        self.nodes[5][0],self.nodes[7][1],self.nodes[7][2]= 800 , 200 , 0
        self.nodes[1][1],self.nodes[1][1],self.nodes[1][2]= 450 , 50 , l
        self.nodes[2][0],self.nodes[2][1],self.nodes[2][2]= 450 ,100 , l
        self.nodes[3][0],self.nodes[3][1],self.nodes[3][2]= 500 , 100 , l
        self.nodes[4][0],self.nodes[4][1],self.nodes[4][2]= 500 , 50 , l
        color = ""
        for i in range(len(self.nodes)):
            if self.nodes[i][2] == 0:
                color = "black"
            elif self.nodes[i][2] == 1:
                color ="green"
            elif self.nodes[i][2] == 2:
                color ="orange"
            elif self.nodes[i][2] == 3:
                color ="yellow"
            elif self.nodes[i][2] == 4:
                color ="red"
            elif self.nodes[i][2] == 5:
                color ="brown"
        for i in range(len(self.nodes)):
            self.canvas.create_oval((self.nodes[i][0]-3),(self.nodes[i][1]-3),(self.nodes[i][0]+3),(self.nodes[i][1]+3),fill=color)
            self.canvas.create_text((self.nodes[i][0]-3),(self.nodes[i][1]-3), text=i)   
        return(self.nodes)
        
    def nodes_creator_room3(self):
        l = random.randint(1,3)
        self.nodes = np.array([[0 for _ in range(3)] for _ in range(8)])
        self.nodes[5][0],self.nodes[5][1],self.nodes[5][2]= 400 , 140 , 0
        self.nodes[1][1],self.nodes[1][1],self.nodes[1][2]= 150 , 50 , l
        self.nodes[2][0],self.nodes[2][1],self.nodes[2][2]= 150 ,100 , l
        self.nodes[3][0],self.nodes[3][1],self.nodes[3][2]= 200 , 100 , l
        self.nodes[4][0],self.nodes[4][1],self.nodes[4][2]= 200 , 50 , l
        color = ""
        for i in range(len(self.nodes)):
            if self.nodes[i][2] == 0:
                color = "black"
            elif self.nodes[i][2] == 1:
                color ="green"
            elif self.nodes[i][2] == 2:
                color ="orange"
            elif self.nodes[i][2] == 3:
                color ="yellow"
            elif self.nodes[i][2] == 4:
                color ="red"
            elif self.nodes[i][2] == 5:
                color ="brown"
        for i in range(len(self.nodes)):
            self.canvas.create_oval((self.nodes[i][0]-3),(self.nodes[i][1]-3),(self.nodes[i][0]+3),(self.nodes[i][1]+3),fill=color)
            self.canvas.create_text((self.nodes[i][0]-3),(self.nodes[i][1]-3), text=i)   
        return(self.nodes)
    def nodes_creator_room4(self):
        l = random.randint(1,3)
        self.nodes = np.array([[0 for _ in range(3)] for _ in range(8)])
        self.nodes[7][0],self.nodes[7][1],self.nodes[7][2]= 80 , 400 , 0
        self.nodes[1][1],self.nodes[1][1],self.nodes[1][2]= 50 , 50 , random.randint(1,3)
        self.nodes[2][0],self.nodes[2][1],self.nodes[2][2]= 100 ,100 , random.randint(1,3)
        self.nodes[3][0],self.nodes[3][1],self.nodes[3][2]= 50 , 100 , random.randint(1,3)
        self.nodes[4][0],self.nodes[4][1],self.nodes[4][2]= 100 , 50 , random.randint(1,3)
        self.nodes[5][0],self.nodes[5][1],self.nodes[5][2]= 50 , 150 , random.randint(1,3)
        self.nodes[6][0],self.nodes[6][1],self.nodes[6][2]= 100 , 150 , random.randint(1,3)
        color = ""
        for i in range(8):
            if self.nodes[i][2] == 0:
                color = "black"
            elif self.nodes[i][2] == 1:
                color ="green"
            elif self.nodes[i][2] == 2:
                color ="orange"
            elif self.nodes[i][2] == 3:
                color ="yellow"
            elif self.nodes[i][2] == 4:
                color ="red"
            elif self.nodes[i][2] == 5:
                color ="brown"
        for i in range(8):
            self.canvas.create_oval((self.nodes[i][0]-3),(self.nodes[i][1]-3),(self.nodes[i][0]+3),(self.nodes[i][1]+3),fill=color)
            self.canvas.create_text((self.nodes[i][0]-3),(self.nodes[i][1]-3), text=i)   
        return(self.nodes)


    def nodes_creator_room5(self):
        l = random.randint(1,3)
        self.nodes = np.array([[0 for _ in range(3)] for _ in range(8)])
        self.nodes[7][0],self.nodes[7][1],self.nodes[7][2]= 80 , 400 , 0
        self.nodes[1][1],self.nodes[1][1],self.nodes[1][2]= 50 , 50 , random.randint(1,3)
        self.nodes[2][0],self.nodes[2][1],self.nodes[2][2]= 100 ,100 , random.randint(1,3)
        self.nodes[3][0],self.nodes[3][1],self.nodes[3][2]= 50 , 100 , random.randint(1,3)
        self.nodes[4][0],self.nodes[4][1],self.nodes[4][2]= 100 , 50 , random.randint(1,3)
        self.nodes[5][0],self.nodes[5][1],self.nodes[5][2]= 50 , 150 , random.randint(1,3)
        self.nodes[6][0],self.nodes[6][1],self.nodes[6][2]= 100 , 150 , random.randint(1,3)
        color = ""
        for i in range(len(self.nodes)):
            if self.nodes[i][2] == 0:
                color = "black"
            elif self.nodes[i][2] == 1:
                color ="green"
            elif self.nodes[i][2] == 2:
                color ="orange"
            elif self.nodes[i][2] == 3:
                color ="yellow"
            elif self.nodes[i][2] == 4:
                color ="red"
            elif self.nodes[i][2] == 5:
                color ="brown"
        for i in range(len(self.nodes)):
            self.canvas.create_oval((self.nodes[i][0]-3),(self.nodes[i][1]-3),(self.nodes[i][0]+3),(self.nodes[i][1]+3),fill=color)
            self.canvas.create_text((self.nodes[i][0]-3),(self.nodes[i][1]-3), text=i)   
        return(self.nodes)
                
            



       
    def __init__(self,root):
        self.canvas = Canvas(root, width=1400 , height= 1000)
        self.canvas.pack()
        self.canvas.create_line(0,800,1200,800,fill="green",width=5)
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
        self.nodes_creator_room1()
        self.nodes_creator_room2()
        self.nodes_creator_room3()
        self.nodes_creator_room4()
        self.nodes_creator_room5()
        
root = Tk()
root.geometry("1200x900")
world = mapBuild(root)
mainloop()