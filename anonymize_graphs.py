import glob
import os
import pickle
import pdb
import networkx as nx
from generate_maps import read_pickle


with open('map_channels.pickle', 'r') as f:
    map_channels = pickle.load(f)
with open('map_videos.pickle', 'r') as f:
    map_videos = pickle.load(f)

for graph in glob.glob("./graph*.pickle"):
    G = read_pickle(graph)[0]
    H = nx.Graph()

    all_edges = []
    for edge in G.edges():
        src, dst = edge
        
        if len(src) == 11 and len(dst) == 24:
            video = src
            channel = dst
        elif len(src) == 24 and len(dst) == 11:
            video = dst
            channel = src
        else:
            print(src, dst)
            continue

        all_edges.append((map_channels[channel], map_videos[video]))
    H.add_edges_from(all_edges)
    nx.write_gpickle(H,"anonymized_graphs/" + graph)

        


