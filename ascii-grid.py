from math import floor
from math import ceil

join = ''.join

class grid:
  blockWidth = 0
  blockHeight = 0
  width = 0
  height = 0

  hedge = '-'
  vedge = '|'
  corn = '+'

  stuff = [[]]

  def hb(self):
    return self.corn +\
           join([join([self.hedge for j in range(self.blockWidth)]) +\
           self.corn for i in range(self.width)]) +\
           '\n'

  def fr(self, r):
    return self.vedge +\
           join([self.stuff[r][i] +\
                 self.vedge\
                 for i in range(len(self.stuff[r]))]) +\
           '\n'
  
  def er(self):
    return self.vedge +\
           join([join([join([' ' for k in range(self.blockWidth)])]) +\
                              self.vedge for i in range(self.width)]) + '\n'

  def draw(self):
    return self.hb() +\
           join([join([self.er() for i in range(floor(self.blockHeight/2))]) +\
                 self.fr(j) +\
                 join([self.er() for i in range(ceil(self.blockHeight/2))]) +\
                 self.hb()\
                 for j in range(self.height)])

  def update(self, x, y, v):
    if len(v) > self.blockWidth:
      v = v[0:self.blockWidth+1]
    while len(v) < self.blockWidth:
      if len(v) % 2 == 0:
        v = v + ' '
      else:
        v = ' ' + v
    self.stuff[y][x] = v

  def __init__(self, bw, bh, w, h):
    self.blockWidth = bw
    self.blockHeight = bh
    self.width = w
    self.height = h
    self.stuff = [[join([' ' for k in range(self.blockWidth)]) for i in range(self.width)] for j in range(self.height)]

g = grid(5,2,3,3)
g.update(1,1,'X/O')
print(g.draw())
