from collections import deque

def BFS(graph, label, status, node):
    # default
    wait = deque([node])
    status[node] = 'wait'
    label[node] = 'good'
    while wait: # not yet visited
        left = wait.popleft()
        for right in graph.neighbors(left):
            if status[right] == 'N':
                status[right] = 'wait'
                if label[left] == 'good':
                    label[right] = 'evil'
                else:
                    label[right] = 'good'
                wait.append(right)
            elif label[right] == label[left]:
                return False
        status[left] = 'visited'
    return True


def assign_good_and_evil(graph):
    stat = {node: 'N' for node in graph.nodes}
    lable = {}
    for node in graph.nodes:
        if stat[node] == 'N':
            result = BFS(graph, lable, stat, node)
            if result is False:
                return None
    return lable
