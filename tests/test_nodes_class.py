import pytest
import sys
import os
sys.path.append(os.path.abspath('../'))
from script import Database, Table, Column
from script import load

def test_database_class():
    db_obj = Database()
    load(db_obj, "  DB  ", "  Database name  ")
    assert (db_obj.name, db_obj.title) == ("DB", "Database name")

def test_table_class():
    tbl_obj = Table()
    load(tbl_obj, "    TAble  ", "  Table name    ")
    assert (tbl_obj.name, tbl_obj.title) == ("TAble", "Table name")

def test_int_column_class():
    col_obj = Column()
    load(col_obj, "  COL20    ", "    Column #20   ", "  integer    ")
    assert (col_obj.name, col_obj.title, col_obj.dtype.name) == ("COL20", "Column #20", "integer")

def test_str_column_class():
    col_obj = Column()
    load(col_obj, "  COL30    ", "    Column #30   ", "  string    ")
    assert (col_obj.name, col_obj.title, col_obj.dtype.name) == ("COL30", "Column #30", "string")

pytest.main()

