rule get_genome:
    output:
        "refs/genome.fasta"
    params:
        species="saccharomyces_cerevisiae",
        datatype="dna",
        build="R64-1-1",
        release="75"
    log:
        "logs/get_genome.log"
    wrapper:
        "master/bio/reference/ensembl-sequence"
