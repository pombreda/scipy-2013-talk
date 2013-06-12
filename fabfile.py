"""
To compile this presentation run

fab pdf
"""

import os
import os.path as osp
import shutil
import sys

from fabric.api import local, settings
from fabric.utils import abort


def requirements():
    with settings(warn_only=True):
        pandoc = local('pandoc --version', capture=True)
        rubber = local('rubber --version', capture=True)

    if pandoc.failed:
        print("pandoc was not found!!. Please install it "
              "from http://code.google.com/p/pandoc/downloads/list")
        abort("ABORTING!!")
    else:
        print('Ok! pandoc is installed \n')

    if rubber.failed:
        if sys.platform.startswith('linux'):
            print("rubber was not found!!. Please install it with")
            print('sudo apt-get install rubber')
            abort("ABORTING!!")
        else:
            print('Ok! rubber is installed')


def pdf():
    # tmp dir for compilation
    if not osp.isdir('tmp'):
        os.mkdir('tmp')

    # From markdown to tex
    local('pandoc talk.md --slide-level 2 -t beamer -o talk.tex')

    # Compiling
    if sys.platform.startswith('linux'):
        local('rubber --into tmp -fd main.tex')
    else:
        shutil.copyfile('main.tex', 'tmp' + osp.sep + 'main.tex')
        shutil.copyfile('talk.tex', 'tmp' + osp.sep + 'talk.tex')
        os.chdir('tmp')
        local('pdflatex main.tex')
        local('pdflatex main.tex')   # Twice the get the TOC
        os.chdir('..')

    # Moving pdf to root
    shutil.copyfile('tmp' + osp.sep + 'main.pdf', 'main.pdf')

