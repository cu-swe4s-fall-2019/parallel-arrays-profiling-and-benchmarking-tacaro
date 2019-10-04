# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

# Required Data Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt


# Usage
*plot_gtex.py* is the main component of this package. It is a python script that
intakes GTEX RNA seq data and shows differential gene transcription patterns
across various tissues.

It requires:
- A GTEX Gene Reads file of the form: GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
- A GTEX sample attributes file of the form: GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

plot_gtex.py requires the following arguments:
- --gene_reads (-gr): A GTEX Gene REads file, in file format .gz
- --sample_attributes (-sa): A GTEx sample attributes file, in .txt format
- --gene (-g): The desired gene to be searched
- --group_type (-gt): Either SMTS 'sample tissue' or SMTSD 'Tissue Group'
- --output_file (-o): desired name of plot to be generated, in .png format

plot_gtex.py is executed from the command line:
`$ python plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz  --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file ACTA2.png
`
This is the only script the user should execute. The included modules are referenced
by plot_gtex.py.


# Installation
1. pycodestyle is required to run the PEP8 adherence tests. This can be installed
with `pip install pycodestyle`, upgraded with `pip install --upgrade pycodestyle`
and uninstalled with `pip uninstall pycodestyle`.

2. Functional testing requires ssshtest, which can be installed with:
`test -e ssshtest || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest . ssshtest`

3. Matplotlib is required for plotting, it can be installed with:
`conda activate swe4s`
`conda install matplotlib`

4. Pillow is required for image testing, it can be installed with
`pip install Pillow`
