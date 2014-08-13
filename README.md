githooks
========
Some git hooks I find useful. These are desinged to keep you from committing:

* code with breakpoints, ``set_trace()``
* code that has invalid statements (invalid syntax or undeclared variables)

pre-requisites
===============
* Install python and pep8
* Put them both on your path
* Clone the ``githooks`` repository (no python/pip install needed, but you do need to keep the directory around)

installing in your code
========================
Symlink githooks to .git/hooks in the repo you want to use githooks in:

    cd ~/my_repo/.git/hooks
    ln -s ~/githooks/* .