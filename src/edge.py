#Date: 10/21/2019
#Class: CS5310
#Assignment: Graph Library
#Author(s): Mohammad Jaminur Islam
from src.vertex import Vertex, Adjacency
from utility.constant import BI_DIRECTIONAL_EDGE, OUT_GOING_EDGE, INCOMING_EDGE


class Edge:

    def __init__(self, start = None, end = None, weight=0, type = 0, IN_COMING_EDGE=None):
        if not(start==None): #with initialization adjusting the adjacency list for that node
            if not end == None:
                self.startNode = start
                self.endNode = end
                self.weight = weight
                self.type = type
                if(type == 0):
                    if(isinstance(start,Vertex)):
                        self.startNode.add_adjacent(self.endNode,BI_DIRECTIONAL_EDGE)
                        self.endNode.add_adjacent(self.startNode,BI_DIRECTIONAL_EDGE)
                else:
                    if(isinstance(start,Vertex)):
                        self.startNode.add_adjacent(self.endNode,OUT_GOING_EDGE)
                        self.endNode.add_adjacent(self.startNode,INCOMING_EDGE)

        else:
            self.startNode = start
            self.endNode = end
            self.weight = weight
            self.type = type #directed or undirected