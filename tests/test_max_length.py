import pytest
import sys
import os
sys.path.append(os.path.abspath('../'))
from script import Database, Table, Column
from script import load, parse_input, max_length

def test_length_db():
    db_list = []
    db_obj = Database()
    load(db_obj, "  DB  ", "  Database name  ")
    db_list.append(db_obj)
    db_max = max_length(db_list, "database")
    assert db_max == 8

def test_length_tbl():
    tbl_list = []
    tbl_obj = Table()
    load(tbl_obj, "    TAble  ", "  Table name    ")
    tbl_list.append(tbl_obj)
    tbl_max = max_length(tbl_list, "table")
    assert tbl_max == 5

def test_length_col_title_type():
    col_list = []
    col_obj = Column()
    load(col_obj, "  COL20    ", "    Column #20   ", "  integer    ")
    col_list.append(col_obj) 
    col_obj_2 = Column()
    load(col_obj_2, "  COL30    ", "    Column #30   ", "  string    ")
    col_list.append(col_obj_2)
    col_max = max_length(col_list, "column")
    assert col_max == 6

    title_max = max_length(col_list, "title")
    assert title_max == 10

    type_max = max_length(col_list, "type")
    assert type_max == 7


pytest.main()

