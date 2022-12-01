import numpy as np
import GUI
from tkinter import *
import random
class path:
    def room1_path(self,nodes,position):
        self.room1 = np.array([[0 for _ in range(3)] for _ in range(9)])
        # next_pos = np.array([[0 for _ in range(3)] for _ in range(1)])
        # next_pos = position
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
        close_1 = np.array([[0 for _ in range(3)] for _ in range(1)])
        close_1[0][0], close_1[0][1], close_1[0][2] = self.room1[7][0], self.room1[7][1], self.room1[7][2]
        close_2 = np.array([[0 for _ in range(3)] for _ in range(1)])
        close_2[0][0], close_2[0][1], close_2[0][2] = self.room1[6][0], self.room1[6][1], self.room1[6][2]
        room_path = path.Select_path(position,self.room1,self.room1[8],close_2,close_1)
        return(room_path)
    
    def Select_path(position,room_nodes,out,close_1,close_2):
        i=1
        xmin,xmax,ymin,ymax = 0 ,20000 , 0 , 20000
        next_pos = position
        result = np.array([[0 for _ in range(3)] for _ in range(1)])
        result = next_pos
        new_path = np.array([[0 for _ in range(3)] for _ in range(1)])
        j=2
        x = 0
        w = out
        o = np.array([[0 for _ in range(3)] for _ in range(1)])
        
        # o[0][0],o[0][1],o[0][2] = out[0][0],out[0][1],out[0][2]
        o=w
        k = 0
        while (o[0] != next_pos[0][0]) and (o[1] != next_pos[0][1]) and (o[2] != next_pos[0][2]):
        
            new_path = np.array([[0 for _ in range(3)] for _ in range(j)])
            x = 0
            while x < len(result):
                new_path[x] = result[x]
                x = x + 1
            rand = random.randint(1,8)
            #rand = 4
            test = np.array([[0 for _ in range(3)] for _ in range(1)])
            test[0][0],test[0][1],test[0][2] = new_path[i-1][0], new_path[i-1][1], new_path[i-1][2] 
            
            # rand = 6
            
            # if i < 7 :
            #     x = 0
            #     while x < len(self.path):
            #         self.new_path[x][0],self.new_path[x][1],self.new_path[x][2] = self.path[x][0],self.path[x][1],self.path[x][2]
            #         x = x + 1
            #     self.new_path[i][0],self.new_path[i][1],self.new_path[i][2] = 1,1,1
            #     print(self.new_path) 
            #if ((next_pos[0][0] == close_1[0][0]) and (next_pos[0][1] == close_1[0][1])) or ((next_pos[0][0] == close_2[0][0])and (next_pos[0][1] == close_2[0][1])):
            
            if (next_pos[0][0] == close_1[0][0]) or (next_pos[0][0] == close_2[0][0]):
                x = 0
                while x < len(result):
                    new_path[x] = result[x]
                    x = x + 1
                next_pos = out
                
                new_path[i] = next_pos
                i = i+1
                j = j + 1
                # self.new_path[i][0],self.new_path[i][1],self.new_path[i][2] = self.room1[8][0], self.room1[8][1], self.room1[8][2]
                break
            #new path
            elif (rand ==1):
                next_pos[0][0] = next_pos[0][0]-100
                if next_pos[0][0] == -50:
                    next_pos[0][0] = next_pos[0][0] + 100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(room_nodes,next_pos)
                
                
                if next_pos[0][2] == 9:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0] + 100
                    next_pos[0][2] = temp
                elif next_pos[0][2] == 4:
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0] + 100
                    next_pos[0][2] = temp
                elif((test[0][0] != next_pos[0][0]) or (test[0][1] != next_pos[0][1]) or (test[0][2] != next_pos[0][2]))  and path.compare(room_nodes,next_pos,1):
                
                    x = 0
                    while x < len(result):
                        new_path[x] = result[x]
                        x = x + 1
                    new_path[i] = next_pos
                    i = i+1
                    j = j + 1
                elif (test[0][0] == next_pos[0][0]) and (test[0][1] == next_pos[0][1]) and (test[0][2] == next_pos[0][2]):
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0] + 100
                    next_pos[0][2] = temp
                if path.checkRand(rand) == TRUE:
                    i = i - 1
                    j=j-1 

            elif (rand ==2):
                
                next_pos[0][0] = next_pos[0][0]-100
                if next_pos[0][0] == -50:
                    next_pos[0][0] = next_pos[0][0] + 100
                next_pos[0][1] = next_pos[0][1]+100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(room_nodes,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 2:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] +100
                    next_pos[0][1] = next_pos[0][1]-100
                    next_pos[0][2] = temp
                if next_pos[0][2] == 4:
                    while rand == 2:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] +100
                    next_pos[0][1] = next_pos[0][1]-100
                    next_pos[0][2] = temp
                elif((test[0][0] != next_pos[0][0]) or (test[0][1] != next_pos[0][1]) or (test[0][2] != next_pos[0][2]))  and path.compare(room_nodes,next_pos,1):
                
                    x = 0
                    while x < len(result):
                        new_path[x] = result[x]
                        x = x + 1
                    new_path[i] = next_pos
                    i = i+1
                    j = j + 1
                elif (test[0][0] == next_pos[0][0]) and (test[0][1] == next_pos[0][1]) and (test[0][2] == next_pos[0][2]):
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0] +100
                    next_pos[0][1] = next_pos[0][1]-100
                    next_pos[0][2] = temp 
                if path.checkRand(rand) == TRUE:
                    i = i - 1
                    j=j-1  
            
            elif (rand ==3):
                
                next_pos[0][1] = next_pos[0][1]+100
                
                temp = next_pos[0][2]
                
                next_pos[0][2] = path.get_level(room_nodes,next_pos)
                
                if next_pos[0][2] == 9:
                    while rand == 3:
                        rand =random.randint(1,8)
                    next_pos[0][1] = next_pos[0][1] -100
                    next_pos[0][2] = temp
                if next_pos[0][2] == 4:
                    while rand == 3:
                        rand =random.randint(1,8)
                    next_pos[0][1] = next_pos[0][1] -100
                    next_pos[0][2] = temp
                elif((test[0][0] != next_pos[0][0]) or (test[0][1] != next_pos[0][1]) or (test[0][2] != next_pos[0][2]))  and path.compare(room_nodes,next_pos,1):
                
                    x = 0
                    while x < len(result):
                        new_path[x] = result[x]
                        x = x + 1
                    new_path[i] = next_pos
                    i = i+1
                    j = j + 1
                    
                elif (test[0][0] == next_pos[0][0]) and (test[0][1] == next_pos[0][1]) and (test[0][2] == next_pos[0][2]):
                    rand =random.randint(2,8)
                    next_pos[0][1] = next_pos[0][1] -100
                    next_pos[0][2] = temp
                    
                if path.checkRand(rand) == TRUE:
                    i = i - 1
                    j=j-1 

            elif (rand ==4):
                
                next_pos[0][0] = next_pos[0][0]+100
                next_pos[0][1] = next_pos[0][1]+100
                temp = next_pos[0][2]
                
                next_pos[0][2] = path.get_level(room_nodes,next_pos)
                
                
                if next_pos[0][2] == 9:
                    while rand == 4:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0]-100
                    next_pos[0][1] = next_pos[0][1]-100
                    next_pos[0][2] = temp
                elif next_pos[0][2] == 4:
                    while rand == 4:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0]-100
                    next_pos[0][1] = next_pos[0][1]-100
                    next_pos[0][2] = temp   
                elif (test[0][0] == next_pos[0][0]) and (test[0][1] == next_pos[0][1]) and (test[0][2] == next_pos[0][2]):
                
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0]-100
                    next_pos[0][1] = next_pos[0][1]-100
                    next_pos[0][2] = temp
                    
                elif((test[0][0] != next_pos[0][0]) or (test[0][1] != next_pos[0][1]) or (test[0][2] != next_pos[0][2]))  and path.compare(room_nodes,next_pos,1):
                    x = 0
                    while x < len(result):
                        new_path[x] = result[x]
                        x = x + 1
                    
                    new_path[i] = next_pos
                    i = i+1
                    j = j + 1
                    
                if path.checkRand(rand) == TRUE:
                    i = i - 1
                    j=j-1 
            
            elif (rand ==5):
                
                next_pos[0][0] = next_pos[0][0]+100
                next_pos[0][1] = next_pos[0][1]
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(room_nodes,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 5:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] -100
                    next_pos[0][2] = temp
                if next_pos[0][2] == 4:
                    while rand == 5:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] -100
                    next_pos[0][2] = temp
                elif((test[0][0] != next_pos[0][0]) or (test[0][1] != next_pos[0][1]) or (test[0][2] != next_pos[0][2]))  and path.compare(room_nodes,next_pos,1):
                
                    x = 0
                    while x < len(result):
                        new_path[x] = result[x]
                        x = x + 1
                    new_path[i] = next_pos
                    i = i+1
                    j = j + 1
                elif (test[0][0] == next_pos[0][0]) and (test[0][1] == next_pos[0][1]) and (test[0][2] == next_pos[0][2]):
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0] -100
                    next_pos[0][2] = temp
                if path.checkRand(rand) == TRUE:
                    i = i - 1
                    j=j-1 

            elif (rand ==6):
                
                next_pos[0][0] = next_pos[0][0]+100
                next_pos[0][1] = next_pos[0][1]-100
                if next_pos[0][1] == -50:
                    next_pos[0][1] = next_pos[0][1] + 100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(room_nodes,next_pos)
                comp = np.array([[0 for _ in range(3)] for _ in range(1)])
                comp[0][0],comp[0][1],comp[0][2] = next_pos[0][0], next_pos[0][1], next_pos[0][2] 
                
                if next_pos[0][2] == 9:
                    while rand == 6:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] -100
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                    
                if next_pos[0][2] == 4:
                    while rand == 6:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] -100
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                    
                    
                
                elif((test[0][0] != next_pos[0][0]) or (test[0][1] != next_pos[0][1]) or (test[0][2] != next_pos[0][2]))  and path.compare(room_nodes,next_pos,1):
                    x = 0
                    while x < len(result):
                        new_path[x] = result[x]
                        x = x + 1
                    new_path[i] = next_pos
                    i = i+1
                    j = j + 1
                    
                elif (test[0][0] == next_pos[0][0]) and (test[0][1] == next_pos[0][1]) and (test[0][2] == next_pos[0][2]):
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0] -100
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                    
                
                if path.checkRand(rand) == TRUE:
                    i = i - 1
                    j=j-1 

            elif (rand ==7):
                
                next_pos[0][0] = next_pos[0][0]
                next_pos[0][1] = next_pos[0][1]-100
                if next_pos[0][1] == -50:
                    next_pos[0][1] = next_pos[0][1] + 100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(room_nodes,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 7:
                        rand =random.randint(1,8)
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                elif next_pos[0][2] == 4:
                    while rand == 7:
                        rand =random.randint(1,8)
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                elif((test[0][0] != next_pos[0][0]) or (test[0][1] != next_pos[0][1]) or (test[0][2] != next_pos[0][2]))  and path.compare(room_nodes,next_pos,1):
                
                    x = 0
                    while x < len(result):
                        new_path[x] = result[x]
                        x = x + 1
                    new_path[i] = next_pos
                    i = i+1
                    j = j + 1
                elif (test[0][0] == next_pos[0][0]) and (test[0][1] == next_pos[0][1]) and (test[0][2] == next_pos[0][2]):
                    rand =random.randint(2,8)
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                if path.checkRand(rand) == TRUE:
                    i = i - 1
                    j=j-1 

            elif (rand ==8):
                
                next_pos[0][0] = next_pos[0][0] -100
                next_pos[0][1] = next_pos[0][1]-100
                if next_pos[0][1] == -50:
                    next_pos[0][1] = next_pos[0][1] + 100
                if next_pos[0][0] == -50:
                    next_pos[0][0] = next_pos[0][0] + 100
                temp = next_pos[0][2]
                next_pos[0][2] = path.get_level(room_nodes,next_pos)
                if next_pos[0][2] == 9:
                    while rand == 8:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] +100
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                if next_pos[0][2] == 4:
                    while rand == 8:
                        rand =random.randint(1,8)
                    next_pos[0][0] = next_pos[0][0] +100
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                
                elif((test[0][0] != next_pos[0][0]) or (test[0][1] != next_pos[0][1]) or (test[0][2] != next_pos[0][2]))  and path.compare(room_nodes,next_pos,1) :
                    x = 0
                    while x < len(result):
                        new_path[x] = result[x]
                        x = x + 1
                    new_path[i] = next_pos
                    i = i+1
                    j = j + 1
                elif (test[0][0] == next_pos[0][0]) and (test[0][1] == next_pos[0][1]) and (test[0][2] == next_pos[0][2]):
                    rand =random.randint(2,8)
                    next_pos[0][0] = next_pos[0][0] +100
                    next_pos[0][1] = next_pos[0][1]+100
                    next_pos[0][2] = temp
                if path.checkRand(rand) == TRUE:
                    i = i - 1
                    j=j-1   
            # elif (rand_pick == 1) and ()
            result = np.array([[0 for _ in range(3)] for _ in range(j)])
            x = 0
            
            while x < len(new_path):
                    result[x] = new_path[x]
                    x = x + 1
            k = k +1
            if k > 50:
                i=1
                xmin,xmax,ymin,ymax = 0 ,20000 , 0 , 20000
                next_pos = position
                result = np.array([[0 for _ in range(3)] for _ in range(1)])
                result = next_pos
                new_path = np.array([[0 for _ in range(3)] for _ in range(1)])
                j=2
                x = 0
                w = out
                o = np.array([[0 for _ in range(3)] for _ in range(1)])
                
                # o[0][0],o[0][1],o[0][2] = out[0][0],out[0][1],out[0][2]
                o=w
                k = 0

        return(new_path)

    def checkRand(rand):
        arr = [0,0,0,0,0,0,0,0,0]
        i=0
        while i<9:

            if arr[i] == rand:
                x = TRUE
            else:
                x = FALSE
            i=i+1
        if x == TRUE:
            i=0
            while i<9:
                if arr[i] != 0:
                    arr[i] = rand
                i = i +1
        if arr[8] != 0:
            return(FALSE)
        return(FALSE)

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
        close_1 = np.array([[0 for _ in range(3)] for _ in range(1)])
        close_1[0][0], close_1[0][1], close_1[0][2] = self.room2[17][0], self.room2[17][1], self.room2[17][2]
        close_2 = np.array([[0 for _ in range(3)] for _ in range(1)])
        close_2[0][0], close_2[0][1], close_2[0][2] = self.room2[18][0], self.room2[18][1], self.room2[18][2]
        sew = nodes[50]
        room_path = path.Select_path(position,self.room2,self.room2[20],close_2,close_1)
        return(room_path)
        

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
        close_1 = np.array([[0 for _ in range(3)] for _ in range(1)])
        close_1[0][0], close_1[0][1], close_1[0][2] = self.room3[9][0], self.room3[9][1], self.room3[9][2]
        close_2 = np.array([[0 for _ in range(3)] for _ in range(1)])
        close_2[0][0], close_2[0][1], close_2[0][2] = nodes[18][0], nodes[18][1], nodes[18][2]
        room_path = path.Select_path(position,self.room3,self.room3[15],close_2,close_1)
        return(room_path)    
        

    def room4_path(self,nodes,position):
        self.room4 = np.array([[0 for _ in range(3)] for _ in range(12)])
        self.room4[0][0],self.room4[0][1],self.room4[0][2] = nodes[43][0],nodes[43][1],nodes[43][2]
        self.room4[1][0],self.room4[1][1],self.room4[1][2] = nodes[44][0],nodes[44][1],nodes[44][2]
        self.room4[2][0],self.room4[2][1],self.room4[2][2] = nodes[45][0],nodes[45][1],nodes[45][2]
        self.room4[3][0],self.room4[3][1],self.room4[3][2] = nodes[46][0],nodes[46][1],nodes[46][2]
        self.room4[4][0],self.room4[4][1],self.room4[4][2] = nodes[47][0],nodes[47][1],nodes[47][2]
        self.room4[5][0],self.room4[5][1],self.room4[5][2] = nodes[48][0],nodes[48][1],nodes[48][2]
        self.room4[6][0],self.room4[6][1],self.room4[6][2] = nodes[49][0],nodes[49][1],nodes[49][2]
        self.room4[7][0],self.room4[7][1],self.room4[7][2] = nodes[50][0],nodes[50][1],nodes[50][2]
        self.room4[8][0],self.room4[8][1],self.room4[8][2] = nodes[51][0],nodes[51][1],nodes[51][2]
        self.room4[9][0],self.room4[9][1],self.room4[9][2] = nodes[52][0],nodes[52][1],nodes[52][2]
        self.room4[10][0],self.room4[10][1],self.room4[11][2] = nodes[53][0],nodes[53][1],nodes[53][2]
        self.room4[11][0],self.room4[11][1],self.room4[11][2] = nodes[57][0],nodes[57][1],nodes[57][2]
        close_1 = np.array([[0 for _ in range(3)] for _ in range(1)])
        close_1[0][0], close_1[0][1], close_1[0][2] = self.room4[9][0], self.room4[9][1], self.room4[9][2]
        close_2 = np.array([[0 for _ in range(3)] for _ in range(1)])
        close_2[0][0], close_2[0][1], close_2[0][2] = nodes[18][0], nodes[18][1], nodes[18][2]
        room_path = path.Select_path(position,self.room4,nodes[57],close_2,close_1)
        return(room_path) 
    def search(node,comp):
        i = 0 
        while i < len(node):
            if node[i].all() == comp:
                return(i)
                break 
    def compare(nodes,comp,roomnum):
    
        i = 0
        x = FALSE 
        while i < len(nodes):
            
            if (nodes[i][0] == comp[0][0]) and (nodes[i][1] == comp[0][1]) and (nodes[i][2] == comp[0][2]):
            
                x = TRUE
                
                i = len(nodes)
                return(x)
                
                break
            i = i+1
        

    def get_level(node,comp):
        p = 0 
        while p < len(node):
            if ((node[p][0] == comp[0][0])) and (node[p][1] == comp[0][1]):
                x =(node[p][2])
                
                p = len(node)
            else:
                x=9    
            p = p +1
        
        return(x)   

    def get_path_GUI1_room1(nodes,position):
        final_path1 = path().room1_path(nodes,position)
        pos_1 =np.array([[0 for _ in range(3)] for _ in range(1)])
        pos_1[0][0],pos_1[0][1],pos_1[0][2] = nodes[29][0], nodes[29][1], nodes[29][2]
        
        final_path2 = path().room2_path(nodes,pos_1)
        pos_2 =np.array([[0 for _ in range(3)] for _ in range(1)])
        pos_2[0][0],pos_2[0][1],pos_2[0][2] = nodes[46][0], nodes[46][1], nodes[46][2]
        # final_path3 = path().room3_path(nodes,pos_2)
        # pos_3 = final_path3[len(final_path3)-1]
        final_path4 = path().room4_path(nodes,pos_2)
        
        num = len(final_path1) + len(final_path2)  + len(final_path4)
        gg = np.array([[0 for _ in range(3)] for _ in range(num)])
        
        
        
        i = 0 
        j = 0
        while i < (num-3):
            while j < len(final_path1):
                gg[i][0],gg[i][1],gg[i][2] = final_path1[j][0], final_path1[j][1], final_path1[j][2]
                j = j+1
                i = i+1
                
            j = 0
            while j < len(final_path2):
                gg[i][0],gg[i][1],gg[i][2] = final_path2[j][0], final_path2[j][1], final_path2[j][2]
                j = j+1
                i = i+1
                
            # while j < len(final_path3)-1:
            #     gg[i][0],gg[i][1],gg[i][2] = final_path3[j][0], final_path3[j][1], final_path3[j][2]
            #     j = j+1
            #     i = i+1
            j=0
            while j < len(final_path4):
                gg[i][0],gg[i][1],gg[i][2] = final_path4[j][0], final_path4[j][1], final_path4[j][2]
                j = j+1
                i = i+1
                
        return(gg)
# root = Tk()
# root.geometry("1000x1000")
# world = GUI.mapBuild(root)
# nodes = GUI.mapBuild(root).nodes_creator()
# mainloop()
# door1 = np.array([[0 for _ in range(3)] for _ in range(1)])
# door1[0][0],door1[0][1],door1[0][2] = nodes[0][0], nodes[0][1], nodes[0][2]
# print(door1,"how")
# gg = path.get_path_GUI1_room1(nodes,door1)
# print(gg)
# print(door1,"how")