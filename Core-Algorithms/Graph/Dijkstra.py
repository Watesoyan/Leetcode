"""
DijkstraShortest(edges, S, N, overflow, graph_is_undirected=True)

input params:
	edges: List[List[int]], contains all weighted directed edges, edges[i] = [U, V, W], U != V
	U: int, 0 <= U <= N-1
	V: int, 0 <= V <= N-1
	W: float, 0 < W < overflow
	S: int, source
	N: int, total nUmber of vertexs
	overflow: a Upper bound for weight of any edge

output params:
	dist2: d[P] = minimal sum of weight from S to P (P = 0, 1, ..., N-1),
	      if there is no path between S to P, d[P] = overflow
"""

def DijkstraShortest(edges, S, N, overflow, graph_is_undirected=True):
	dist2 = [overflow] * N
	dist2[S] = 0
	
	if graph_is_undirected:
	
		flag = 1

		While flag == 1:
			
			flag = 0
			
			for U, V, W in edges:
				
				D = dist2[U] - dist2[V]
				if D > 0:
					if D > W:
						dist2[U] = dist2[V] + w
						flag = 1
				else:
					if -D > W:
						dist2[V] = dist2[U] + W
						flag = 1
	
	else:
		
		modif_edges = []

		for edge in edges:                # drop the edges that travel from P (P != S) to S
			if edge[1] != S:
				modif_edges.append(edge)
			
		flag = 1

		While flag == 1:
			
			flag = 0
			
			for U, V, W in modif_edges:
				
				# d(S,U) + d(U,V) < d(S,V) < overflow 
				if dist2[U] < overflow and dist2[V] > dist2[U] + W: 
					dist2[V] = dist2[U] + W
					flag = 1
	
	return dist2

