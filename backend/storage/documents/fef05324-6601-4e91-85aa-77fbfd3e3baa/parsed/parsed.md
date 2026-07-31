## Problem Reduction

- So  far  we  have  considered  search  strategies  for  OR graph.
- In OR graph, several arcs indicate a variety of ways in which the original problem may be solved.
- Another  kind  of  structure  AND-OR  graph  (tree)  is useful for representing the solution of problems by decomposing  them  into  smaller  problems,  all  of  which must then be solved.
- This  decomposition  generates  arcs  that  we  will  call AND  arc.    One  AND  arc  may  point  to  any  number  of successors, all of which must be solved.
- The proposed structure is called AND-OR graph rather than simply AND graph.
- To  find  a  solution  in  AND-OR  graph,  we  need  an algorithm  similar  to  A*  but  with  the  ability  to  handle AND arc appropriately.
- In search for AND-OR graph also, we will use the value of heuristic function f for each node.
- Example of AND-OR tree:

<!-- image -->

## AND OR graph Search

- Traverse the graph, starting at the initial node and follow the current best path and accumulate the set of nodes that are on that (best) path which have not yet been expanded.
- Pick up one of these unexpanded nodes and expand it.
- Add its successors to the graph and compute f for each of them.
- Change the f estimate of newly expanded node to reflect the new information provided by its successors.
- Propagate  this  change  backward  through  the  graph  to the start.
- Mark  the  best  path  which  could  be  different  from the current best path.
- Propagation of revised cost estimates back up the tree. (This propagation was not there in A*)
- In  the  following  example,  let  us  assume  that  each  arc with single successor will have a cost of 1 and each AND arc with multiple successor will have a cost of 1 for each of its components for the sake of simplicity.
- Consider  the  following  AND-OR  graph.  Numbers  in the brackets are estimated cost.
- Initially we start from start node A and compute heuristic values for each of its successors, say {B, (C &amp; D)} as {11, 9}.
- We  see  that  path  from  (C  &amp;  D)  seems  to  be  better. Compute heuristic values of C and D as 9 and 27 respectively. Now the cost of path from A through (C &amp; D) is 38 which no longer is good path.
- Expand  path  from  A  to  B.  After  expansion  we  see  that heuristic value of this path comes out to be 18. This path is still best path so far. So further explore path from A to B ….
- The process continues until either a solution is found or all paths  have  lead  to  dead  ends,  indicating  that  there  is  no solution.

<!-- image -->

## The  "Solve" labeling Procedure

- A terminal node is labeled "solved" if it is a goal node (representing a solution of sub-problem) otherwise label it "unsolved"  (representing  a  sub-problem  that  can  not  be reduced any further).
- A non-terminal AND  node  labeled  "unsolvable"  as soon as one of its successors is labeled "unsolvable".  It is labeled "solved" if all of its successors are "solved".
- A non-terminal OR node is labeled "solved" as soon as one  of  its  successors  is  labeled  "solved".    It  is  labeled "unsolved" if all its successors are "unsolvable".

Example: Consider the following example

1. After one cycle

<!-- image -->

## 3 . A ft e r   t h r e e   c y c le

<!-- image -->

## 4 . A ft e r   fo u r   c y c le

<!-- image -->

## Remarks:

- In  first  cycle,  we  expanded  A,  second cycle  B,  third  cycle  C  and  in  fourth  cycle D.  After D is expended, node A gets label SOLVED.
- The  solution  graph  with  minimal  cost equal  to  5  is  obtained  by  tracing  down through the marked arrows.

## Example

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Date

Page

<!-- image -->

<!-- image -->

<!-- image -->

f(n)-g(n)th(n)

Path-1: f(S-C)= 1+13-14

Path-2: f(S-A-B)=1+1+7+12-21

f(C-F-G)=1+1+5+7-14

f(S-C)=1+14-15 (revised)

<!-- image -->

<!-- image -->

Path  -1: f(A-B-C)= 1+1+3+4= 9

f(B-E)=1+5-6

f(A-B-C)= 1+1+6+4= 12

f(D-G-H)= 1+l+4+4 =10 f(A-C-D)= 1+1+4+10= 16

## EXAMPLE 2

<!-- image -->

## EXAMPLE 2 ..CONTD.

<!-- image -->

## EXAMPLE 2 ..CONTD.

<!-- image -->

## EXAMPLE 2 ..CONTD.

<!-- image -->