import networkx as nx
import random
import datetime
import csv

#config 
folder = 'graph_gml/'
csv_file =''
nodos = [10**3,10**4,10**5]
probs = [1,0.5,0.2]

#functions

def graph_add_random_weight(G,ini=1,end=10):
    for o, d in G.edges():
        G[o][d]['weight'] = random.randint(ini,end)
    return G

def create_er_graph(nodos=[10,100,1000],edges=[10,100,1000]):
    graphs_er=[]
    for cnt_nodos in nodos:
        for cnt_edges in edges:
            graph = nx.gnm_random_graph(cnt_nodos,cnt_edges)
            graph = graph_add_random_weight(graph)
            graphs_er.append(graph)
            print("erdos_renyi_nodos={}_prob={}.edges.gml".format(str(cnt_nodos),str(cnt_edges)))
    return graphs_er

def create_ba_graph(nodos=[50,100,1000],probs=[1,0.5]):
    graphs_ba=[]

    for cnt_nodos in nodos:
        for p in probs:
            if p == 1:    
                graph = nx.barabasi_albert_graph(cnt_nodos,int(cnt_nodos*p)-1)
            else:
                graph = nx.barabasi_albert_graph(cnt_nodos,int(cnt_nodos*p))
            graph_add_random_weight(graph)
            graphs_ba.append(graph)
            print("barabasi_albert_nodos={}_probs={}".format(str(cnt_nodos),str(p)))
    return graphs_ba


def get_floyd_washall_time(G,weight='weight'):
    begin = datetime.datetime.now()
    _distance = nx.floyd_warshall(G,weight=weight)
    end=datetime.datetime.now()
    return(end-begin)

def get_johnson_time(G,weight='weight'):
    begin = datetime.datetime.now()
    _distance = nx.johnson(G,weight=weight)
    end=datetime.datetime.now()
    return(end-begin)


def save_results(G,model,time_fw,time_jo):
    with open('result.csv','a')as file:
            writer = csv.writer(file,delimiter=',')
            nodos = G.number_of_nodes()
            edges = G.number_of_edges()
            writer.writerow(('erdos renyi',str(nodos),str(edges),str(time_fw),str(time_jo)))

with open('result.csv','w')as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow(('Tipo grafo','nodos','edges','tiempo floyd warshal' ,'tiempo johnson'))   


#grafo prueba
nodos=10
edges=[nodos*nodos,nodos,nodos/2]

er = create_er_graph(nodos=[nodos],edges=edges)
print("er created")
time_fw = get_floyd_washall_time(er[0])
time_jo = get_johnson_time(er[0])
save_results(er[0],"erdos renyi",time_fw,time_jo)

time_fw = get_floyd_washall_time(er[1])
time_jo = get_johnson_time(er[1])
save_results(er[1],"erdos renyi",time_fw,time_jo)

time_fw = get_floyd_washall_time(er[2])
time_jo = get_johnson_time(er[2])
save_results(er[1],"erdos renyi",time_fw,time_jo)

ba = create_ba_graph(nodos=[nodos])
print("ba created")
time_fw = get_floyd_washall_time(ba[0])
time_jo = get_johnson_time(ba[0])
save_results(ba[0],"barabasi albert",time_fw,time_jo)

time_fw = get_floyd_washall_time(ba[1])
time_jo = get_johnson_time(ba[1])
save_results(ba[1],"barabasi albert",time_fw,time_jo)

# creo los grafos con 1000 nodos
nodos=10**3
edges=[nodos*nodos,nodos,nodos/2]

er = create_er_graph(nodos=[nodos],edges=edges)
print("er created")
time_fw = get_floyd_washall_time(er[0])
time_jo = get_johnson_time(er[0])
save_results(er[0],"erdos renyi",time_fw,time_jo)

time_fw = get_floyd_washall_time(er[1])
time_jo = get_johnson_time(er[1])
save_results(er[1],"erdos renyi",time_fw,time_jo)

time_fw = get_floyd_washall_time(er[2])
time_jo = get_johnson_time(er[2])
save_results(er[2],"erdos renyi",time_fw,time_jo)

ba = create_ba_graph(nodos=[nodos])
print("ba created")
time_fw = get_floyd_washall_time(ba[0])
time_jo = get_johnson_time(ba[0])
save_results(ba[0],"barabasi albert",time_fw,time_jo)

time_fw = get_floyd_washall_time(ba[1])
time_jo = get_johnson_time(ba[1])
save_results(ba[1],"barabasi albert",time_fw,time_jo)

# creo los grafos con 10000 nodos
nodos=10**4
edges=[nodos*nodos,nodos,nodos/2]

er = create_er_graph(nodos=[nodos],edges=edges)
print("er created")
time_fw = get_floyd_washall_time(er[0])
time_jo = get_johnson_time(er[0])
save_results(er[0],"erdos renyi",time_fw,time_jo)

time_fw = get_floyd_washall_time(er[1])
time_jo = get_johnson_time(er[1])
save_results(er[1],"erdos renyi",time_fw,time_jo)

time_fw = get_floyd_washall_time(er[2])
time_jo = get_johnson_time(er[2])
save_results(er[2],"erdos renyi",time_fw,time_jo)


ba = create_ba_graph(nodos=[nodos],)
print("ba created")
time_fw = get_floyd_washall_time(ba[0])
time_jo = get_johnson_time(ba[0])
save_results(ba[0],"barabasi albert",time_fw,time_jo)

time_fw = get_floyd_washall_time(ba[1])
time_jo = get_johnson_time(ba[1])
save_results(ba[1],"barabasi albert",time_fw,time_jo)


# creo los grafos con 100000 nodos
nodos=10**5
edges=[nodos*nodos,nodos,nodos/2]

er = create_er_graph(nodos=[nodos],edges=edges)
print("er created")
time_fw = get_floyd_washall_time(er[0])
time_jo = get_johnson_time(er[0])
save_results(er[0],"erdos renyi",time_fw,time_jo)

time_fw = get_floyd_washall_time(er[1])
time_jo = get_johnson_time(er[1])
save_results(er[1],"erdos renyi",time_fw,time_jo)

time_fw = get_floyd_washall_time(er[2])
time_jo = get_johnson_time(er[2])
save_results(er[2],"erdos renyi",time_fw,time_jo)



ba = create_ba_graph(nodos=[nodos])
print("ba created")
time_fw = get_floyd_washall_time(ba[0])
time_jo = get_johnson_time(ba[0])
save_results(ba[0],"barabasi albert",time_fw,time_jo)

time_fw = get_floyd_washall_time(ba[1])
time_jo = get_johnson_time(ba[1])
save_results(ba[1],"barabasi albert",time_fw,time_jo)

# for graph in list(er):
#     time_fw,dist = get_floyd_washall_time(graph)
#     time_jo,dist = get_johnson_time(graph)
#     with open('result.csv','a')as file:
#         writer = csv.writer(file,delimiter=',')
#         nodos = graph.number_of_nodes()
#         edges = graph.number_of_edges()
#         writer.writerow(('erdos renyi',str(nodos),str(edges),str(time_fw),str(time_jo)))
        

# ba = create_ba_graph(nodos=[10**3])
# print("ba created")
# for graph in list(ba):
#     time_fw,dist = get_floyd_washall_time(graph)
#     time_jo,dist = get_johnson_time(graph)
#     with open('result.csv','a')as file:
#         writer = csv.writer(file,delimiter=',')
#         nodos = graph.number_of_nodes()
#         edges = graph.number_of_edges()
#         writer.writerow(["barabasi",str(nodos),str(edges),str(time_fw),str(time_jo)])

# er = create_er_graph(nodos=[10**3])
# print("er created")

