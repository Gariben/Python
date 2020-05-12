## Mother Exercise Challenge Rating Calculator

[The "Mother" Exercise](https://vimeo.com/14691967) is an exercise for Touch Instruments developed by Markus Reuter.

As his student I have practiced 36 finger pattern for this exercise, and we are working on
a metric ("Challenge Rating") to determine which finger patterns are most difficult, and, presumably most beneficial
for students of these instruments.

### Step 1: Finger movement tables

While we originally set out to determine the Challenge Rating by examining an entire finger pattern (e.g. `123456`), it became
quickly apparent that some movements maybe easier in one direction (e.g. ascending the fretboard) versus another direction
(descending, alternating on a single fret). Thus it was decided that we should create tables wherein we prescribe the relative
difficulty of one finger to another based on the context. The metric used is how much contraction and movement the fingers and hand
must make in order to make the movement. These values are comparative, as to avoid further subjectivity from attempting to determine an objective value for each.
These tables will remain configurable should these values change, or if one wishes to eventually compare the results of different values.

```
ascending[1][2] = 1
ascending[1][3] = 4
ascending[1][4] = 6

ascending[2][1] = 7
ascending[2][3] = 3
ascending[2][4] = 5

ascending[3][1] = 11
ascending[3][2] = 8
ascending[3][4] = 3

ascending[4][1] = 12
ascending[4][2] = 10
ascending[4][3] = 9

```

### Step 2: Exercise Simulation

Once the `ascending`, `descending`, and `rolling` tables have been determined, simulations of all finger patterns' movements will be simulated,
and the challenging rating values will be added from finger to finger. This will not be the entire exercise, but rather the smallest possible version
of the exercise that incorporates all three movements. This will reduce a redundant inflation of the Challenge Rating.


#### TODO:
* Experiment with deriving `rolling`, `descending` tables from ascending.
