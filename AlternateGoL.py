# 2021/06/11
# Conway's Game of Life - Alternate rules analysis project by Atlas Yang

import numpy as np
import sys, random, copy


# Constants
N = 10
DIM = 2
CELL_NUM = N ** DIM
ADJ_CELL_NUM = (3 ** DIM) - 1
STATE_NUM = 2

SHAPE = np.array([N for i in range(DIM)])

cellMap = np.array([np.random.randint(0, STATE_NUM) for i in range(CELL_NUM)]).reshape(SHAPE)

# All-zero rule
T = np.zeros((STATE_NUM, ADJ_CELL_NUM + 1), dtype = np.int)

# Random rule
T = np.array([np.random.randint(0, STATE_NUM) for i in range(STATE_NUM * (ADJ_CELL_NUM + 1))]).reshape(T.shape)

#T = np.array([[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0]])

def zero_one(n):
    if n == 0:
        return 0
    else:
        return 1

def p_set_init(pset):
    p = []
    if len(pset) == N ** DIM:
        return pset
    else:
        for i in pset:
            for j in range(N):
                p.append(np.append(i, j))
        return p_set_init(p)
POS_SET = p_set_init([[i] for i in range(N)])


def h_set_init(tset):
    t = []
    if len(tset) == 3 ** DIM:
        return tset
    else:
        for i in tset:
            for j in (-1, 0, 1):
                t.append(np.append(i, j))
        return h_set_init(t)
ADJ_AID_SET = h_set_init([[-1], [0], [1]])



def sum_adjacent(pos):
    try:
        s = 0
        for aid_pos in ADJ_AID_SET:
            s += zero_one(cellMap[tuple(pos + aid_pos)])
        s -= zero_one(cellMap[tuple(pos)])
        return s
    except:
        return 0


def process():
    global cellMap
    basis_pos = np.array([0 for i in range(DIM)])
    t_map = np.zeros_like(cellMap)
    for pos in POS_SET:
        t_map[tuple(pos)] = int(T[cellMap[tuple(pos)]][sum_adjacent(pos)])
    cellMap = t_map
    return

