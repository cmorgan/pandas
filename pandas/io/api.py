"""
Data IO api
"""

from pandas.io.parsers import (read_csv, read_table, read_clipboard,
                               read_fwf, to_clipboard)
from pandas.io.excel import ExcelFile, ExcelWriter, read_excel
from pandas.io.pytables import HDFStore, Term, get_store, read_hdf
from pandas.io.html import read_html
from pandas.io.sql import read_sql
from pandas.io.stata import read_stata
