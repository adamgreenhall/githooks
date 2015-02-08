import re
import git
import pep8 as _pep8
from flake8 import main as _flake8


def pep8():
    # enforce pep8
    pep8style = _pep8.StyleGuide()
    result = pep8style.check_files(git.files_altered())
    passed = result.total_errors == 0
    return passed


def pdb():
    # check for breakpoints
    pat = re.compile('(set_trace\(\)|(import|from)\si?pdb|(import|from)\sIPython)')
    passed = {}
    for fnm in git.files_altered():
        with open(fnm) as f:
            for i, content in enumerate(f.readlines()):
                match = re.findall(pat, content)
                if match:
                    passed[fnm] = False
                    print('{}:{}: breakpoint'.format(fnm, i + 1))

    return all(passed.values())


def flake8(ignore=()):
    # run flake8
    passed = {}
    for fnm in git.files_altered():
        passed[fnm] = _flake8.check_file(fnm, ignore=ignore) == 0
    return all(passed.values())


if __name__ == "__main__":
    pdb()
    flake8()
