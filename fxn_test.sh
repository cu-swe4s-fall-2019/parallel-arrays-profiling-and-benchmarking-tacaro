test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest


run test_no_gr python plot_gtex.py --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file ACTA2.png
assert_exit_code 2

run test_no_sa python plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --gene ACTA2 --group_type SMTS --output_file ACTA2.png
assert_exit_code 2

run test_no_gene python plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --group_type SMTS --output_file ACTA2.png
assert_exit_code 2

touch already.png
run test_file_already_exists python plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file already.png
assert_exit_code 1
rm already.png

run test_col_name_bad python plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type wallawallabingbang --output_file ACTA2.png
assert_exit_code 1

run test_no_data python plot_gtex.py --gene_reads GTEx_Analysi_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type wallawallabingbang --output_file ACTA2.png
assert_exit_code 1

run test_no_attr python plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Ans_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file ACTA2.png
assert_exit_code 1

run test_pycodestyle_dv pycodestyle data_viz.py
assert_exit_code 0

run test_pycodestyle_gd pycodestyle get_data.py
assert_exit_code 0

run test_pycodestyle_ml pycodestyle math_lib.py
assert_exit_code 0

run test_pycodestyle_pg pycodestyle plot_gtex.py
assert_exit_code 0

run test_pycodestyle_tests pycodestyle tests.py
assert_exit_code 0
