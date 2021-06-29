# 2021/06/11
# Conway's Game of Life - Alternate rules analysis project by Atlas Yang

import numpy as np
import sys, random, copy

# making cell grid with class(OOP)

class CellMap:
    def __init__(self, n, dimension, state_num):
        self.N = n
        self.DIM = dimension
        self.CELL_NUM = self.N ** self.DIM
        self.STATE_NUM = state_num
        self.SHAPE = tuple([self.N for i in range(self.DIM)])
        self.map = np.array([np.random.randint(0, self.STATE_NUM) for i in range(self.CELL_NUM)]).reshape(self.SHAPE)
        self.ADJ_CELL_NUM = (3 ** self.DIM) - 1
        self.transition_matrix = np.array([np.random.randint(0, self.STATE_NUM) for i in range(self.STATE_NUM * (self.ADJ_CELL_NUM + 1))]).reshape((self.STATE_NUM, self.ADJ_CELL_NUM + 1))
        self.POS_SET = self.p_set_init([[i] for i in range(self.N)])
        self.ADJ_AID_SET = self.h_set_init([[-1], [0], [1]])
    

    def zero_one(self, n):
        if n == 0:
            return 0
        else:
            return 1
    

    def h_set_init(self, tset):
        t = []
        if len(tset) == 3 ** self.DIM:
            return tset
        else:
            for i in tset:
                for j in (-1, 0, 1):
                    t.append(np.append(i, j))
            return self.h_set_init(t)


    def p_set_init(self, pset):
        p = []
        if len(pset) == self.N ** self.DIM:
            return pset
        else:
            for i in pset:
                for j in range(self.N):
                    p.append(np.append(i, j))
            return self.p_set_init(p)

    
    def sum_adjacent(self, pos):
        try:
            s = 0
            for aid_pos in self.ADJ_AID_SET:
                s += self.zero_one(self.map[tuple(pos + aid_pos)])
            s -= self.zero_one(self.map[tuple(pos)])
            return s
        except:
            return 0


    def process(self, epoch = 1):
        for i in range(epoch):
            t_map = np.zeros_like(self.map)
            for pos in self.POS_SET:
                t_map[tuple(pos)] = int(self.transition_matrix[self.map[tuple(pos)]][self.sum_adjacent(pos)])
            self.map = t_map
        return

