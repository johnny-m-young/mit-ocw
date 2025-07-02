# Answers to problem set 1

## Problem 1

###

$(a)$ $\exists x\in X,\: S(x)\land A(x)$

###

$(b)$ $\forall x\in X,\: TA(x)\land S(x)\implies A(x)$

###

$(c)$ $\nexists x\in X,\: TA(x)\land \neg A(x)$ **CHECK THIS?**

###

$(d)$ $\sum_{x=0}^X TA(x)\land \neg S(x) \geq 3$

$\exists x\in X,\: TA(x)\land \neg S(x)$ **NEED TO FINISH THIS ONE**

## Problem 2

### $(a)$

For the left side of the equation the truth table is as follows:

| $P$ | $Q$ | $R$ | $Q\land R$ | $(P\lor (Q\land R))$ | $\neg (P\lor (Q\land R))$ |
| --- | --- | --- | ---------- | -------------------- | ------------------------- |
| $T$ | $T$ | $T$ | $T$        | $T$                  | $F$                       |
| $T$ | $T$ | $F$ | $F$        | $T$                  | $F$                       |
| $T$ | $F$ | $T$ | $F$        | $T$                  | $F$                       |
| $T$ | $F$ | $F$ | $F$        | $T$                  | $F$                       |
| $F$ | $T$ | $T$ | $T$        | $T$                  | $F$                       |
| $F$ | $T$ | $F$ | $F$        | $F$                  | $T$                       |
| $F$ | $F$ | $T$ | $F$        | $F$                  | $T$                       |
| $F$ | $F$ | $F$ | $F$        | $F$                  | $T$                       |

And for the right side of the equation:

| $P$ | $Q$ | $R$ | $(\neg P)$ | $\neg Q\lor \neg R$ | $(\neg P) \land (\neg Q\lor \neg R)$ |
| --- | --- | --- | ---------- | ------------------- | ------------------------------------ |
| $T$ | $T$ | $T$ | $F$        | $F$                 | $F$                                  |
| $T$ | $T$ | $F$ | $F$        | $T$                 | $F$                                  |
| $T$ | $F$ | $T$ | $F$        | $T$                 | $F$                                  |
| $T$ | $F$ | $F$ | $F$        | $T$                 | $F$                                  |
| $F$ | $T$ | $T$ | $T$        | $F$                 | $F$                                  |
| $F$ | $T$ | $F$ | $T$        | $T$                 | $T$                                  |
| $F$ | $F$ | $T$ | $T$        | $T$                 | $T$                                  |
| $F$ | $F$ | $F$ | $T$        | $T$                 | $T$                                  |

Both sides evaluate to the same thing, for the same values of $P$, $Q$ and $R$. Therefore, the truth table for this whole equation looks like this:

| $P$ | $Q$ | $R$ | $\neg (P\lor (Q\land R)) = (\neg P)\land (\neg Q\lor \neg R)$ |
| --- | --- | --- | ------------------------------------------------------------- |
| $T$ | $T$ | $T$ | $T$                                                           |
| $T$ | $T$ | $F$ | $T$                                                           |
| $T$ | $F$ | $T$ | $T$                                                           |
| $T$ | $F$ | $F$ | $T$                                                           |
| $F$ | $T$ | $T$ | $T$                                                           |
| $F$ | $T$ | $F$ | $T$                                                           |
| $F$ | $F$ | $T$ | $T$                                                           |
| $F$ | $F$ | $F$ | $T$                                                           |

### $(b)$

For the left side of the equation the truth table is as follows:

| $P$ | $Q$ | $R$ | $Q\lor R$ | $(P\land (Q\lor R))$ | $\neg (P\land (Q\lor R))$ |
| --- | --- | --- | --------- | -------------------- | ------------------------- |
| $T$ | $T$ | $T$ | $T$       | $T$                  | $F$                       |
| $T$ | $T$ | $F$ | $T$       | $T$                  | $F$                       |
| $T$ | $F$ | $T$ | $T$       | $T$                  | $F$                       |
| $T$ | $F$ | $F$ | $F$       | $F$                  | $T$                       |
| $F$ | $T$ | $T$ | $T$       | $F$                  | $T$                       |
| $F$ | $T$ | $F$ | $T$       | $F$                  | $T$                       |
| $F$ | $F$ | $T$ | $T$       | $F$                  | $T$                       |
| $F$ | $F$ | $F$ | $F$       | $F$                  | $T$                       |

And for the right side of the equation:

| $P$ | $Q$ | $R$ | $\neg P$ | $\neg Q\lor \neg R$ | $\neg P\lor (\neg Q\lor \neg R)$ |
| --- | --- | --- | -------- | ------------------- | -------------------------------- |
| $T$ | $T$ | $T$ | $F$      | $F$                 | $F$                              |
| $T$ | $T$ | $F$ | $F$      | $T$                 | $T$                              |
| $T$ | $F$ | $T$ | $F$      | $T$                 | $T$                              |
| $T$ | $F$ | $F$ | $F$      | $T$                 | $T$                              |
| $F$ | $T$ | $T$ | $T$      | $F$                 | $T$                              |
| $F$ | $T$ | $F$ | $T$      | $T$                 | $T$                              |
| $F$ | $F$ | $T$ | $T$      | $T$                 | $T$                              |
| $F$ | $F$ | $F$ | $T$      | $T$                 | $T$                              |

So truth table for this whole equation looks like this:

| $P$ | $Q$ | $R$ | $\neg (P\land (Q\lor R)) = \neg P \lor (\neg Q\lor \neg R)$ |
| --- | --- | --- | ----------------------------------------------------------- |
| $T$ | $T$ | $T$ | $T$                                                         |
| $T$ | $T$ | $F$ | $F$                                                         |
| $T$ | $F$ | $T$ | $F$                                                         |
| $T$ | $F$ | $F$ | $T$                                                         |
| $F$ | $T$ | $T$ | $T$                                                         |
| $F$ | $T$ | $F$ | $T$                                                         |
| $F$ | $F$ | $T$ | $T$                                                         |
| $F$ | $F$ | $F$ | $T$                                                         |

## Problem 3

There are different ways of representing the $nand$ logical operator<sup>[[1]](https://oeis.org/wiki/Logical_NAND)</sup>. For this problem set I'm going the use the $\uparrow$ notation.

### $(a)$

$(i)$ A $nand$ truth table is just the negation of an $and$ truth table so $A\land B$ can be represented as $\neg (A\uparrow B)$

$(ii)$ For this one, we need to turn the $nand$ truth table on its head (i.e. read TTTF rather than FTTT from top to bottom)
To achieve this we can negate both $A$ and $B$ to give $\neg A\uparrow \neg B$

$(iii)$ This one was a bit more tricky to figure out. It helped me to write out the truth table for $A\implies B$ and compare with $A\uparrow B$:

| $A$ | $B$ | $A\implies B$ | $A\uparrow B$ |
| --- | --- | ------------- | ------------- |
| T   | T   | T             | F             |
| T   | F   | F             | T             |
| F   | T   | T             | T             |
| F   | F   | T             | T             |

What I noticed is that the bottom half of the truth tables are the same. Another thing I observed is that the top half are the negations of each other. $A$ is True in both of these top entries, so I felt like the answer had to lie in manipulating $B$. Furthermore, as $A\implies B$ is always true for $A = False$ I knew I could manipulate $B$ to alter the top two entries of the truth table, without changing the bottom. By negating $B$ we can achieve the desired result.

Therefore the answer is $A\implies \neg B$

### $(b)$

If we set P and Q both equal to A in the $nand$ truth table we get

| $A$ | $A$ | $A\uparrow A$ |
| --- | --- | ------------- |
| T   | T   | F             |
| F   | F   | T             |

Therefore $(\neg A) = A\uparrow A$

### $(c)$

| $P$ | $Q$ | $P\uparrow Q$ |
| --- | --- | ------------- |
| T   | T   | F             |
| T   | F   | T             |
| F   | T   | T             |
| F   | F   | T             |

From the $nand$ truth table, we can see that there are two possible ways of $P\uparrow Q$ being True. Either $P$ and $Q$ are opposites, or they are both False. In part $(b)$ we showed that $(\neg A) = A\uparrow A$. If we therefore set $P = A$ and $Q = A\uparrow A$, we get get the following truth table:

| $A$ | $A\uparrow A$ | $A\uparrow (A\uparrow A)$ |
| --- | ------------- | ------------------------- |
| T   | F             | T                         |
| F   | T             | T                         |

The only way $nand$ is False is if both $P$ and $Q$ are True. We've just shown an expression which always evaluates to True, so we can just use that for both $P$ and $Q$ to get a comparison which always evaluates to False:

$(A\uparrow (A\uparrow A))\uparrow (A\uparrow (A\uparrow A))$ is always False.

## Problem 4

### Weighing #1

Split the coins into two piles of 6 coins and weigh them against each other. This would reveal in which pile the fake coin is - which ever pile is the lighter.

### Weighing #2

Split the coins from the lighter pile into two piles of 3 coins and weigh them against each other. Again, we know the fake coin is in the lighter pile.

### Weighing #3

Pick two random coins from our pile of 3 and weigh them against each other. If they are the same weight, the fake one is the one we did not pick. Otherwise, the fake coin is the lighter of the two.

### NOTE

You could have done this by first splitting the 12 coins into three piles of 4 coins and picked two piles at random to weigh against each other. Using the same deduction as above: if they weigh the same, the fake coin is in the pile you did not pick. Otherwise the fake coin is in the lighter pile. This gets us to the same result but just uses the three-way technique earlier in the game. You could have also done it by using this technique in round 2 instead of rounds 1 or 3.

## Problem 5

## Problem 6
