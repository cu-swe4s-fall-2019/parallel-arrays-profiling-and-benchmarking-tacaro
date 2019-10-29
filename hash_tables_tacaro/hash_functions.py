import os
import sys
import argparse


def h_ascii(key, N):
    try:
        N = int(N)
    except ValueError:
        print('Must be an integer.')
        return None
    key = str(key)
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    output = s % N
    return output


def h_rolling(key, N, p=53, m=2**64):
    try:
        N = int(N)
    except ValueError:
        print('The size of the hash table (N) should be an integer.')
        return None
    key = str(key)
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p ** i
    s = s % m
    output = s % N
    return output


def h_fletcher64(key, N):
    if key is None:
        raise ValueError("Cannot be none.")
    try:
        key = str(key)
    except TypeError:
        print("Cannot convert the key to a string")
        sys.exit(1)
    if key == '':
        raise ValueError("Can't use empty string")
    if key is None:
        raise ValueError("Key cannot be None")

    a = list(map(ord, key))
    b = [sum(a[:i]) % 4294967295 for i in range(len(a)+1)]
    H = (sum(b) << 32) | max(b)
    return H


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='A Python module of different hash methods',
        prog='hash_functions'
    )

    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help='input file')
    parser.add_argument('-m',
                        '--method',
                        type=str,
                        help='Hash methods. Available options are: "ascii" \
                        "rolling" and "fletcher64".')
    args = parser.parse_args()

    if (not os.path.exists(args.input)):
        print('Input file')
        sys.exit(1)

    for l in open(args.input):
        if (args.method == 'ascii'):
            print(h_ascii(l, 100000))
        elif (args.method == 'rolling'):
            print(h_rolling(l, 100000))
        elif (args.method == 'fletcher64'):
            print(h_fletcher64(l, 100000))
        else:
            print('Please input the hash methods avaiable, including "ascii" \
                  ,"rolling" or "fletcher64".')
            sys.exit(1)
