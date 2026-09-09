import sqlite3

# connect and cursor


def conn_cursor():
    try:
        conn = sqlite3.connect("main.db")
        cursor = conn.cursor()
        return conn,cursor
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
        return None, None
    except sqlite3.DatabaseError as e:
        print(f"Error : {e}")
        return None, None


# create the table


def create_table(conn, cursor):
    if cursor and conn:
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                age INTEGER              
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS grades(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course TEXT UNIQUE,
                grade INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
            )
            """)

            conn.commit()
            return True
        except sqlite3.OperationalError as e:
            print(f"Error : {e}")
            return False
        except Exception as e:
            print(f"Error : {e}")
            return False


# close the connn


def close_conn(conn):
    if conn:
        conn.close()
        return True
    return False
