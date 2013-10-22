#!/usr/bin/env python

import re
import sys
from pyflakes.api import checkPath
from git_utils import (
    get_filenames_from_git_stage, get_file_from_git_stage)

breakpoints_re = map(lambda pat: re.compile(pat), 
    ["import\s+i?pdb", "from\s+i?pdb", "from\s+IPython", "import\s+IPython"]
    )

exit_status = 0
for filename in get_filenames_from_git_stage(".py", deleted=False):
    if checkPath(filename) > 0:
      exit_status = 1
    content = get_file_from_git_stage(filename)
    line_no = 0
    for line in content.split("\n"):
        line_no += 1
        if reduce(lambda a, b: a or b, 
            map(lambda pat: pat.search(line), breakpoints_re)):
            # pdb_import_re.search(line) or pdb_from_re.search(line)
            print "%s:%d: has breakpoint %s" % (filename, line_no, line)
            exit_status = 1
if exit_status == 1:
  print('commit failed')
sys.exit(exit_status)
