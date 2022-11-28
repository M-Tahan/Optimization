from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import random
# root = Tk()
# root.geometry('1820x920')
# nodes = [(30,30,'X') , (90,90,'Z')]
# for c in nodes:
#     l = Label(root, text=c[2])
#     l.place(x=c[0], y=c[1])

# root.mainloop()
class mapBuild:
    def nodes_creator(self):
        self.nodes = np.array([[0 for _ in range(3)] for _ in range(58)])
        self.nodes[54][0], self.nodes[54][1], self.nodes[54][2] = 400 , 100 , 0
        self.nodes[55][0], self.nodes[55][1], self.nodes[55][2] = 350 , 400 , 0
        self.nodes[56][0], self.nodes[56][1], self.nodes[56][2] = 700 , 200 , 0
        self.nodes[57][0], self.nodes[57][1], self.nodes[57][2] = 900 , 200 , 5
        k=0
        
        for i in range(9):
            for j in range(7):
                if(j > 3 and i == 5) or (j > 3 and i == 8) or (j>4 and i==7) or (j>5 and i==6):
                    pass
                elif (k == 7) or (k == 13) or (k == 14) or (k == 20) or (k == 28) or (k == 31) or (k == 35) or (k == 45) or (k == 51) or (k == 50):
                    
                    self.nodes[k][0],self.nodes[k][1],self.nodes[k][2] = (50+(i*100)), (50+(j*100)),4
                    k=k+1
                else:
                    self.nodes[k][0],self.nodes[k][1],self.nodes[k][2] = (50+(i*100)), (50+(j*100)), random.randint(1,3)
                    k=k+1
        print(self.nodes)
        return(self.nodes)
    # def crowd_pos_room1():

    def __init__(self,root):
        self.canvas = Canvas(root, width=1000 , height= 1000)
        self.canvas.pack()
        self.canvas.create_line(0,200,400,200,fill="green",width=5)
        self.canvas.create_line(5,0,5,1000,fill="green",width=5)
        self.canvas.create_line(5,5,400,5,fill="green",width=5)
        self.canvas.create_line(400,0,400,90,fill="green",width=5)
        self.canvas.create_line(400,110,400,200,fill="green",width=5)
        self.canvas.create_line(400,5,700,5,fill="green",width=5)
        self.canvas.create_line(5,400,340,400,fill="green",width=5)
        self.canvas.create_line(360,400,700,400,fill="green",width=5)
        self.canvas.create_line(700,5,700,190,fill="green",width=5)
        self.canvas.create_line(700,210,700,400,fill="green",width=5)
        self.canvas.create_line(5,700,550,700,fill="green",width=5)
        self.canvas.create_line(550,400,550,700,fill="green",width=5)
        self.canvas.create_line(550,700,900,400,fill="green",width=5)
        self.canvas.create_line(900,400,900,210,fill="green",width=5)
        self.canvas.create_line(900,190,900,5,width=5,fill="green")
        self.canvas.create_text(910,200,text="EXIT")
        nodes = self.nodes_creator()
        color = ""
        for i in range(58):
            if nodes[i][2] == 0:
                color = "black"
            elif nodes[i][2] == 1:
                color = "green"
            elif nodes[i][2] == 2:
                color = "yellow"
            elif nodes[i][2] == 3:
                color = "orange"
            elif nodes[i][2] == 4:
                color = "red"
            elif nodes[i][2] == 5:
                color = "brown"
            self.canvas.create_oval((nodes[i][0]-3),(nodes[i][1]-3),(nodes[i][0]+3),(nodes[i][1]+3),fill=color)
        self.canvas.create_line(900,5,700,5,fill="green",width=5)
        

        self.canvas.create_text(100,200, text="s")

root = Tk()
root.geometry("1000x1000")
world = mapBuild(root)
nodes = mapBuild(root).nodes_creator()
mainloop()