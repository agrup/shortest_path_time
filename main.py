import networkx as nx
import random
import datetime
import csv
#config 
folder = "graph_gml/"
nodos = [10000,100000,100000]
probs = [1,0.5,0.2]

#functions

def graph_add_random_weight(G,ini=1,end=10):
    for o, d in G.edges():
        G[o][d]['weight'] = random.randint(ini,end)
    return G

def create_er_graph(nodos=[10,100,1000],probs=[1,0.3,0.1]):
    graphs_er=[]
    for cnt_nodos in nodos:
        for p in probs:
            graph = nx.erdos_renyi_graph(cnt_nodos,p)
            graph = graph_add_random_weight(graph)
            graphs_er.append(graph)
            nx.write_edgelist(graph,"{}erdos_renyi_nodos={}_prob={}.edges.gml".format(folder,str(cnt_nodos),str(p)))
            nx.write_gml(graph,"{}erdos_renyi_nodos={}_prob={}.nodes.gml".format(folder,str(cnt_nodos),str(p)))
    return graphs_er

def create_ba_graph(nodos=[50,100,1000],probs=[1,0.5]):
    graphs_ba=[]

    for cnt_nodos in nodos:
        for p in probs:
            if p == 1:    
                graph = nx.barabasi_albert_graph(cnt_nodos,int(cnt_nodos*p)-1)
            else:
                graph = nx.barabasi_albert_graph(cnt_nodos,int(cnt_nodos*p))
            #print("barabasi edges",int(cnt_nodos*p),cnt_nodos,p,"nodos",cnt_nodos)
            graph_add_random_weight(graph)
            graphs_ba.append(graph)
            nx.write_edgelist(graph,"{}barabasi_albert_nodos={}_probs={}.edges.gml".format(folder,str(cnt_nodos),str(p)))
            nx.write_gml(graph,"{}barabasi_albert_nodos={}_probs={}.nodes.gml".format(folder,str(cnt_nodos),str(p)))
    return graphs_ba


def get_floyd_washall_time(G,weight='weight'):
    begin = datetime.datetime.now()
    distance = nx.floyd_warshall(G,weight=weight)
    end=datetime.datetime.now()
    return(end-begin,distance)

def get_johnson_time(G,weight='weight'):
    begin = datetime.datetime.now()
    distance = nx.johnson(G,weight=weight)
    end=datetime.datetime.now()
    return(end-begin,distance)

er = create_er_graph()

with open('result.csv','w')as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow(('Tipo grafo','nodos','edges','tiempo floyd warshal' ,'tiempo johnson'))   

for graph in list(er):
    time_fw,dist = get_floyd_washall_time(graph)
    time_jo,dist = get_johnson_time(graph)
    with open('result.csv','a')as file:
        writer = csv.writer(file,delimiter=',')
        nodos = graph.number_of_nodes()
        edges = graph.number_of_edges()
        writer.writerow(('erdos renyi',str(nodos),str(edges),str(time_fw),str(time_jo)))
        

ba = create_ba_graph()

for graph in list(ba):
    time_fw,dist = get_floyd_washall_time(graph)
    time_jo,dist = get_johnson_time(graph)
    with open('result.csv','a')as file:
        writer = csv.writer(file,delimiter=',')
        nodos = graph.number_of_nodes()
        edges = graph.number_of_edges()
        writer.writerow(["barabasi",str(nodos),str(edges),str(time_fw),str(time_jo)])



