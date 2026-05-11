# Answers to problem set 2

## Problem 1

For this problem, we're going to prove that any sequence of 5 numbers - $a_1, a_2, a_3, a_4, a_5$ - will contain a _3-chain_ (a subsequence $a, b, c$ where either $a < b < c$ or $a > b > c$)

### $(a)$

Assuming $a_1 < a_2$ and there is no _3-chain_ means $a_2 > a_3$, otherwise $a_1 < a_2 < a_3$ forms a _3-chain_.

$a_1 < a_2 > a_3$

This means $a_3 < a_4$, otherwise $a_2 > a_3 > a_4$ forms a _3-chain_.

$a_1 < a_2 > a_3 < a_4$

$a_3$ must be less than $a_1$, otherwise you could form a _3-chain_ by deleting $a_2$ from the sequence, giving you $a_1 < a_3 < a_4$.

### $(b)$

From $(a)$

$a_1 < a_2 > a_3 < a_4$ where $a1 > a_3$

$a_4$ must be less than $a_2$ otherwise you could form a _3-chain_ by deleting $a_3$ from the sequence, giving you $a_1 < a_2 < a_4$. As $a_3 < a_4$ this means $a_3 < a_4 < a_2$

### $(c)$

Assuming, from the previous questions, $a_1 < a_2 > a_3 < a_4$ where $a_3 < a_1 < a_2$ and $a_3 < a_4 < a_2$.

If we set $a_4 < a_5$ that immediately forms a _3-chain_ in $a_3 < a_4 < a_5$.

Let us then consider the case where $a_4 > a_5$.

$a_1 < a_2 > a_3 < a_4 > a_5$ where $a_3 < a_1 < a_2$ and $a_3 < a_4 < a_2$

Deleting $a_1$ and $a_3$ forms a _3-chain_ because $a_2 > a_4 > a_5$. Therefore, the sequence $a_1\: a_2\: a_3\: a_4\: a_5$ where $a_1 < a_2$ and $a_3 < a_4 < a_2$ will always contain a _3-chain_ for any value of $a_5$.

### $(d)$ INCOMPLETE

Proof by contradiction

Assume for the the purpose of contradiction that any sequence of five distinct integers, $a_1\: a_2\: a_3\: a_4\: a_5$, does not contain a _3-chain_.

## Problem 2

### Proof by induction

#### Base case - $P(0)$

$\sum_{i=0}^0 i^3 = \Big( \frac{0(0+1)}{2} \Big)^2$

$0 = 0$ ✅

#### Inductive step - $P(n)\implies P(n+1)$

Assume $P(n)$ is true

$P(n) = \sum_{i=0}^n i^3 = \Big(\frac{n(n+1)}{2} \Big)^2 = \Big(\frac{n^2+n}{2} \Big)^2 = \frac{n^4+2n^3+n^2}{4}$

Then prove $P(n+1) = P(n) +(n+1)^3$

$P(n+1) = \Big(\frac{(n+1)(n+2)}{2} \Big)^2 = \Big(\frac{n^2+3n+2}{2} \Big)^2 = \frac{n^4+6n^3+13n^2+12n+4}{4}$

We can now use $P(n) = \frac{n^4+2n^3+n^2}{4}$:

$P(n+1) = \frac{n^4+6n^3+13n^2+12n+4}{4} = \frac{n^4+2n^3+n^2}{4} + \frac{4n^3+12n^2+12n+4}{4} = P(n) + \frac{4n^3+12n^2+12n+4}{4}$

$ = P(n) + (n^3 + 3n^2 + 3n + 1) = P(n) + (n+1)^3$ ✅

## Problem 3

This was a tricky one and I had to get ChatGPT to play maths tutor with me to solve it. It eventually gave me the one word hint when I asked for it: **Perimeter**

I can define the perimeter as:

- the number of edges between infected and uninfected students, plus
- the number of edges between infected students and the grid boundary

Each infected student can contribute to **at most** 4 units of the perimeter if they are all isolated like in the example below. In this example the perimeter is 12.

| x   | -   | -   | x   |
| --- | --- | --- | --- |
| -   | -   | -   | -   |
| -   | x   | -   | -   |
| -   | -   | -   | -   |

If infected students are in contact with each other, like below, this reduces the perimeter as the sides in contact do not contribute. In this example the perimeter is 10.

| x   | -   | -   | -   |
| --- | --- | --- | --- |
| -   | x   | -   | -   |
| -   | x   | -   | -   |
| -   | -   | -   | -   |

This means the initial perimeter can be expressed as $P_0\leq 4i$ where $i$ is the number of infected students. Furthermore, we know that in order for an uninfected student to become infected, it must be in contact with 2 or more infected students.

In the case where there are exactly 2 infected students in contact with an uninfected student, the perimeter is preserved between timesteps because 2 of the newly infected student's sides are in contact with infected students - reducing the perimeter by 2 - but 2 sides are exposed to either the boundary or an uninfected student - increasing the perimeter by 2.

This is not the case when an uninfected student is in contact with 3 or 4 infected students. In this case, the perimeter reduces. In fact we can generalise how the perimeter changes from one timestep to the next by the equation $P_{t+1}=P_t-4n_4-2n_3$ where $n_4$ denotes the number of uninfected students in contact with exactly 4 infected students and $n_3$ denotes the number of uninfected students in contact with exactly 3 infected students.

This means the perimeter can never expand, so at any timestep the perimeter can be expressed as $P_t\leq 4i$. In a fully infected class, the perimeter would be $4n$. Therefore if $i<n$ then $4i < 4n$ and hence $P_t < 4n$ so the whole class can never be infected.

**If fewer than $n$ students in class are initially infected, the whole class will never be completely infected ✅**

## Problem 4

The problem here is in the inductive step. The professor correctly refactors $a^{n+1}$ to $\frac{a^n\cdot a^n}{a^{n-1}}$ but then incorrectly substitutes $n$. He says $\frac{a^n\cdot a^n}{a^{n-1}} = \frac{1\cdot 1}{1}$ by substituting $n=0$ but this is incorrect. If we substitute $n=0$ we get $\frac{a^n\cdot a^n}{a^{n-1}} = \frac{a^0\cdot a^0}{a^{-1}} = \frac{1\cdot 1}{a^{-1}} = a$.

## Problem 5

$G_{0}=0$, $G_{1}=1$ and $G_{n}=5G_{n-1}-6G_{n-2}$ for all $n \in \N, n \geq 2$

Prove $G_{n}=3^n-2^n$ for all $n \in \N$

### Prove base cases:

$G_0 = 3^0 - 2^0 = 1 - 1 = 0$ ✅

$G_1 = 3^1 - 2^1 = 3 - 2 = 1$ ✅

### Prove that $5G_{n-1} - 6G_{n-2} = 3^n - 2^n$ for $n \in \N, n \geq 2$:

I'll prove this by strong induction. Assuming $G_i = 3^i - 2^i$ for all $n \in \N, i < n$

Therefore, $G_{n-1} = 3^{n-1} - 2^{n-1}$ and $G_{n-2} = 3^{n-2} - 2^{n-2}$

$G_n = 5G_{n-1} - 6G_{n-2} = 5\cdot (3^{n-1} - 2^{n-1}) - 6\cdot (3^{n-2} - 2^{n-2})$

$=(5\cdot 3^{n-1} - 6\cdot 3^{n-2}) + (6\cdot 2^{n-2} - 5\cdot 2^{n-1})$

$=3^{n-2}\cdot (5\cdot 3 - 6) + 2^{n-2}\cdot (6 - 5\cdot 2)$

$=9\cdot 3^{n-2} - 4\cdot 2^{n-2}$

$=3^2\cdot 3^{n-2} - 2^2\cdot 2^{n-2}$

$=3^n - 2^n$ ✅

## Problem 6

Relative positions:

| 1   | 2   | 3   | 4   |
| --- | --- | --- | --- |
| 5   | 6   | 7   | 8   |
| 9   | 10  | 11  | 12  |
| 13  | 14  | 15  | 16  |

There are two types of move possible: a row move and a column move.

### Part A

#### Lemma 1

A row move does not change the order of the letters.

##### Proof

In a row move, we move a letter from cell $i$ into an adjacent cell ($i\pm 1$). Nothing else moves, hence the order of the items is preserved.

### Part B

#### Lemma 2

A column move changes the relative order of precisely 3 pairs of letters.

##### Proof

In a column move, we move a letter from cell $i$ to a blank space in cell $i\pm 4$. When an item moves 4 positions, it changes relative order with 3 other letters - $i\pm 1$, $i\pm 2$ and $i\pm 3$.

### Part C

#### Lemma 3

The parity of the number of inverted pairs stays the same in a row move.

##### Proof

By Lemma 1, the relative order of letters does not change in a row move. Therefore, the number of inverted pairs must stay the same and hence the parity will remain the same.

### Part D

### Lemma 4

The number of inverted pairs can only increase by 3, decrease by 3 or stay the same.

#### Proof

In a row move, the number of inverted pairs stays the same (by Lemma 1).

In a column move, 3 pairs of letters change relative order (by Lemma 2).

- All pairs were in correct order: number of inversions increases by 3.
- 1 inverted pair present:
- 2 inverted pairs present:
- 3 inverted pairs present:

| A   | B   | C   | E   |
| --- | --- | --- | --- |
| D   | -   | F   | G   |
| H   | I   | J   | K   |
| L   | M   | N   | O   |

| A   | -   | C   | E   |
| --- | --- | --- | --- |
| D   | B   | F   | G   |
| H   | I   | J   | K   |
| L   | M   | N   | O   |

## Problem 7
