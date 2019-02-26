# Langston's Ant
# Michael Wilson | @mewil
# February 26, 2018
# CMPLXSYS 530
# Inspired to use turtle library by https://fiftyexamples.readthedocs.io/en/latest/life.html

from turtle import Turtle, Screen

WHITE = 'white'
BLACK = 'black'

def update_cell(env, ant, color):
    ant.fillcolor(color)
    env[(round(ant.xcor()), round(ant.ycor()))] = color

def step(ant, pos, env):
    if pos not in env or env[pos] == WHITE:
        update_cell(env, ant, BLACK)
        ant.right(90)
    else:
        update_cell(env, ant, WHITE)
        ant.left(90)

    ant.forward(10)
    ant.stamp()
    return (round(ant.xcor()), round(ant.ycor()))


def main():
    env = {}
    screen = Screen()
    screen.screensize(500, 500)
    screen.tracer(0, 0)

    ant = Turtle()
    ant.shape('square')
    ant.speed('fastest')

    ant2 = ant.clone()
    ant2.right(180)

    p, p2 = (0, 0), (0, 0)

    for i in range(10001):
        p = step(ant, p, env)
        p2 = step(ant2, p2, env)
        if i % 25 == 0: screen.update()

if __name__ == "__main__":
    main()