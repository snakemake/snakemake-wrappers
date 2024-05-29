def parse_input(input_item, parser=None, **kwargs):
    def inner(wildcards, input_item):
        with open(input.get(input_item), "r") as infile:
            if parser is None:
                return infile.read().strip()
            else:
                return parser(infile, kwargs)

    return inner


def extract_checksum(infile, **kwargs):
    import polars as pl
    import polars.selectors as cs

    return (
        pl.read_csv(infile, separator=" ", has_header=False)
        .filter(cs.by_index(1).str.ends_with(kwargs["file"]))
        .select(cs.by_index(0))
        .item()
    )
