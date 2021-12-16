def DFSUtil(graph, temp, v, visited, weight, threshold):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in graph.neighbors(v):
            if (weight(v,i) != None) and (weight(v,i) >= threshold):
                if visited[i] == False:
                # Update the list
                    temp = DFSUtil(graph, temp, i, visited, weight, threshold)
        return temp
    
def cluster(graph,weight,threshold = 0):
    visited = {}
    cc = []
    for i in graph.nodes:
        visited[i] = False
    for v in graph.nodes:
        if visited[v] == False:
            temp = []
            cc.append(frozenset(DFSUtil(graph, temp, v, visited, weight, threshold)))
    return frozenset(cc)