import numpy as np
import GUI
from tkinter import *
class path:
    def room1_path(self,nodes,position):
        self.room1 = np.array([[0 for _ in range(3)] for _ in range(9)])
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
        print(self.room1)
    

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
        print(self.room2)
        print(len(self.room2))

root = Tk()
root.geometry("1000x1000")
world = GUI.mapBuild(root)
nodes = GUI.mapBuild(root).nodes_creator()
mainloop()

path().room2_path(nodes,0)