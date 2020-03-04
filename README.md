# Graph-Rank
> Implemention of Google's PageRank algorithm with different use cases.


## About
PageRank is an algorithm which was developed by Google for ranking web pages accross the Internet. It is essentially a link analysis algorithm which attempts to assign rank values to a set of hyperlinked documents, based on their relative importance.
With Graph-Rank, we model the concept of PageRank to work on any directed weighted multigraph, such that it can rank nodes of graphs according to their relative importance, depending on the amount of traffic flowing through them. 
Specifically, Graph-Rank computes the value <b>R</b> for each node of the graph


`
  R(u) = (1 - D) / N + D * Σ (R(v) * W(v, u) / S(v))
`

where <b>N</b> is the number of nodes within the graph, <b>W(v, u)</b> is the weight associated with an edge from v to u, <b>S(v)</b> is the sum of the weights of all outgoing edges from v, and <b>D</b> is a number between 0 and 1.

### The Random Surfer 
One way to get a rough understanding of the rank values computed by Graph-Rank is to think about a random surfer who travels throughout a graph by making random decisions. 
Every time the random surfer arrives at a node of the graph, it randomly chooses an outgoing edge of this node to move to a different node of the graph. 
The rank value for a node of the graph would then be the probability of finding the radom surfer at this node, at a particular moment in time. 

The random surfer is more likely to spend time on a node of a graph which is has better connectivity, and also has a lot of traffic flowing through it.

## Use Cases

### The Celebrity problem
Graph-Rank is applied to solve the trivial problem of identifying the most popular person invited to a party.

### Station Ranking
Graph-Rank is used to solve the problem of finding the busiest railway stations of India. The railway network for this problem consisted of over <b>8000</b> stations and over <b>10000</b> trains. 
