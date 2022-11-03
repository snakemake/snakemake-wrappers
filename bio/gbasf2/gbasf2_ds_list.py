#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Script to run as subprocess in a gbasf2 environment (with ``run_with_gbasf``) to
list LFNs. If successful, prints matched LFNs as a list in JSON format.
"""

from __future__ import print_function

import argparse
import json
import sys

from BelleDIRAC.Client.helpers.auth import userCreds
from BelleDIRAC.gbasf2.lib.ds.manager import Manager


@userCreds
def get_lfns(dataset, user):
    """
    If successful, returns a list of matched LFNs.
    """
    manager = Manager()
    response = manager.getLfns(dataType=None, dataset=dataset, user=user)
    if not response["OK"]:
        sys.exit(1)
    return response["Value"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", help="Dataset query.")
    parser.add_argument("--user", help="DIRAC username.")
    args = parser.parse_args()
    lfns = get_lfns(args.dataset, args.user)
    print(json.dumps(lfns))
