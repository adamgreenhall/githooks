#!/usr/bin/env python

import re
import sys

from git_utils import (
    get_filenames_from_git_stage, get_file_from_git_stage)


pdb_re = re.compile("import\s+pdb")
exit_status = 0

for filename in get_filenames_from_git_stage(".py"):
    content = get_file_from_git_stage(filename)
    line_no = 0
    for line in content.split("\n"):
        line_no += 1
        if pdb_re.search(line):
            print "%s %d: !!! DEBUG CODE !!! %s" % (filename, line_no, line)
            exit_status = 1

sys.exit(exit_status)
