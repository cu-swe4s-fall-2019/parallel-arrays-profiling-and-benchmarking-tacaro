import sys
import os
import math
import numpy as np

a = np.loadtxt(sys.stdin, dtype=np.int)


def read_stdin_col(col_num):
    return a[:, col_num]


def main():
    print(read_stdin_col(0))
    print(read_stdin_col(1))


if __name__ == '__main__':
    main()
