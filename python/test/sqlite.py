import os
import sqlite3

db_filename = 'todo.db'

schema_table_lists = '''
--save all data, continue modifing
create table residual_error (
    name        text primary key,
    content     text
);
--save changed data, continue adding
create table update_list (
    id          integer primary key autoincrement not null,
    content     text,
    state       bool
);
'''


def create_db(dbName, schemas):

    db_is_new = not os.path.exists(dbName)

    if db_is_new:

        conn = sqlite3.connect(dbName)

        conn.executescript(schemas) 

        conn.close()

    else:

        print 'Database exists, can not create.'

def main():

    create_db(db_filename, schema_table_lists)

if __name__ == '__main__':

    main()


