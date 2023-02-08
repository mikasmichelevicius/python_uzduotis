import pytest
import sys
import os
sys.path.append(os.path.abspath('../'))
from script import Database, Table, Column
from script import load, parse_input, max_length, output_table

def test_empty_output_table(capsys):
    output_table([])
    stdout, stderr = capsys.readouterr()
    assert stdout == "database|table|column|type|title\n"

def test_output_table(capsys):
    entries_list = []
    db_obj = Database()
    load(db_obj, "  DB  ", "  Database name  ")
    entries_list.append(db_obj)

    tbl_obj = Table()
    load(tbl_obj, "    TAble  ", "  Table name    ")
    entries_list.append(tbl_obj)


    col_obj = Column()
    load(col_obj, "  COL20    ", "    Column #20   ", "  integer    ")
    entries_list.append(col_obj) 

    output_table(entries_list)
    stdout, stderr = capsys.readouterr()

    print(stdout)

    assert stdout == "database|table|column|type   |title        \nDB      |     |      |       |Database name\n        |TAble|      |       |Table name   \n        |     |COL20 |integer|Column #20   \n"


pytest.main()

