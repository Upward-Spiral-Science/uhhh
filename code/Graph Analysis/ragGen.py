# Methods for generating Region Adjacency Graphs
import networkx as nx
import numpy as np

# Generates the Region Adjacency Graph
def generate_rag(im, linear):
    G=nx.Graph()

    if linear == True:
        (max_diff, min_diff) = get_diff_range(im)
        scale_factor = 1/(max_diff - min_diff)

    x = 0
    for col in im:
        y = 0
        for pix in col:
            point = (x,y)
            neighs = get_neighbors(point, im)

            if linear == True:
                weights = get_weights_linear(im, point, neighs, scale_factor)
            else:
                weights = get_weights_nonlinear(im, point, neighs)

            to_add = []
            which = 0
            for neigh in neighs:
                if neigh != None:
                    to_add.append((point, neigh, weights[which]))
                    which+=1
#             print to_add
            G.add_weighted_edges_from(to_add)
            y+=1
        x+=1

    return G


# point = tuple containing index of point (position)
# returns list of neighbors in [north, east, south, west]
def get_neighbors(point, image):
    shape = np.shape(image)
    neighbors = []

    # North
    neighbors.append((point[0], point[1]-1)) if point[1]>0 else neighbors.append(None)
    # East
    neighbors.append((point[0]+1, point[1])) if point[0]<shape[0]-1 else neighbors.append(None)
    # South
    neighbors.append((point[0], point[1]+1)) if point[1]<shape[1]-1 else neighbors.append(None)
    # West
    neighbors.append((point[0]-1, point[1])) if point[0]>0 else neighbors.append(None)

    return neighbors


# calculates weights between nodes
# weight defined as inverse absolute distance
def get_weights_nonlinear(image, point, neighbors):
    weights = []
    for neigh in neighbors:
        if neigh != None:
            weight = 1/(abs(image[point] - image[neigh])+1)
            weights.append(weight)
    return weights


# calculates weights between nodes
# weight scaled and linear
# TODO: Explain weighting difference with math
def get_weights_linear(image, point, neighbors, scale_factor):

    weights = []
    for neigh in neighbors:
        if neigh != None:
            diff = abs(image[point] - image[neigh])
            weight = 1 - (scale_factor*diff)
            weights.append(weight)

    return weights


def populate_graph(G, im):
    nodes_to_add = []
    for x in range(np.shape(im)[0]):
        for y in range(np.shape(im)[1]):
            nodes_to_add.append((x,y))

    G.add_nodes_from(nodes_to_add)

# returns the max and min difference in node weight
# to be used for scaling edges in graph
def get_diff_range(image):
    diffs = []

    x = 0
    for col in image:
        y = 0
        for pix in col:
            point = (x,y)
            neighs = get_neighbors(point, image)

            for neigh in neighs:
                if neigh != None:
                    diffs.append(abs(image[point] - image[neigh]))

            y+=1
        x+=1
    return (max(diffs), min(diffs))
