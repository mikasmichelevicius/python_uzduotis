import sys
from multipledispatch import dispatch

class Node:
    name: str
    title: str

# Added line for testing

class Database(Node):
    pass

class Table(Node):
    pass

class DataType:
    name: str

class Column(Node):
    dtype: DataType

class Integer(DataType):
    pass

class String(DataType):
    pass

@dispatch(Database, str, str)
def load(node, name, title):
    node.name = name.strip()
    node.title = title.strip()

@dispatch(Table, str, str)
def load(node, name, title):
    node.name = name.strip()
    node.title = title.strip()

@dispatch(Column, str, str, str)
def load(node, name, title, dtype):
    node.name = name.strip()
    node.title = title.strip()
    dtype = dtype.strip()
    if dtype == "integer":
        col_dtype = Integer()
        col_dtype.name = dtype
        node.dtype = col_dtype
    else:
        col_dtype = String()
        col_dtype.name = dtype
        node.dtype = col_dtype

def parse_input(lines):
    table_entries = []

    for line in lines:
        cells = line.split("|")
        len_cells = len(cells)

        if len_cells == 3:
            db_name = cells[0]
            db_title = cells[2]
            db = Database()
            load(db, db_name, db_title)
            table_entries.append(db)
        
        elif len_cells == 4:
            tbl_name = cells[1]
            tbl_title = cells[3]
            tbl = Table()
            load(tbl, tbl_name, tbl_title)
            table_entries.append(tbl)

        else:
            col_name = cells[2]
            col_type = cells[3]
            col_title = cells[4]
            col = Column()
            load(col, col_name, col_title, col_type)
            table_entries.append(col)

    return table_entries

def output_table(table_entries):

    if not table_entries:
        print("database|table|column|type|title")
        return

    title_max = max_length(table_entries, "title")

    db_list = filter(lambda entry: isinstance(entry, Database), table_entries)
    db_max = max_length(db_list, "database")

    tbl_list = filter(lambda entry: isinstance(entry, Table), table_entries)
    tbl_max = max_length(tbl_list, "table")

    col_list = list(filter(lambda entry: isinstance(entry, Column), table_entries))
    col_max = max_length(col_list, "column")

    type_max = max_length(col_list, "type")

    print(f"{'database'.ljust(db_max)}|{'table'.ljust(tbl_max)}|{'column'.ljust(col_max)}|{'type'.ljust(type_max)}|{'title'.ljust(title_max)}")
    for entry in table_entries:
        if isinstance(entry, Database):
            print(f"{entry.name.ljust(db_max)}|{' '.ljust(tbl_max)}|{' '.ljust(col_max)}|{' '.ljust(type_max)}|{entry.title.ljust(title_max)}")
        elif isinstance(entry, Table):
            print(f"{' '.ljust(db_max)}|{entry.name.ljust(tbl_max)}|{' '.ljust(col_max)}|{' '.ljust(type_max)}|{entry.title.ljust(title_max)}")
        elif isinstance(entry, Column): 
            print(f"{' '.ljust(db_max)}|{' '.ljust(tbl_max)}|{entry.name.ljust(col_max)}|{entry.dtype.name.ljust(type_max)}|{entry.title.ljust(title_max)}")

def max_length(entries, column_type):
    if column_type == "database" or column_type == "table" or column_type == "column":
        max_val = max(len(node.name) for node in entries)
        return max(max_val, len(column_type))
    elif column_type == "title":
        max_val = max(len(node.title) for node in entries)
        return max(max_val, len(column_type))
    else:
        max_val = max(len(node.dtype.name) for node in entries)
        return max(max_val, len(column_type))

def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def main():
    lines = read_input(sys.argv[1])
    table_entries = parse_input(lines[1:])
    output_table(table_entries)

if __name__ == "__main__":
    main()
