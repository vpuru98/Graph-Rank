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

<i>Note: An extra correction term is further added to the above formula for dealing with the sink nodes of a graph. </i>

### The Random Surfer 
One way to get a rough understanding of the rank values computed by Graph-Rank is to think about a random surfer who travels throughout a graph by making random decisions. 
Every time the random surfer arrives at a node of the graph, it randomly chooses an outgoing edge of this node to move to a different node of the graph. 
The rank value for a node of the graph would then be the probability of finding the radom surfer at this node, at a particular moment in time. 
The random surfer is more likely to spend time on a node of the graph which is has better connectivity, and also has a lot of traffic flowing through it.

## Use Cases

### The Celebrity problem
Graph-Rank is applied to solve the trivial problem of identifying the most popular person invited to a party.

### Station Ranking
Graph-Rank is used to solve the problem of finding the busiest railway stations of India. The railway network for this problem consisted of over <b>8000</b> stations and over <b>10000</b> trains. The results are summarized below.


    1.  HOWRAH JN : 0.0032299914
    2.  NEW DELHI : 0.0019528751
    3.  SEALDAH : 0.0019370082
    4.  THANE : 0.0018996189
    5.  DELHI : 0.0018904029
    6.  VIJAYAWADA JN : 0.001728963
    7.  AHMEDABAD JN : 0.001698128
    8.  KANPUR CENTRAL : 0.0016731561
    9.  H NIZAMUDDIN : 0.0016620263
    10. LUCKNOW NR : 0.0016309597
    11. C SHIVAJI MAH T : 0.0015898468
    12. KALYAN JN : 0.0015394498
    13. PUNE JN : 0.0015036637
    14. GORAKHPUR JN : 0.001480323
    15. BORIVALI : 0.0014553636
    16. AMBALA CANT JN : 0.0014540411
    17. PATNA JN : 0.001433949
    18. BARDDHAMAN JN : 0.0014216573
    19. VISAKHAPATNAM : 0.0014024297
    20. VARANASI JN : 0.0013835786


The datasets used for solving this problem are credited to [Ayush Dubey](https://github.com/ayushdubey003/) 
