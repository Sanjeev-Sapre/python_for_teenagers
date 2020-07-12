from turtle import *

speed(0)
penup()
grid = {}
while True:
  p = tuple(map(round, pos()))
  c = grid.get(p, 'white')
  if c == 'white':
    c = 'red'
    left(90)
  else:
    c = 'white'
    right(90)
  grid[p] = c
  dot(10, c)
  forward(10)