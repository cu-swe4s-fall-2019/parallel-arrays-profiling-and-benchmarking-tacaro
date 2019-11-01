import data_viz as dz
import sys
import os
import argparse
import gzip
import matplotlib
import matplotlib.pylab as plt
from hash_table_sub import hash_functions
from hash_table_sub import hash_tables as ht
from os import path
matplotlib.use('Agg')


data_file_name = 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_\
reads.acmg_59.gct.gz'
sample_info_file_name = 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
group_col_name = 'SMTS'  # stores tissue categories
sample_id_col_name = 'SAMPID'
gene_name = 'ACTA2'


def linear_search(key, L):
    for l in range(len(L)):  # for each element in the list
        current = L[l]
        if key == current:  # if the key is the current value
            return l  # return the key
    return -1  # else, return a fake index to indicate failure


def binary_search(key, D):
    low_bound = -1
    up_bound = len(D)
    while (up_bound - low_bound > 1):
        middle = (up_bound + low_bound) // 2  # floor division

        if key == D[middle][0]:  # if you find the key at the midpoint..
            return D[middle][1]  # return the key:value at that point

        if (key < D[middle][0]):  # if the key is less than the value at
            # mid (alphabetically, numerically, etc.)
            up_bound = middle
            # the key is below the current value,
            # set the new high bracket to the current midpoint
        else:
            low_bound = middle
            # otherwise, the key is above the current value,
            # set the new low bracket to current midpoint

    return -1  # else, return a fake index to indicate failure


def hashing(group, file):
    header = None
    target = []
    hash = ht.ChainedHash(90000, hash_functions.h_ascii)

    for l in open(file):
        sample_data = l.rstrip().split('\t')
        if header is None:
            header = sample_data
            continue

        sample_id = linear_search('SAMPID', header)
        target_id = linear_search(group, header)

        if target_id == -1:
            return None, target

        key = sample_data[target_id]
        val = sample_data[sample_id]
        query = hash.search(key)
        if search is None:
            hash.add(key, [val])
            target.append(key)
        else:
            search.append(value)
    return hash, target


def main():
    parser = argparse.ArgumentParser(
                description='Open file, find tissue gene counts for given \
                gene',
                prog='bay')

    parser.add_argument('-gr',  # input gene reads, from user
                        '--gene_reads',
                        type=str,
                        help="GTEx Gene Counts, likely a .gz file",
                        required=True)

    parser.add_argument('-sa',  # desired samp attr, from user
                        '--sample_attributes',
                        type=str,
                        help='GTEx Sample Attirubtes File, likely a .txt file',
                        required=True)

    parser.add_argument('-g',  # desired gene, from user
                        '--gene',
                        type=str,
                        help='Desired Gene to search. Must match exactly',
                        required=True)

    parser.add_argument('-gt',  # desired group, from user
                        '--group_type',
                        type=str,
                        help="Takes SMTS, 'sample tissue', or SMTSD, 'Tissue \
                        Group'",
                        required=True)

    parser.add_argument('-o',  # desired output, from user
                        '--output_file',
                        type=str,
                        help='Desired name of output plot.',
                        required=True)

    args = parser.parse_args()
    data_file_name = args.gene_reads
    sample_info_file_name = args.sample_attributes
    gene_name = args.gene
    group_col_name = args.group_type
    out_file_name = args.output_file

    if group_col_name == "SMTS" or group_col_name == "SMTSD":
        pass
    else:
        raise ValueError("You must enter a group type: SMTS, or SMTSD")

    if path.exists(out_file_name):
        raise OSError("File path already exists!")
        sys.exit(1)

    if path.exists(data_file_name) is False:
        raise OSError("Data file not present in working directory!")
        sys.exit(1)

    if path.exists(sample_info_file_name) is False:
        raise OSError("Sample attributes not present in working directory!")
        sys.exit(1)

    table, target = hashing(args.group_type, args.sample_attributes)
    group.sort()

    v = None
    d = None
    count_header = None
    for l in gzip.open(args.gene_reads, 'rt'):
        if v is None:
            v = l
            continue
        if d is None:
            d = l
            continue
        if count_header is None:
            count_header = l.rstrip().split('\t')
            count_header_exp = []
            for i in range(len(count_header)):
                count_header_exp.append([count_header[i], i])
            count_header_exp.sort()
            continue

        counts = l.rstrip().split('\t')
        d_id = linear_search('Description', count_header)

    if d_id == -1:
        print('Gene not found')
        sys.exit(1)

    if counts[d_id] == args.gene:
        printed = []
        chained = hash_tables.ChainedHash(90000, hash_functions.h_ascii)
        for i in range(d_id + 1, len(count_header)):
            chained.add(count_header[i], int(counts[i]))
        for attr in group:
            count_list = []
            locator = table.search(attr)
            if locator is None:
                continue
            for sample_name in locator:
                count = chained.search(sample_name)
                if count is None:
                    continue
                count_list.append(count)
            printed.append(count_list)

        dz.boxplot(printed, group, args.gene, args.group_type, "Gene Read\
         Counts", args.output_file)

###########################


if __name__ == '__main__':
    main()
