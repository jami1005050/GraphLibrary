#Date: 10/21/2019
#Class: CS5310
#Assignment: Graph Library
#Author(s): Mohammad Jaminur Islam

import unittest

from src.edge import Edge
from src.graph import Graph
from src.vertex import Vertex
from utility.constant import UNDIRECTED_GRAPH, DIRECTED_GRAPH


class MyTestCase(unittest.TestCase):

    def test_graph(self): #test
        graph = Graph(UNDIRECTED_GRAPH)
        self.assertIsInstance(graph,Graph) #check if the graph object is a class of Graph

    def test_undirectedGraph(self): #test undirected graph
        graph =Graph(UNDIRECTED_GRAPH)
        assert graph.type == UNDIRECTED_GRAPH #check if the graph is an undirected graph

    def test_directedGraph(self):#test directed graph
        graph = Graph(DIRECTED_GRAPH)
        assert graph.type == DIRECTED_GRAPH#check if the graph is a directed graph

    def test_vertexObject(self): #create vertex creation
        vertex = Vertex(1)
        self.assertIsInstance(vertex,Vertex) #check if it is an instance of an vertex

    def test_edgeObject(self): #test edge creation
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        edge = Edge(vertex1,vertex2) #edge creattion by two verticfes
        self.assertIsInstance(edge,Edge) #check if it is the instance of an edge class

    def test_adjacency(self): #test adjacency
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        edge = Edge(vertex1,vertex2)
        graph = Graph(UNDIRECTED_GRAPH)  #graph object
        graph.insert_edge(edge) #created edge insert
        assert len (vertex1.adjacentList) == 1 #check adjacency for vertex 1
        assert len(graph.vertexList) == 2 #check vertex list size
        assert  len(graph.edgeList) == 1 #check edge list size

    def test_insert_vertex(self): #check insertion of a vertex
        graph = Graph(UNDIRECTED_GRAPH) #undirected graph
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        graph.insert_vertex(vertex1)
        assert len(graph.vertexList) == 1 #check vertex list size
        graph.insert_vertex(vertex2)
        assert len(graph.vertexList) == 2 #after 2nd vertex insert check the size of the vertex

    def test_insert_edge(self): #test edge insertion
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        graph = Graph(UNDIRECTED_GRAPH)  #undirected graph
        graph.insert_vertex(vertex1)
        graph.insert_vertex(vertex1)
        edge = Edge(vertex1, vertex2)
        graph.insert_edge(edge)
        assert len(vertex1.adjacentList) == 1 #test adjacency list size
        assert len(graph.vertexList) == 2
        assert len(graph.edgeList) == 1

    def test_vertex_existence(self): #check if a vertex exist in the graph
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        graph = Graph(UNDIRECTED_GRAPH)
        graph.insert_vertex(vertex1)
        graph.insert_vertex(vertex2)
        assert graph.search_vertex_by_label(1) == vertex1

    def test_remove_edge(self): #delete edge test
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        edge = Edge(vertex1,vertex2)
        graph = Graph(UNDIRECTED_GRAPH)
        graph.insert_edge(edge) #create edge
        assert len (vertex1.adjacentList) == 1
        assert len(graph.vertexList) == 2 #test vertex list before remove
        assert  len(graph.edgeList) == 1 #test edge list before remove
        print("size of the edgelist: ",len(graph.edgeList))
        graph.remove_edge(1,2)
        print("adjacenty list size",len(vertex1.adjacentList))
        assert len(vertex1.adjacentList) == 0  #test adjacency list after remove
        assert len(graph.vertexList) == 2 #test vertex list after remove
        print("length of the edge list: ",len(graph.edgeList))
        assert len(graph.edgeList) == 0 #test edgelist after remove

    def test_remove_vertex(self): #remove vertex test
        graph1 = Graph(UNDIRECTED_GRAPH) #undirected graph
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        vertex3 = Vertex(3)
        vertex4 = Vertex(4)
        vertex5 = Vertex(5)
        vertex6 = Vertex(6) #vertex creation
        graph1.insert_vertex(vertex1)
        graph1.insert_vertex(vertex2)
        graph1.insert_vertex(vertex3)
        graph1.insert_vertex(vertex4)
        graph1.insert_vertex(vertex5)
        graph1.insert_vertex(vertex6) #6 vertex insert
        graph1.insert_edge_by_ends(vertex1, vertex2)
        graph1.insert_edge_by_ends(vertex1, vertex3)
        graph1.insert_edge_by_ends(vertex1, vertex4)
        graph1.insert_edge_by_ends(vertex2, vertex4)
        graph1.insert_edge_by_ends(vertex3, vertex5)
        graph1.insert_edge_by_ends(vertex4, vertex6)
        graph1.insert_edge_by_ends(vertex5, vertex6) #edges insert operation
        print('vertex count before vertex delete: ', graph1.get_vertex_count())
        print("****after vertex remove****")
        graph1.remove_vertex(1) #remove operation
        print('vertex count after vertex delete: ', graph1.get_vertex_count())
        print('edge count after vertex delete: ', graph1.get_edge_count())
        assert len(graph1.edgeList) == 4 #test the edges after vertex remove
        graph1.print_all_edge()

    def test_degree_undirected(self): #test degree of a undirected graph vertex
        print("******undirected graph*******")
        graph1 = Graph(UNDIRECTED_GRAPH)
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        vertex3 = Vertex(3)
        vertex4 = Vertex(4)
        vertex5 = Vertex(5)
        vertex6 = Vertex(6) #6 vertices
        graph1.insert_vertex(vertex1)
        graph1.insert_vertex(vertex2)
        graph1.insert_vertex(vertex3)
        graph1.insert_vertex(vertex4)
        graph1.insert_vertex(vertex5)
        graph1.insert_vertex(vertex6) #insert 6 vertices
        graph1.insert_edge_by_ends(vertex1, vertex2)
        graph1.insert_edge_by_ends(vertex1, vertex3)
        graph1.insert_edge_by_ends(vertex1, vertex4)
        graph1.insert_edge_by_ends(vertex2, vertex4)
        graph1.insert_edge_by_ends(vertex3, vertex5)
        graph1.insert_edge_by_ends(vertex4, vertex6)
        graph1.insert_edge_by_ends(vertex5, vertex6) #edge insertion
        flag = graph1.check_directed(1,2)  #check if the graph is directed or undirected
        print("flag: ",flag)
        assert  graph1.get_degree(4) == 3 # test the degree for vertex 4


    def test_directed_graph(self): #test directed graph
        print("******Directed graph******")
        graphDirected = Graph(DIRECTED_GRAPH) #directed graph creation
        vertex1 = Vertex(1, 1)
        vertex2 = Vertex(2, 2)
        vertex3 = Vertex(3, 3)
        vertex4 = Vertex(4, 4)
        vertex5 = Vertex(5, 5)
        vertex6 = Vertex(6, 6)
        vertex7 = Vertex(7, 7) #directed graph vertex creation

        graphDirected.insert_vertex(vertex1)
        graphDirected.insert_vertex(vertex2)
        graphDirected.insert_vertex(vertex3)
        graphDirected.insert_vertex(vertex4)
        graphDirected.insert_vertex(vertex5)
        graphDirected.insert_vertex(vertex6) #directed graph vertex insert
        graphDirected.insert_edge_by_ends(vertex1, vertex2)
        graphDirected.insert_edge_by_ends(vertex1, vertex3)
        graphDirected.insert_edge_by_ends(vertex2, vertex7)
        graphDirected.insert_edge_by_ends(vertex3, vertex2)
        graphDirected.insert_edge_by_ends(vertex4, vertex3)
        graphDirected.insert_edge_by_ends(vertex4, vertex1)
        graphDirected.insert_edge_by_ends(vertex4, vertex5)
        graphDirected.insert_edge_by_ends(vertex5, vertex1)
        graphDirected.insert_edge_by_ends(vertex5, vertex6)
        graphDirected.insert_edge_by_ends(vertex6, vertex1)
        graphDirected.insert_edge_by_ends(vertex6, vertex7)
        graphDirected.insert_edge_by_ends(vertex7, vertex1) #directed graph edge insert

        # testincoming vertex and edges
        incomingvertexList = graphDirected.get_vertices_form_incoming(1) #get vertices forming incident edeges
        outgoingvertexList = graphDirected.get_vertices_form_outgoing(1) #get vertices forming outgoing edges
        assert len(incomingvertexList) > 0 #test incoming vertex list
        assert len(outgoingvertexList) > 0 #test outgoing vertex list
        incomingedgeList = graphDirected.get_edges_incoming(1) #get edges incident incoming on 1
        outgoingedgeList = graphDirected.get_edges_out_going(1) #get edges incident outgoing on 1

        assert len(incomingedgeList) > 0 #test incoming edge list
        assert len(outgoingedgeList) > 0 #test outgoing edge list

        vertex1 = graphDirected.search_vertex_by_label(1)
        assert isinstance(vertex1,Vertex) #search vertex test

        vertexList = graphDirected.all_adjacent_to(1)
        assert len(vertexList) >0 #check all adjacent vertex list size
        edgeList = graphDirected.get_edges_on_node(1) #get edges on vertex 1

        assert len(edgeList)>0 #test returned edge list
        #testoutgoing vertex and edges
        #searchtest
        #check adjacency of two verteices
        #get edeges on node n
        #getAlladjacent to
        indegree = graphDirected.get_in_degree(1) #indegree test
        outdegree = graphDirected.get_out_degree(1) #outdegree test
        flag = graphDirected.check_directed(4,5)
        print("flag: ",flag)
        assert len(graphDirected.vertexList) == 7 #check vertest list lenght
        assert len(graphDirected.edgeList) == 12
        assert indegree == 4
        assert outdegree == 2

        graphDirected.remove_edge(4, 1) #remove edge
        print("*****After edge remove*****")
        indegree_after_rm = graphDirected.get_in_degree(4)
        outdegree_after_rm = graphDirected.get_out_degree(4)

        assert len(graphDirected.edgeList) == 11 #after remove test edge count
        assert indegree_after_rm == 0  #test indegree count after remove
        assert outdegree_after_rm == 2 #test outdegree count after remove
        print("****after vertex remove****")
        graphDirected.remove_vertex(1) #test remove vertex
        assert len(graphDirected.vertexList) == 6 # check vertex count
        assert len(graphDirected.edgeList) == 6 #check edge count
        graphDirected.print_all_edge() #print test


if __name__ == '__main__':
    unittest.main()
