def get_fractions():
    if config.get("reads_are_paired", True):
        fractions = ["R1", "R2"]
    else:
        fractions = ["se"]

    return fractions
