import numpy as np
import sys

def numpy_magic(array, pattern, shape):
    return np.all(np.all(np.lib.stride_tricks.sliding_window_view(n, shape) == pattern, axis=3), axis=2).sum()

def numpy_magic_diagonal(array, pattern, flip):
    if flip:
        return np.all(np.diagonal(np.equal(np.lib.stride_tricks.sliding_window_view(np.fliplr(array), (4,4)), np.fliplr(pattern)),axis1=2,axis2=3), axis=2).sum()
    else:
        return np.all(np.diagonal(np.equal(np.lib.stride_tricks.sliding_window_view(array, (4,4)),pattern),axis1=2,axis2=3), axis=2).sum()

def find_x_mas():
    return np.all(np.diagonal(np.equal(np.lib.stride_tricks.sliding_window_view(array, (4,4)),pattern),axis1=2,axis2=3), axis=2).sum()

    pass

with open(sys.argv[1]) as f:
    lines = [list(l.strip()) for l in f.readlines() ]
    n = np.array(lines)
    print(n)
    patterns = [
        (np.array(['X','M','A','S']), (1,4)),
        (np.array(['S','A','M','X']), (1,4)),
        (np.array([['X'], ['M'], ['A'],['S']]), (4,1)),
        (np.array([['S'], ['A'], ['M'],['X']]), (4,1))
    ]
    s2 = (sum(map(lambda p: numpy_magic(n, p[0], p[1]), patterns)))

    diagonals = [
        (np.array([['X','', '',''],
                 ['', 'M','',''],
                 ['', '','A',''],
                 ['', '','','S']]), False),
        (np.array([['S','', '',''],
                 ['', 'A','',''],
                 ['', '','M',''],
                 ['', '','','X']]), False),
        (np.array([['','', '','X'],
                 ['', '','M',''],
                 ['', 'A','',''],
                 ['S', '','','']]), True),
        (np.array([['','', '','S'],
                 ['', '','A',''],
                 ['', 'M','',''],
                 ['X', '','','']]), True)]
    s1 = (sum(map(lambda p: numpy_magic_diagonal(n, p[0], p[1]), diagonals)))

    #print(s1 + s2)

    p2 = np.array([['M','','S'],
                   ['','A',''],
                   ['M','','S']])


    truth2 = np.array([[True,False,True],
                   [False,True,False],
                   [True,False,True]])
    print(np.all(np.all(np.equal(np.lib.stride_tricks.sliding_window_view(n, (3,3)),np.rot90(p2,k=0)) == truth2, axis=3), axis=2).sum() +
          np.all(np.all(np.equal(np.lib.stride_tricks.sliding_window_view(n, (3,3)),np.rot90(p2,k=1)) == truth2, axis=3), axis=2).sum() +
          np.all(np.all(np.equal(np.lib.stride_tricks.sliding_window_view(n, (3,3)),np.rot90(p2,k=2)) == truth2, axis=3), axis=2).sum() +
          np.all(np.all(np.equal(np.lib.stride_tricks.sliding_window_view(n, (3,3)),np.rot90(p2,k=3)) == truth2, axis=3), axis=2).sum())