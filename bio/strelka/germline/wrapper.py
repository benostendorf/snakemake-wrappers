__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"


import os
from pathlib import Path

config_extra = snakemake.params.get("config_extra", "")
run_extra = snakemake.params.get("run_extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam = snakemake.input.get("bam")  # input bam file, required
assert bam is not None, "input-> bam is a required input parameter"

if snakemake.output[0].endswith(".vcf.gz"):
    run_dir = Path(snakemake.output[0]).parents[2]
else:
    run_dir = snakemake.output

os.system(
    "configureStrelkaGermlineWorkflow.py "  # configure the strelka run
    "--bam %s "  # input bam
    "--referenceFasta %s "  # reference genome
    "--runDir %s "  # output directory
    " %s "  # additional parameters for the configuration
    "&& %s/runWorkflow.py "  # run the strelka workflow
    "-m local "  # run in local mode
    "-j %s "  # number of threads
    "%s "  # additional parameters for the run
    "%s"
    % (
        bam,
        snakemake.input.fasta,
        run_dir,
        config_extra,
        run_dir,
        snakemake.threads,
        run_extra,
        log,
    )
)
