import data_viz as dz
import sys
import os
import argparse
import gzip
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
from os import path

data_file_name='GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.\
gct.gz'
sample_info_file_name='GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
group_col_name = 'SMTS' # stores tissue categories
sample_id_col_name = 'SAMPID'
gene_name = 'ACTA2'




def linear_search(key, L):
    for l  in range(len(L)): # for each element in the list
        current =  L[l]
        if key == current: # if the key is the current value
            return l  # return the key
    return -1  # else, return a fake index to indicate failure

def binary_search(key, D):
    low_bound = -1
    up_bound = len(D)
    while (up_bound - low_bound > 1):
        middle = (up_bound + low_bound) // 2 # floor division

        if key == D[middle][0]: # if you find the key at the midpoint..
            return D[middle][1] # return the key:value at that point

        if ( key < D[middle][0] ):  # if the key is less than the value at mid (alphabetically, numerically, etc.)
            up_bound = middle # the key is below the current value, set the new high bracket to the current midpoint
        else:
            low_bound = middle # otherwise, the key is above the current value, set the new low bracket to current midpoint

    return -1  # else, return a fake index to indicate failure


def main():
    parser = argparse.ArgumentParser(
                description='Open file, find tissue gene counts for given gene',
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

    if path.exists(data_file_name) == False:
        raise OSError("Data file not present in working directory!")
        sys.exit(1)

    if path.exists(sample_info_file_name) == False:
        raise OSError("Sample attributes not present in working directory!")
        sys.exit(1)

########################## LINEAR SEARCH FUNCTIONALITY
    '''
    samples = []
    sample_info_header = None
    for l in open(sample_info_file_name):
        if sample_info_header == None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))

    group_col_idx = linear_search(group_col_name, sample_info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

    groups = []
    members = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]

        curr_group_idx = linear_search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)

    version = None
    dim = None
    data_header = None

    gene_name_col = 1

    group_counts = [ [] for i in range(len(groups)) ]

    for l in gzip.open(data_file_name, 'rt'): # 'rt indicates that we are reading text, in comparison to 'rb' which is 'read binary'
        if version == None:
            version = l
            continue

        if dim == None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header == None:
            data_header = l.rstrip().split('\t')
            continue

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene_name: # linear search functionality
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    member_idx = linear_search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break

    dz.boxplot(group_counts, out_file_name, groups, gene_name, group_col_name)


    '''

###################### BINARY SEARCH FUNCTIONALITY
    samples = []
    sample_info_header = None
    for l in open(sample_info_file_name):
        if sample_info_header == None:
            sample_info_header = l.rstrip().split('\t') # designate the header as the first line in the file, add the items to a list
        else:
            samples.append(l.rstrip().split('\t')) # then add all the samples to a list

    # we use linear search here because the header is NOT sorted!
    group_col_idx = linear_search(group_col_name, sample_info_header) # find the group column name "SMTS" in the header list, note its index
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header) # find the index of the sample IDs within the header

    groups = []
    members = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]

        curr_group_idx = linear_search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)

    version = None
    dim = None
    data_header = None

    gene_name_col = 1


    group_counts = [ [] for i in range(len(groups)) ]

    for l in gzip.open(data_file_name, 'rt'):
        if version == None:
            version = l
            continue

        if dim == None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header == None:
            data_header = []
            i = 0
            for field in l.rstrip().split('\t'):
                data_header.append([field, i])
                i += 1
            data_header.sort(key=lambda tup: tup[0])

            continue

        A = l.rstrip().split('\t')

        if A[dv_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    member_idx = binary_search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break

    dz.boxplot(group_counts, out_file_name, groups, gene_name, group_col_name)

###########################
if __name__ == '__main__':
    main()
