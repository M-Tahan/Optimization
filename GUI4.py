from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import random
class mapBuild:
    def nodes_creator_rooms1(self):
        self.nodes2 = np.array([[0 for _ in range(3)] for _ in range(11)])
        self.nodes2[10][0],self.nodes2[10][1],self.nodes2[10][2]= 800 , 100 , 5
        self.nodes2[4][0],self.nodes2[4][1],self.nodes2[4][2]= 1000 , 30 , random.randint(1,4)
        self.nodes2[8][0],self.nodes2[8][1],self.nodes2[8][2]= 900 ,100 , random.randint(1,4)
        self.nodes2[2][0],self.nodes2[2][1],self.nodes2[2][2]= 1100 , 100 , random.randint(1,4)
        self.nodes2[7][0],self.nodes2[7][1],self.nodes2[7][2]= 900 , 30 , random.randint(1,4)
        self.nodes2[9][0],self.nodes2[9][1],self.nodes2[9][2]= 900 , 170 , random.randint(1,4)
        self.nodes2[6][0],self.nodes2[6][1],self.nodes2[6][2]= 1000 , 170 , random.randint(1,4)
        self.nodes2[3][0],self.nodes2[3][1],self.nodes2[3][2]= 1100 , 170 , random.randint(1,4)
        self.nodes2[5][0],self.nodes2[5][1],self.nodes2[5][2]= 1000 , 100 , random.randint(1,3)
        self.nodes2[1][0],self.nodes2[1][1],self.nodes2[1][2]= 1100 , 30 , random.randint(1,3)
        color = ''
        for i in range(len(self.nodes2)):
            # print(self.nodes2[i][2])
            if self.nodes2[i][2] == 0:
                color = 'black'
            elif self.nodes2[i][2] == 1:
                color ='green'
            elif self.nodes2[i][2] == 2:
                color ='orange'
            elif self.nodes2[i][2] == 3:
                color ='yellow'
            elif self.nodes2[i][2] == 4:
                color ='red'
            elif self.nodes2[i][2] == 5:
                color ='brown'

            self.canvas.create_oval((self.nodes2[i][0]-15),(self.nodes2[i][1]-15),(self.nodes2[i][0]+15),(self.nodes2[i][1]+15),fill=color)
            self.canvas.create_text((self.nodes2[i][0]-15),(self.nodes2[i][1]-15), text=i)   
        return(self.nodes2)


    
    def nodes_creator_upper_rooms(self):
        self.nodes = np.array([[0 for _ in range(3)] for _ in range(11)])
        # l = random.randint(1,3)
        self.nodes[1][0],self.nodes[1][1],self.nodes[1][2]= 100 , 30 , random.randint(1,4)
        self.nodes[2][0],self.nodes[2][1],self.nodes[2][2]= 100 ,100 , random.randint(1,4)
        self.nodes[5][0],self.nodes[5][1],self.nodes[5][2]= 200 , 100 , random.randint(1,4)
        self.nodes[4][0],self.nodes[4][1],self.nodes[4][2]= 200 , 30 , random.randint(1,4)
        self.nodes[6][0],self.nodes[6][1],self.nodes[6][2]= 200 , 170 , random.randint(1,4)
        self.nodes[8][0],self.nodes[8][1],self.nodes[8][2]= 300 , 100 , random.randint(1,4)
        self.nodes[7][0],self.nodes[7][1],self.nodes[7][2]= 300 , 30 , random.randint(1,3)
        self.nodes[9][0],self.nodes[9][1],self.nodes[9][2]= 300 , 170 , random.randint(1,3)
      
        self.nodes[10][0],self.nodes[10][1],self.nodes[10][2]= 400 , 100 , 5
        self.nodes[3][0],self.nodes[3][1],self.nodes[3][2]= 100 , 170 , random.randint(1,3)
        color = ''
        for i in range(len(self.nodes)):
            print(self.nodes[i][2])
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

            self.canvas.create_oval((self.nodes[i][0]-15),(self.nodes[i][1]-15),(self.nodes[i][0]+15),(self.nodes[i][1]+15),fill=color)
            self.canvas.create_text((self.nodes[i][0]-15),(self.nodes[i][1]-15), text=i)   
        return(self.nodes)
        

    

    def nodes_creator_obstacles(self):
        k=0
        self.nodes1 = np.array([[0 for _ in range(3)] for _ in range(89)])
        for j in range(8):
            for i in range(11):
                self.nodes1[k][0],self.nodes1[k][1],self.nodes1[k][2] = (100+(i*100)), (240+(j*70)),random.randint(1,4)
                k= k+1    
        self.nodes1[23][0],self.nodes1[23][1],self.nodes1[23][2] = 500 , 30 ,random.randint(1,4) 
        self.nodes1[34][0],self.nodes1[34][1],self.nodes1[34][2] = 600 , 30 ,random.randint(1,4)
        self.nodes1[45][0],self.nodes1[45][1],self.nodes1[45][2] = 700 , 30 ,random.randint(1,4)
        self.nodes1[27][0],self.nodes1[27][1],self.nodes1[27][2] = 500 , 100 ,random.randint(1,4) 
        self.nodes1[38][0],self.nodes1[38][1],self.nodes1[38][2] = 600 , 100 ,random.randint(1,4)
        self.nodes1[49][0],self.nodes1[49][1],self.nodes1[49][2] = 700 , 100 ,random.randint(1,4)  
        self.nodes1[31][0],self.nodes1[31][1],self.nodes1[31][2] = 500 , 170 ,random.randint(1,4) 
        self.nodes1[42][0],self.nodes1[42][1],self.nodes1[42][2] = 600 , 170 ,random.randint(1,4)
        self.nodes1[53][0],self.nodes1[53][1],self.nodes1[53][2] = 700 , 170 ,random.randint(1,4)
        self.nodes1[88][0],self.nodes1[88][1],self.nodes1[88][2] = 600 , 780 ,0
        # self.nodes1[68][0],self.nodes1[68][1],self.nodes1[68][2] = 500 , 730 ,random.randint(1,3)
        self.nodes1[86][0],self.nodes1[86][1],self.nodes1[86][2] = 600 , 730 ,random.randint(1,3)
        self.nodes1[87][0],self.nodes1[87][1],self.nodes1[87][2] = 700 , 730 ,random.randint(1,3) 
        # self.nodes1[81][0],self.nodes1[81][1],self.nodes1[81][2] = 900 , 730 ,random.randint(1,3)
        self.nodes1[82][0],self.nodes1[82][1],self.nodes1[82][2] = 1000 , 730 ,random.randint(1,3)
        self.nodes1[83][0],self.nodes1[83][1],self.nodes1[83][2] = 1100 , 730 ,random.randint(1,3)   
  

                 
            
           
        for i in range(len(self.nodes1)):
            if self.nodes1[i][2] == 0:
                color = 'black'
            elif self.nodes1[i][2] == 1:
                color ='green'
            elif self.nodes1[i][2] == 2:
                color ='orange'
            elif self.nodes1[i][2] == 3:
                color ='yellow'
            elif self.nodes1[i][2] == 4:
                color ='red'
            elif self.nodes1[i][2] == 5:
                color ='brown'
            
            if ( i !=79  and i !=74  and i !=85 and i!=68 ): 
              self.canvas.create_oval((self.nodes1[i][0]-15),(self.nodes1[i][1]-15),(self.nodes1[i][0]+15),(self.nodes1[i][1]+15),fill=color)
              self.canvas.create_text((self.nodes1[i][0]-15),(self.nodes1[i][1]-15), text=i)  
        print(self.nodes1)             
        return(self.nodes1)





    def __init__(self,root):
        self.canvas = Canvas(root, width=1200 , height= 900)
        self.canvas.pack()
        self.canvas.create_line(0,0,900,0,fill="green",width=5) #centre_Square
        self.canvas.create_line(1200,0,1200,800,fill="green",width=5)
        self.canvas.create_line(1200,780,620,780,fill="green",width=5)
        self.canvas.create_line(0,780,580,780,fill="green",width=5)
        self.canvas.create_line(0,0,0,880,fill="green",width=5) #
        self.canvas.create_line(400,80,400,0,fill="green",width=5) #Upper rooms
        self.canvas.create_line(400,120,400,200,fill="green",width=5)
        self.canvas.create_line(0,200,400,200,fill="green",width=5) 
        self.canvas.create_line(800,0,800,80,fill="green",width=5) 
        self.canvas.create_line(800,120,800,200,fill="green",width=5)
        self.canvas.create_line(800,200,1200,200,fill="green",width=5)##
        self.canvas.create_line(200,350,200,550,fill="black",width=70)#obstacles 
        self.canvas.create_line(600,350,600,550,fill="black",width=70)
        self.canvas.create_line(1000,350,1000,550,fill="black",width=70)
        self.canvas.create_line(300,650,300,750,fill="black",width=100)
        self.canvas.create_line(900,650,900,750,fill="black",width=100)
        self.nodes_creator_upper_rooms()
        self.nodes_creator_obstacles()
        self.nodes_creator_rooms1()
        

root = Tk()
root.geometry("1000x1000")
world = mapBuild(root)
mainloop()
