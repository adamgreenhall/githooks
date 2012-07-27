#!/usr/bin/env python

"""
Validate that all python files staged for commit are pep8 complaint
"""

import os
import re
import tempfile
import uuid
from subprocess import Popen, PIPE


def get_filenames_from_git_stage(
        ext=None, modified=True, created=True, deleted=True):
    """
    Get filenames that are staged in git

    By default we gets all files that have been modified, deleted, or
    created. You can change this behavior by modifying the default
    arguments.
    """
    flag = ""
    if modified:
        flag += "M"
    if created:
        flag += "A"
    if deleted:
        flag += "D"

    file_re = re.compile(r"^[%s]\s+(.+%s)$" % (flag, ext.replace(".", "\.")))
    git = Popen(("git", "status", "--porcelain"), stdout=PIPE)

    files = []
    for line in git.stdout:
        m = file_re.match(line)
        if m:
            files.append(m.groups()[0])

    return files


def get_file_from_git_stage(filename):
    """
    Get a file content from git
    """
    git = Popen(("git", "show", ":%s" % filename), stdout=PIPE)
    stdout, stderr = git.communicate()
    return stdout


def pep8(python_src_code):
    """
    Run pep8 on some python source code
    """
    tmp_dir = tempfile.gettempdir()

    tmp_filename = os.path.join(tmp_dir, str(uuid.uuid4()))
    with open(tmp_filename, mode="w") as tmp_file:
        tmp_file.write(python_src_code)

    pep8 = Popen(("pep8", tmp_filename), stdout=PIPE)
    stdout, stderr = pep8.communicate()
    output = stdout.strip().split("\n")

    os.unlink(tmp_filename)

    results = map(lambda s: s[len(tmp_filename) + 1:], output)
    return results


if __name__ == "__main__":

    import sys

    exit_status = 0
    for py_file in get_filenames_from_git_stage(ext=".py", deleted=False):
        content = get_file_from_git_stage(py_file)
        for line in pep8(content):
            print "%s %s" % (py_file, line)
            exit_status = 1

    sys.exit(exit_status)
