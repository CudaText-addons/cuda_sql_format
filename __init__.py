import sys
import os
import shutil
from cudatext import *
from . import format_proc

sys.path.append(os.path.dirname(__file__))
from . import sqlparse3 as sqlparse

format_proc.MSG = '[SQL Format] '
format_proc.INI = 'cuda_sql_format.py'

def opt():
    ini = format_proc.ini_filename()
    with open(ini) as f:
        text = f.read()
    return eval(text)

def do_format(text):
    return sqlparse.format(text, **opt() )

class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)
