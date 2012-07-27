import re
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

    if not flag:
        raise ValueError("Must define at least one file mod flag.")

    file_re = re.compile(r"^[%s]\s+(.+%s)$" % (flag, ext.replace(".", "\.")))
    git = Popen(("git", "status", "--porcelain"), stdout=PIPE)
    stdout, stderr = git.communicate()

    files = []
    for line in stdout:
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
