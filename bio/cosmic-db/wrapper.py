"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Till Hartmann"
__copyright__ = "Copyright 2021, Till Hartmann"
__email__ = "till.hartmann@udo.edu"
__license__ = "MIT"

import requests
import os
from typing import List
from snakemake.shell import shell

email = os.environ["COSMIC_EMAIL"]
password = os.environ["COSMIC_PW"]
assert email, "$COSMIC_EMAIL is not set"
assert password, "$COSMIC_PW is not set"

COSMIC_URL = "https://cancer.sanger.ac.uk/cosmic/file_download"


def available_builds() -> List[str]:
    builds = requests.get(COSMIC_URL).json()
    return builds


def available_datasets(build: str) -> List[str]:
    datasets = requests.get(f"{COSMIC_URL}/{build}").json()
    return [d.rpartition("/")[-1] for d in datasets]


def available_versions(build: str, dataset: str) -> List[str]:
    versions = requests.get(f"{COSMIC_URL}/{build}/{dataset}").json()
    return [v.rpartition("/")[-1] for v in versions]


def available_files(build: str, dataset: str, version: str) -> List[str]:
    files = requests.get(f"{COSMIC_URL}/{build}/{dataset}/{version}").json()
    return [f.rpartition("/")[-1] for f in files]


def download_path(build: str, dataset: str, version: str, file: str) -> str:
    return f"{COSMIC_URL}/{build}/{dataset}/{version}/{file}"


build = snakemake.params.get("build", "")
dataset = snakemake.params.get("dataset", "")
version = snakemake.params.get("version", "")
file = snakemake.params.get("file", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

builds = available_builds()
assert build in builds, f"{build} is not available. Choose one of: {builds}."

datasets = available_datasets(build)
assert dataset in datasets, f"{dataset} is not available. Choose one of: {datasets}."

versions = available_versions(build, dataset)
assert version in versions, f"{version} is not available. Choose one of: {versions}."

files = available_files(build, dataset, version)
assert file in files, f"{file} is not available. Choose one of: {files}."

download_url = (
    requests.get(download_path(build, dataset, version, file), auth=(email, password))
    .json()["url"]
    .strip()
)

shell('curl "{download_url}" -o {snakemake.output[0]} {log}')
