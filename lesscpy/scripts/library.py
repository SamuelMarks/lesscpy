# -*- coding: utf8 -*-
"""
.. module:: lesscpy.scripts.library
    CSS/LESSCSS to be run as a library

    http://lesscss.org/#docs

    Copyright (c)
    See LICENSE for details
.. moduleauthor:: Samuel Marks <samuelmarks@gmail.com>
"""

from os import path
from lesscpy.scripts.compiler import run


def compile_less(less):
    """ Takes LESS filename (or path+filename) as input, returns CSS string as output """
    return run(debug=False, dry_run=False, force=False, include=None, lex_only=False,
               min_ending=False, minify=False, no_css=False, out=None, recurse=False,
               scopemap=False, spaces=2, tabs=False, target=less, verbose=False, xminify=False)
