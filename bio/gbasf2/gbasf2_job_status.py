#!/usr/bin/env python2

"""
Script that calls gbasf/Dirac API dictionary with status and other information
on all jobs in a project.  If executed, outputs the information as json.  Can
only be executed in a gbasf2 environment with python2.  It is therefore called
by the gbasf2 batch process in a subprocess with the correct environment.

Adapted from some example code by Michel Villanueva in
https://questions.belle2.org/question/7463/best-way-to-programatically-check-if-gbasf2-job-is-done/
"""
from __future__ import print_function

import argparse
import os
import json
import sys

from BelleDIRAC.gbasf2.lib.job.information_collector import InformationCollector
from BelleDIRAC.Client.helpers.auth import userCreds


@userCreds
def get_job_status_dict(project_name, user_name):
    """
    If successful, returns a dictionary for all jobs in the project with a structure like the following,
    which I have taken and adapted from an example output::

        {
            "<JobID>": {
                "SubmissionTime": "2020-03-27 13:08:49",
                "Owner": "<dirac username>",
                "JobGroup": "<ProjectName>",
                "ApplicationStatus": "Done",
                "HeartBeatTime": "2020-03-27 16:01:39",
                "Site": "LCG.KEK.jp",
                "MinorStatus": "Execution Complete",
                "LastUpdateTime": "2020-03-27 16:01:40",
                "Status": "<Job Status>"
            }
        ...
        }
    """
    if user_name is None:
        user_name = os.getenv("BELLE2_USER")
    login = [user_name, "belle"]
    newer_than = "1970-01-01"
    projects = [project_name]
    info_collector = InformationCollector()
    result = info_collector.getAllJobsInProjects(
        projects, date=newer_than, login=login, statuses={"Status": ["all"]}
    )
    project_items = result["Value"][projects[0]]
    status = info_collector.getJobSummary(project_items)
    if not status["OK"]:
        # info_collector returned with False status, probably means project does not exist
        raise sys.exit(3)
    return status["Value"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--project", type=str, required=True, help="gbasf2 project name"
    )
    parser.add_argument("-u", "--user", type=str, default=None, help="grid username")
    args = parser.parse_args()
    job_status_dict = get_job_status_dict(args.project, args.user)
    print(json.dumps(job_status_dict))
