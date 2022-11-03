#!/usr/bin/env python2

"""
Script to run as subprocess in a gbasf2 environment (with ``run_with_gbasf``) to
query the proxy status. If successful, prints proxy info in JSON format.
"""

from __future__ import print_function

import json
import sys

from DIRAC import gLogger
from DIRAC.Core.Base import Script
from DIRAC.Core.Security.X509Chain import X509Chain
from DIRAC.Core.Security.ProxyInfo import getProxyInfo


class CertEncoder(json.JSONEncoder):
    """
    JSON encoder for data structures possibly including certificate objects.
    """

    def default(self, obj):
        if isinstance(obj, X509Chain):
            return obj.dumpAllToString()
        return json.JSONEncoder.default(self, obj)


if __name__ == "__main__":
    # Suppress error messages, since stdout of this script is expected to be in JSON format
    gLogger.setLevel("FATAL")

    Script.enableCS()  # Required so dict includes username
    ProxyInfo = getProxyInfo()
    if not ProxyInfo["OK"]:
        sys.exit(1)

    print(json.dumps(ProxyInfo["Value"], cls=CertEncoder))
