import numpy as np
import matplotlib as mpl
import data_viz as dv

np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)
collectn_5 = np.random.normal(100, 10, 200)
collectn_6 = np.random.normal(80, 30, 200)
collectn_7 = np.random.normal(90, 20, 200)
collectn_8 = np.random.normal(70, 25, 200)

data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4, collectn_5, \
collectn_6, collectn_7, collectn_8]

def main():
    dv.boxplot(data_to_plot, 'testplot.png')

if __name__ == '__main__':
    main()
