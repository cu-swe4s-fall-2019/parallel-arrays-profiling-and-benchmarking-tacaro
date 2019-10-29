import sys
import matplotlib
import argparse
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def main():
    parser = argparse.ArgumentParser(
        description='Generate scatter from stdin',
        prog='scatter')

    parser.add_argument('-o',
                        '--outfile',
                        type=str,
                        help='Output filename')
    parser.add_argument('-x',
                        '--xlabel',
                        type=str,
                        help='xlab')
    parser.add_argument('-y',
                        '--ylabel',
                        type=str,
                        help='ylab')

    args = parser.parse_args()

    out_file = args.outfile
    x_label = args.xlabel
    y_label = args.ylabel

    X, Y = [], []
    i = 0
    for l in sys.stdin:
        A = l.rstrip().split()
        if len(A) == 2:
            X.append(float(A[0]))
            Y.append(float(A[1]))
        elif len(A) == 1:
            X.append(float(i))
            Y.append(float(A[0]))
            i += 1

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(X, Y, '.', ms=1, alpha=0.5)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.savefig(out_file, bbox_inches='tight')


if __name__ == '__main__':
    main()
