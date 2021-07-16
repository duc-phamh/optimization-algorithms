# Tabu search:

Algorithm description: https://en.wikipedia.org/wiki/Tabu_search

---

**Problem:** Implement local search algorithm for the Balanced Partition problem. The algorithm should be designed in such a way that it stops at finding the locally optimal solution.

The dataset is provided via stdin in col format. The output format is a single line with space-separated ids of the vertices from any of the two parts of the partition.


---


Sample Input:
```
c FILE: myciel3.col
c SOURCE: Michael Trick (trick@cmu.edu)
c DESCRIPTION: Graph based on Mycielski transformation. 
c              Triangle free (clique number 2) but increasing
c              coloring number
p edge 11 20
e 1 2
e 1 4
e 1 7
e 1 9
e 2 3
e 2 6
e 2 8
e 3 5
e 3 7
e 3 10
e 4 5
e 4 6
e 4 10
e 5 8
e 5 9
e 6 11
e 7 11
e 8 11
e 9 11
e 10 11
```
Sample Output:
```
9 8 5 2 1
```
