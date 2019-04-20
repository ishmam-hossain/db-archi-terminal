def sqlite3_tables(_cursor):
    _cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return _cursor.fetchall()


def sqlite3_fields(_cursor):
    pass
