def extract_checksum(infile, **kwargs):
    import pandas as pd

    return (
        pd.read_csv(infile, sep="  ", index_col=1, header=None, engine="python")
        .filter(like=kwargs.get("file"), axis=0)
        .iloc[0]
        .item()
    )


def parse_input(input_item=None, parser=None, **kwargs):
    def inner(wildcards, input):
        with open(input.get(input_item), "r") as infile:
            if parser is None:
                return infile.read().strip()
            else:
                return parser(infile, **kwargs)

    return inner
