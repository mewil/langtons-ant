# Langton's Ant

Langton's Ant Simulation for CMPLXSYS 530

To run the simulation run the following commands:

1. `git clone https://github.com/mewil/langtons-ant`
2. `cd langtons-ant`
3. `python sim.py`

## Implementation

This simulation uses Python's turtle library, which provides an interface similar to that of NetLogo. I initialize a screen and two ant agents, then I repeated call the step function on the agents, which checks the agent's environment and moves the agent accordingly, coloring the environment as it moves. To increase performance, the screen is only updated every 25 steps.

## Analysis

It is facinating that a single ant seems to behave randomly for 10,000 steps, before falling into a deterministic upward movement. When two ants are ants are used in the system, they both fall into a deterministic pattern, both before the 10,000 steps it takes a single ant. See images comparing the results of one ant and two ants below.

System state with one ant after 10000 steps:
![alt text](https://github.com/mewil/langtons-ant/blob/master/img.png "One Ant")

System state with two ants after 10000 steps:
![alt text](https://github.com/mewil/langtons-ant/blob/master/img2.png "Two Ants")
