import pytest
import sys
import os
sys.path.append(os.path.abspath('../'))
from script import Database, Table, Column
from script import load, parse_input

def test_parse_input():
    node_list = []
    db_obj = Database()
    load(db_obj, "  DB  ", "  Database name  ")
    node_list.append(db_obj)

    tbl_obj = Table()
    load(tbl_obj, "    TAble  ", "  Table name    ")
    node_list.append(tbl_obj)

    col_obj = Column()
    load(col_obj, "  COL20    ", "    Column #20   ", "  integer    ")
    node_list.append(col_obj)

    col_obj_2 = Column()
    load(col_obj_2, "  COL30    ", "    Column #30   ", "  string    ")
    node_list.append(col_obj_2)

    lines = ["DB || Database name  ","|TAble||Table name","||COL20|integer|Column #20","||COL30|string|Column #30"] 
    table_entries = parse_input(lines)

    assert (table_entries[0].name, table_entries[0].title) == (db_obj.name, db_obj.title)
    assert (table_entries[1].name, table_entries[1].title) == (tbl_obj.name, tbl_obj.title)
    assert (table_entries[2].name, table_entries[2].dtype.name, table_entries[2].title) == (col_obj.name, col_obj.dtype.name, col_obj.title)
    assert (table_entries[3].name, table_entries[3].dtype.name, table_entries[3].title) == (col_obj_2.name, col_obj_2.dtype.name, col_obj_2.title)
pytest.main()

