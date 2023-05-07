# Jumping Leprechauns

**Solve P-11.70 (page 534) - Using an AVL tree.**

Write a program that performs a simple n-body simulation, called “Jumping Leprechauns.” This simulation involves n leprechauns, numbered 1 to n. It maintains a gold value gi for each leprechaun i, which begins with each leprechaun starting out with a million dollars worth of gold, that is, gi = 1,000,000 for each i = 1, 2, . . . , n.

In addition, the simulation also maintains, for each leprechaun, i, a place on the horizon, which is represented as a double-precision floating-point number, xi. In each iteration of the simulation, the simulation processes the leprechauns in order from 1 to n. Initially, xi is calculated as xi = 1000000*r , where *r is a random floating-point number between −1 and 1*.

Processing a leprechaun i during this iteration begins by computing a new place on the horizon for i, which is determined by the assignment xi = xi + rgi , where r is a random floating-point number between −1 and 1. The leprechaun i then steals half the gold from the nearest leprechauns on either side of him on the horizon and adds this gold to his gold value, gi.

Write a program that can perform a series of iterations in this simulation for a given number, n, of leprechauns. You must maintain the set of horizon positions using an AVL tree data structure with the horizon positions as the key. Then you can use the before() and after() methods to look at the horizon positions. The corresponding value for the key-value pair of the AVL node could be an object that stores the leprechaun number and its gold value.

You do not need to write the AVL tree implementation. It is included in this repository.

Below is a Sample Output: 

```
Initial state of the leprechauns:
Horizon position: -0.5 | Gold value: 1000000
Horizon position: -0.2 | Gold value: 1000000
Horizon position: 0.1 | Gold value: 1000000
Horizon position: 0.4 | Gold value: 1000000
Horizon position: 0.8 | Gold value: 1000000

Iteration 1:
Horizon position: -1.2 | Gold value: 1500000
Horizon position: -0.4 | Gold value: 500000
Horizon position: 0.3 | Gold value: 500000
Horizon position: 1.2 | Gold value: 1500000
Horizon position: 1.6 | Gold value: 500000

Iteration 2:
Horizon position: -2.4 | Gold value: 1750000
Horizon position: -1.2 | Gold value: 750000
Horizon position: -0.1 | Gold value: 250000
Horizon position: 2.4 | Gold value: 1750000
Horizon position: 3.2 | Gold value: 750000

Iteration 3:
Horizon position: -3.6 | Gold value: 2125000
Horizon position: -2.4 | Gold value: 625000
Horizon position: -1.3 | Gold value: 125000
Horizon position: 3.6 | Gold value: 2125000
Horizon position: 5.6 | Gold value: 625000
```
