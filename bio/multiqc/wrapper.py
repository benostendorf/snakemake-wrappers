"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from os import path

from snakemake.shell import shell


input_dirs = set(path.dirname(fp) for fp in snakemake.input)
output_dir = path.dirname(snakemake.output[0])
output_name = path.basename(snakemake.output[0])
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "export LC_ALL=en_US.UTF-8;"
    "export LANG=en_US.UTF-8;"
    "multiqc"
    " {snakemake.params}"
    " --force"
    " -o {output_dir}"
    " -n {output_name}"
    " {input_dirs}"
    " {log}"
)
