""" Pymode support functions. """

from __future__ import absolute_import

import sys
import vim  # noqa


def auto():
    """ Fix PEP8 erorrs in current buffer. """

    from .autopep8 import fix_file

    class Options(object):
        aggressive = 2
        diff = False
        experimental = True
        ignore = vim.eval('g:pymode_lint_ignore')
        in_place = True
        indent_size = 4 # int(vim.eval('&tabstop'))
        line_range = None
        max_line_length = 79
        pep8_passes = 100
        recursive = False
        select = vim.eval('g:pymode_lint_select')
        verbose = 0

    fix_file(vim.current.buffer.name, Options)


def get_documentation():
    """ Search documentation and append to current buffer. """

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    sys.stdout, _ = StringIO(), sys.stdout
    help(vim.eval('a:word'))
    sys.stdout, out = _, sys.stdout.getvalue()
    vim.current.buffer.append(str(out).splitlines(), 0)
