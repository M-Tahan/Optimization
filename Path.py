import numpy as np
import GUI
from tkinter import *
import random
class path:
    def room1_path(self,nodes,position):
        self.room1 = np.array([[0 for _ in range(3)] for _ in range(9)])
        next_pos = np.array([[0 for _ in range(3)] for _ in range(1)])
        next_pos = position
        # GUI file:
        self.room1[0][0], self.room1[0][1], self.room1[0][2] = nodes[0][0], nodes[0][1], nodes[0][2]
        self.room1[1][0], self.room1[1][1], self.room1[1][2] = nodes[1][0], nodes[1][1], nodes[1][2]
        self.room1[2][0], self.room1[2][1], self.room1[2][2] = nodes[7][0], nodes[7][1], nodes[7][2]
        self.room1[3][0], self.room1[3][1], self.room1[3][2] = nodes[8][0], nodes[8][1], nodes[8][2]
        self.room1[4][0], self.room1[4][1], self.room1[4][2] = nodes[14][0], nodes[14][1], nodes[14][2]
        self.room1[5][0], self.room1[5][1], self.room1[5][2] = nodes[15][0], nodes[15][1], nodes[15][2]
        self.room1[6][0], self.room1[6][1], self.room1[6][2] = nodes[21][0], nodes[21][1], nodes[21][2]
        self.room1[7][0], self.room1[7][1], self.room1[7][2] = nodes[22][0], nodes[22][1], nodes[22][2]
        self.room1[8][0], self.room1[8][1], self.room1[8][2] = nodes[54][0], nodes[54][1], nodes[54][2]
        self.path = np.array([[0 for _ in range(3)] for _ in range(1)])
        i=1
        self.path = next_pos
        j=2
        x = 0
        while position.all() != self.room1[8].all():
            self.new_path = np.array([[0 for _ in range(3)] for _ in range(j)])
            rand = random.randint(1,8)
            # if i < 7 :
            #     x = 0
            #     while x < len(self.path):
            #         self.new_path[x][0],self.new_path[x][1],self.new_path[x][2] = self.path[x][0],self.path[x][1],self.path[x][2]
            #         x = x + 1
            #     self.new_path[i][0],self.new_path[i][1],self.new_path[i][2] = 1,1,1
            #     print(self.new_path) 
            if ((next_pos[0][0] == self.room1[6][0]) and (next_pos[0][1] == self.room1[6][1])) or ((next_pos[0][0] == self.room1[7][0])and (next_pos[0][1] == self.room1[7][1])):
                x = 0
                while x < len(self.path):
                    self.new_path[x] = self.path[x]
                    x = x + 1
                next_pos = self.room1[8]
                self.new_path[i] = next_pos
                # self.new_path[i][0],self.new_path[i][1],self.new_path[i][2] = self.room1[8][0], self.room1[8][1], self.room1[8][2]
                break
            #new path
            elif (rand ==1):
                next_pos[0][0] = next_pos[0][0]-100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(self.room1,next_pos)
                if next_pos[0][2] == 9:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0] + 100
                    next_pos[0][2] = temp
                elif (path.compare(path,next_pos)) == FALSE:
                    x = 0
                    while x < len(self.path):
                        self.new_path[x] = self.path[x]
                        x = x + 1
                    self.new_path[i] = next_pos
                elif (path.compare(path,next_pos)) == TRUE:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0]

            elif (rand ==2):
                next_pos[0][0] = next_pos[0][0]-100
                next_pos[0][1] = next_pos[0][1]+100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(self.room1,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 2:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] +100
                    next_pos[0][1] = next_pos[0][1]-100
                    next_pos[0][2] = temp
                elif (path.compare(path,next_pos)) == FALSE:
                    x = 0
                    while x < len(self.path):
                        self.new_path[x] = self.path[x]
                        x = x + 1
                    self.new_path[i] = next_pos
                elif (path.compare(path,next_pos)) == TRUE:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0]  
            
            elif (rand ==3):
                
                next_pos[0][1] = next_pos[0][1]+100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(self.room1,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 3:
                        rand =random.randint(1,8)
                    next_pos[0][1] = next_pos[0][1] +100
                    next_pos[0][2] = temp
                elif (path.compare(path,next_pos)) == FALSE:
                    x = 0
                    while x < len(self.path):
                        self.new_path[x] = self.path[x]
                        x = x + 1
                    self.new_path[i] = next_pos
                elif (path.compare(path,next_pos)) == TRUE:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0]

            elif (rand ==4):
                next_pos[0][0] = next_pos[0][0]+100
                next_pos[0][1] = next_pos[0][1]+100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(self.room1,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 4:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0]-100
                    next_pos[0][1] = next_pos[0][1]-100
                    next_pos[0][2] = temp
                elif (path.compare(path,next_pos)) == FALSE:
                    x = 0
                    while x < len(self.path):
                        self.new_path[x] = self.path[x]
                        x = x + 1
                    self.new_path[i] = next_pos
                elif (path.compare(path,next_pos)) == TRUE:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0]
            
            elif (rand ==5):
                next_pos[0][0] = next_pos[0][0]+100
                next_pos[0][1] = next_pos[0][1]
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(self.room1,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 5:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] -100
                    next_pos[0][2] = temp
                elif (path.compare(path,next_pos)) == FALSE:
                    x = 0
                    while x < len(self.path):
                        self.new_path[x] = self.path[x]
                        x = x + 1
                    self.new_path[i] = next_pos
                elif (path.compare(path,next_pos)) == TRUE:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0]

            elif (rand ==6):
                next_pos[0][0] = next_pos[0][0]-100
                next_pos[0][1] = next_pos[0][1]-100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(self.room1,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 6:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] +100
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                elif (path.compare(path,next_pos)) == FALSE:
                    x = 0
                    while x < len(self.path):
                        self.new_path[x] = self.path[x]
                        x = x + 1
                    self.new_path[i] = next_pos
                elif (path.compare(path,next_pos)) == TRUE:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0]

            elif (rand ==7):
                next_pos[0][0] = next_pos[0][0]
                next_pos[0][1] = next_pos[0][1]-100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(self.room1,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 7:
                        rand =random.randint(1,8)
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                elif (path.compare(path,next_pos)) == FALSE:
                    x = 0
                    while x < len(self.path):
                        self.new_path[x] = self.path[x]
                        x = x + 1
                    self.new_path[i] = next_pos
                elif (path.compare(path,next_pos)) == TRUE:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0]

            elif (rand ==8):
                next_pos[0][0] = next_pos[0][0] -100
                next_pos[0][1] = next_pos[0][1]-100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(self.room1,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 7:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] +100
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                elif (path.compare(path,next_pos)) == FALSE:
                    x = 0
                    while x < len(self.path):
                        self.new_path[x] = self.path[x]
                        x = x + 1
                    self.new_path[i] = next_pos
                elif (path.compare(path,next_pos)) == TRUE:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0]   
            # elif (rand_pick == 1) and ()
            self.path = np.array([[0 for _ in range(3)] for _ in range(j)])
            x = 0
            i = i+1
            j = j + 1
            while x < len(self.path):
                    self.new_path[x] = self.path[x]
                    x = x + 1
        print(self.new_path)    
    

    def room2_path(self,nodes,position):
        self.room2 = np.array([[0 for _ in range(3)] for _ in range(21)])
        # GUI file:
        self.room2[0][0], self.room2[0][1], self.room2[0][2] = nodes[2][0], nodes[2][1], nodes[2][2]
        self.room2[1][0], self.room2[1][1], self.room2[1][2] = nodes[3][0], nodes[3][1], nodes[3][2]
        self.room2[2][0], self.room2[2][1], self.room2[2][2] = nodes[9][0], nodes[9][1], nodes[9][2]
        self.room2[3][0], self.room2[3][1], self.room2[3][2] = nodes[10][0], nodes[10][1], nodes[10][2]
        self.room2[4][0], self.room2[4][1], self.room2[4][2] = nodes[16][0], nodes[16][1], nodes[16][2]
        self.room2[5][0], self.room2[5][1], self.room2[5][2] = nodes[17][0], nodes[17][1], nodes[17][2]
        self.room2[6][0], self.room2[6][1], self.room2[6][2] = nodes[23][0], nodes[23][1], nodes[23][2]
        self.room2[7][0], self.room2[7][1], self.room2[7][2] = nodes[24][0], nodes[24][1], nodes[24][2]
        self.room2[8][0], self.room2[8][1], self.room2[8][2] = nodes[28][0], nodes[28][1], nodes[28][2]
        self.room2[9][0], self.room2[9][1], self.room2[9][2] = nodes[29][0], nodes[29][1], nodes[29][2]
        self.room2[10][0], self.room2[10][1], self.room2[10][2] = nodes[30][0], nodes[30][1], nodes[30][2]
        self.room2[11][0], self.room2[11][1], self.room2[11][2] = nodes[31][0], nodes[31][1], nodes[31][2]
        self.room2[12][0], self.room2[12][1], self.room2[12][2] = nodes[35][0], nodes[35][1], nodes[35][2]
        self.room2[13][0], self.room2[13][1], self.room2[13][2] = nodes[36][0], nodes[36][1], nodes[36][2]
        self.room2[14][0], self.room2[14][1], self.room2[14][2] = nodes[37][0], nodes[37][1], nodes[37][2]
        self.room2[15][0], self.room2[15][1], self.room2[15][2] = nodes[38][0], nodes[38][1], nodes[38][2]
        self.room2[16][0], self.room2[16][1], self.room2[16][2] = nodes[39][0], nodes[39][1], nodes[39][2]
        self.room2[17][0], self.room2[17][1], self.room2[17][2] = nodes[40][0], nodes[40][1], nodes[40][2]
        self.room2[18][0], self.room2[18][1], self.room2[18][2] = nodes[41][0], nodes[41][1], nodes[41][2]
        self.room2[19][0], self.room2[19][1], self.room2[19][2] = nodes[42][0], nodes[42][1], nodes[42][2]
        self.room2[20][0], self.room2[20][1], self.room2[20][2] = nodes[56][0], nodes[56][1], nodes[56][2]
        


    def room3_path(self,nodes,position):
        self.room3 = np.array([[0 for _ in range(3)] for _ in range(16)])
        self.room3[0][0],self.room3[0][1],self.room3[0][2] = nodes[4][0],nodes[4][1],nodes[4][2]
        self.room3[1][0],self.room3[1][1],self.room3[1][2] = nodes[5][0],nodes[5][1],nodes[5][2]
        self.room3[2][0],self.room3[2][1],self.room3[2][2] = nodes[6][0],nodes[6][1],nodes[6][2]
        self.room3[3][0],self.room3[3][1],self.room3[3][2] = nodes[11][0],nodes[11][1],nodes[11][2]
        self.room3[4][0],self.room3[4][1],self.room3[4][2] = nodes[12][0],nodes[12][1],nodes[12][2]
        self.room3[5][0],self.room3[5][1],self.room3[5][2] = nodes[13][0],nodes[13][1],nodes[13][2]
        self.room3[6][0],self.room3[6][1],self.room3[6][2] = nodes[18][0],nodes[18][1],nodes[18][2]
        self.room3[7][0],self.room3[7][1],self.room3[7][2] = nodes[19][0],nodes[19][1],nodes[19][2]
        self.room3[8][0],self.room3[8][1],self.room3[8][2] = nodes[20][0],nodes[20][1],nodes[20][2]
        self.room3[9][0],self.room3[9][1],self.room3[9][2] = nodes[25][0],nodes[25][1],nodes[25][2]
        self.room3[10][0],self.room3[10][1],self.room3[10][2] = nodes[26][0],nodes[26][1],nodes[26][2]
        self.room3[11][0],self.room3[11][1],self.room3[11][2] = nodes[27][0],nodes[27][1],nodes[27][2]
        self.room3[12][0],self.room3[12][1],self.room3[12][2] = nodes[32][0],nodes[32][1],nodes[32][2]
        self.room3[13][0],self.room3[13][1],self.room3[13][2] = nodes[33][0],nodes[33][1],nodes[33][2]
        self.room3[14][0],self.room3[14][1],self.room3[14][2] = nodes[34][0],nodes[34][1],nodes[34][2]
        self.room3[15][0],self.room3[15][1],self.room3[15][2] = nodes[55][0],nodes[55][1],nodes[55][2]
            
        

    def room4_path(self,nodes,position):
        self.room4 = np.array([[0 for _ in range(3)] for _ in range(12)])
        i = 0
        k = 44
        while k !=53:
            self.room4[i][0],self.room4[i][1],self.room4[i][2] = nodes[k][0],nodes[k][1],nodes[k][2]
            k = k+1
            i = i+1
        self.room4[11][0],self.room4[11][1],self.room4[11][2] = nodes[57][0],nodes[57][1],nodes[57][2]
    
    def search(node,comp):
        i = 0 
        while i < len(node):
            if node[i].all() == comp:
                return(i)
                break 
    def compare(node,comp):
        i = 0
        x = FALSE 
        while i < len(node):
            if node[i].all() == comp.all():
                x = TRUE
                break
        return(x)

    def get_level(node,comp):
        i = 0 
        while i < len(node):
            if (node[i][0] == comp[i][0]) and (node[i][1] == comp[i][1]):
                return(node[i][2])
                break 
        return(9)    
root = Tk()
root.geometry("1000x1000")
world = GUI.mapBuild(root)
nodes = GUI.mapBuild(root).nodes_creator()
mainloop()
door1 = np.array([[0 for _ in range(3)] for _ in range(1)])
door1[0][0],door1[0][1],door1[0][2] = nodes[0][0], nodes[0][1], nodes[0][2]
path().room1_path(nodes,door1)