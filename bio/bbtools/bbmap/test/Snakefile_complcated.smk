rule bbmap:
    input:
        reads=["reads/{sample}.1.fastq",
               "reads/{sample}.2.fastq",
               "reads/{sample}.se.fastq"],
        ref="genome.fasta",
    output:
        bam= "mapped/{sample}.bam",
        unmapped= ['unmapped/unmapped_reads.1.fastq.gz',
                   'unmapped/unmapped_reads.2.fastq.gz',
                   'unmapped/unmapped_reads.se.fastq.gz'],
        covstats='coverage/covstats.txt',       # Per-scaffold coverage info.
        basecov='coverage/basecov.txt.gz',      # Coverage per base location.
        bincov='coverage/bincov.txt',           # Print binned coverage per location (one line per X bases).
        scafstats= 'stats/scafstats.txt',       # Statistics on how many reads mapped to which scaffold.
        bhist= 'stats/bhist.txt',               # Base composition histogram by position.
        qhist= 'stats/qhist.txt',               # Quality histogram by position.
        idhist='stats/idhist.txt',              # Histogram of read count versus percent identity.
        statsfile='stats/mappingstats.txt',     # Mapping statistics are printed here.

    log:
        "logs/bbmap/{sample}.log"
    params:   # all parameters are oprional
        sort_bam= True, # all other keywords have toe correspond to the bbmap key words
        nodisk = True,  # otherwise stores index of ref
        minid = 0.76,
        ambigous = 'all',
        maxsites= 5,
        pigz=True,                  # pawn a pigz (parallel gzip) process for faster
        pairedonly=False,
        usejni=True,                # Do alignments faster, in C code.  Requires compiling the C code; details are in /jni/README.txt.
        k=13,
        secondary= True,            # Print secondary alignments
        secondarycov=True,          # Include coverage of secondary alignments.
        physcov=True,               # Calculate physical coverage for paired reads.
        covbinsize=1000,            # Set the binsize for binned coverage output.
        machineout=True,            # Set to true to output statistics in machine-friendly
        idbins='auto'               # Number idhist bins.  Set to 'auto' to use read length.
    threads: 8
    resources:
        mem=50*1e9                # oprional: bbmap normaly needs a lot of memory
    wrapper:
        "master/bio/bbtools/bbmap"
