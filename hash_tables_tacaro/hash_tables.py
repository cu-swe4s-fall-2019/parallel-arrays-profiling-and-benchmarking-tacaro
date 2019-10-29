import hash_functions
import sys
import time
import random
import os


def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


class LinearProbe:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.table = [None] * N

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        hash_slot = start_hash
        if self.table[start_hash] is None:
            self.table[start_hash] = (key, value)
        else:
            for i in range(self.N):
                query = (hash_slot + i) % self.N
                if self.table[query] is None:
                    self.table[query] = (key, value)
                    return True
            return False

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        for i in range(self.N):
            query = (start_hash + i) % self.N
            if self.table[query][0] == key:
                return self.table[start_hash][1]
            if self.table[start_hash] is None:
                return None
        return None


class QuadraticProbe:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.table = [None] * N

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        hash_slot = start_hash
        if self.table[start_hash] is None:  # base case
            self.table[start_hash] = (key, value)
        else:
            k = 0
            for i in range(self.N):
                query = (hash_slot + i**k) % self.N
                k += 1
                if self.table[query] is None:
                    self.table[query] = (key, value)
                    return True
            return False  # executes if key not found

        # pass

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        for i in range(self.N):
            k = 0
            query = (start_hash + i**k) % self.N
            k += 1
            if self.table[query][0] == key:
                return self.table[start_hash][1]  # return the value, index 1
            if self.table[start_hash] is None:
                return None
        return None  # executes if key not found


class ChainedHash:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        self.T[start_hash].append((key, value))
        self.M += 1
        return True

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        value = None
        for k, v in self.T[start_hash]:
            if key == k:
                value = v
                return value
        return value


def main():
    parser = argparse.ArgumentParser(
        description='Create hash table, benchmark its efficiency',
        prog='HashTables')

    parser.add_argument('-n',
                        '--size',
                        type=int,
                        help='table size')

    parser.add_argument('-a',
                        '--algorithm',
                        type=str,
                        help="OPTIONS: 'ascii' or 'rolling'")
    parser.add_argument('-s',
                        '--collision',
                        type=str,
                        help='OPTIONS: LP or CH')
    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help='input file name')
    parser.add_argument('-k',
                        '--n_key',
                        type=int,
                        help='number of keys')

    args = parser.parse_args()

    ht = None
    if args.algorithm == 'ascii':

        if args.collision == 'LP':
            ht = LinearProbe(args.size, hash_functions.h_ascii)
        elif args.collision == 'QP':
            ht = QuadraticProbe(args.size, hash_functions.h_ascii)
        elif args.collision == 'CH':
            ht = ChainedHash(args.size, hash_functions.h_ascii)
        else:
            print('Please input the collision resolution strategies \
                available, including "LP", "QP" or "CH".')
            sys.exit(1)

    elif args.algorithm == 'rolling':

        if args.collision == 'LP':
            ht = LinearProbe(args.size, hash_functions.h_rolling)
        elif args.collision == 'QP':
            ht = QuadraticProbe(args.size, hash_functions.h_rolling)
        elif args.collision == 'CH':
            ht = ChainedHash(args.size, hash_functions.h_rolling)
        else:
            print('Please input the collision resolution strategies \
                available, including "LP", "QP" or "CH".')
            sys.exit(1)

    elif args.algorithm == 'myown':

        if args.collision == 'LP':
            ht = LinearProbe(args.size, hash_functions.h_myown)
        elif args.collision == 'QP':
            ht = QuadraticProbe(args.size, hash_functions.h_myown)
        elif args.collision == 'CH':
            ht = ChainedHash(args.size, hash_functions.h_myown)
        else:
            print('Please input the collision resolution strategies \
                available, including "LP", "QP" or "CH".')
            sys.exit(1)

    else:
        print('Please input the hash algorithms available, either \
            "ascii" or "rolling".')
        sys.exit(1)

    keys_to_search = 100   # number of keys to search
    V = []

    if (not os.path.exists(args.input)):
        print('Input file not found')
        sys.exit(1)

    for l in open(args.input):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l, l)
        t1 = time.time()
        print('insert', ht.M/ht.N, t1 - t0)
        if ht.M == args.n_key:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1-t0)


if __name__ == '__main__':
    main()
