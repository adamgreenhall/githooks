import re
import subprocess


def execute(*cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out


def files_altered():
    modified = re.compile('^[AM]+\s+(?P<name>.*\.py)', re.MULTILINE)
    files = execute('git', 'status', '--porcelain')
    return modified.findall(files)


def file_contents_old(filename):
    """Get a file content from git at HEAD"""
    return execute("git", "show", ":%s" % filename)


def file_contents(filename):
    # TODO - is this right?
    with open(filename, 'r') as f:
        out = f.read()
    return out


def repo_basedir():
    return execute('git', 'rev-parse', '--show-toplevel').strip()
