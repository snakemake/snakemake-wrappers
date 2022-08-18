def get_processed_consensus_input(wildcards):
    if wildcards.read_type == "se":
        return "results/consensus/{}.se.fq".format(wildcards.sample)
    return [
        "results/consensus/{}.1.fq".format(wildcards.sample),
        "results/consensus/{}.2.fq".format(wildcards.sample),
    ]
