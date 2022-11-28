import GUI
import numpy as np
import random
from tkinter import *

# class Path_Room1:
#     def getPath(self,nodes,pos):
#         pos = np.array([[0 for _ in range(3)] for _ in range(1)])
#         self.path1 = np.array([[0 for _ in range(3)] for _ in range(600)])
#         position = pos
#         node1 ,node2,node3,node4,node5,node6,node7,node8=np.array([[0 for _ in range(3)] for _ in range(1)]),np.array([[0 for _ in range(3)] for _ in range(1)]),np.array([[0 for _ in range(3)] for _ in range(1)]),np.array([[0 for _ in range(3)] for _ in range(1)]),np.array([[0 for _ in range(3)] for _ in range(1)]),np.array([[0 for _ in range(3)] for _ in range(1)]),np.array([[0 for _ in range(3)] for _ in range(1)]),np.array([[0 for _ in range(3)] for _ in range(1)])
#         exit = np.array([[0 for _ in range(3)] for _ in range(1)])
#         position = np.array([[0 for _ in range(3)] for _ in range(1)])
#         next_node = pos
#         exit[0][0], exit[0][1], exit[0][2] = nodes[54][0] , nodes[54][1] , nodes[54][2]
#         for j in range(58):
#             if (nodes[j][0] == 50) and (nodes[j][1] == 50):
#                 node1[0][0], node1[0][1], node1[0][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#             if (nodes[j][0] == 150) and (nodes[j][1] == 50):
#                 node2[0][0], node2[0][1], node2[0][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#             if (nodes[j][0] == 250) and (nodes[j][1] == 50):
#                 node3[0][0], node3[0][1], node3[0][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#             if (nodes[j][0] == 350) and (nodes[j][1] == 50):
#                 node4[0][0], node4[0][1], node4[0][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#             if (nodes[j][0] == 50) and (nodes[j][1] == 150):
#                 node5[0][0], node5[0][1], node5[0][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#             if (nodes[j][0] == 150) and (nodes[j][1] == 150):
#                 node6[0][0], node6[0][1], node6[0][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#             if (nodes[j][0] == 250) and (nodes[j][1] == 150):
#                 node7[0][0], node7[0][1], node7[0][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#             if (nodes[j][0] == 50) and (nodes[j][1] == 150):
#                 node8[0][0], node8[0][1], node8[0][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]    
#         i = 0
#         self.path1[0][0], self.path1[0][1], self.path1[0][2] = node1[0][0], node1[0][1],node1[0][2]
#         while (position.all() != exit.all()):
#             i = i + 1
#             rand = random.randint(1,5)
#             if (position == node1) and (rand == 1):
#                 self.path1[i][0], self.path1[i][1], self.path1[i][2] = node2[0][0], node2[0][1],node2[0][2]
#             elif (position == node1) and (rand == 2):
#                 self.path1[i][0], self.path1[i][1], self.path1[i][2] = node6[0][0], node6[0][1], node6[0][2]
#             elif (position == node1) and (rand == 3):
#                 self.path1[i][0], self.path1[i][1], self.path1[i][2] = node5[0][0], node5[0][1], node5[0][2]
#             elif (position == node2) and (rand == 1):
                
        
#         print(self.path1)

# def intial_path_from_room_1(self,nodes):
#     room1,room2,room3,room4 = np.array([[0 for _ in range(3)] for _ in range(8)]), np.array([[0 for _ in range(3)] for _ in range(20)]), np.array([[0 for _ in range(3)] for _ in range(15)]), np.array([[0 for _ in range(3)] for _ in range(11)])
#     for j in range(58):
#         if (nodes[j][0] == 50) and (nodes[j][1] == 50):
#             room1[0][0], room1[0][1], room1[0][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#         if (nodes[j][0] == 150) and (nodes[j][1] == 50):
#             room1[1][0], room1[1][1], room1[1][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#         if (nodes[j][0] == 250) and (nodes[j][1] == 50):
#             room1[2][0], room1[2][1], room1[2][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#         if (nodes[j][0] == 350) and (nodes[j][1] == 50):
#             room1[3][0], room1[3][1], room1[3][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#         if (nodes[j][0] == 50) and (nodes[j][1] == 150):
#             room1[4][0], room1[4][1], room1[4][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#         if (nodes[j][0] == 150) and (nodes[j][1] == 150):
#             room1[5][0], room1[5][1], room1[5][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#         if (nodes[j][0] == 250) and (nodes[j][1] == 150):
#             room1[6][0], room1[6][1], room1[6][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#         if (nodes[j][0] == 50) and (nodes[j][1] == 150):
#             room1[7][0], room1[7][1], room1[7][2] = nodes[j][0] , nodes[j][1] , nodes[j][2]
#     position = np.array([[0 for _ in range(3)] for _ in range(1)])
#     position[0][0], position[0][1], position[0][2] = room1[0][0], room1[0][1], room1[0][2]
#     exit = np.array([900,200,5])
#     path = np.array([0,0,0] for _ in range(600))
#     while(position.all() != exit.all()):
def intial_path_from_room_1(self,nodes):
    self.path1 =   [[50,50,nodes[0][2]],[150,150,nodes[8][2]],[]]      
root = Tk()
root.geometry("1000x1000")
world = GUI.mapBuild(root)
nodes = GUI.mapBuild(root).nodes_creator()
# Path_Room1().getPath(nodes,[50,50,1])
mainloop()

