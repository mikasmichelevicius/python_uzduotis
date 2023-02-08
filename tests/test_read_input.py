import pytest
import sys
import os
sys.path.append(os.path.abspath('../'))
from script import Database, Table, Column
from script import load, parse_input, max_length, output_table, read_input

def test_read_input():
    lines = read_input("test_input.txt")
    table = ["database | table | column | type   | title\n", "DB2                       |        | Database name\n", "         | TBL3           |        | Table name\n"]
    assert lines[1] == table[1]
    assert lines[2] == table[2]

pytest.main()

