import pyodbc
import pandas as pd

def create_connection():
    try:
        DB = {'servername': r'{SERVERNAME}', 'database': r'{DATABASENAME}'}
        export_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')
        export_cursor = export_conn.cursor()
        return export_conn, export_cursor
    except pyodbc.Error as e:
        print(f"Error occurred while connecting to the database: {e}")
        return None, None

def run_query(query):
    conn, cursor = create_connection()
    try:
        if conn is not None and cursor is not None:
            df = pd.read_sql(query, conn)
            return df
        else:
            return None
    except pd.DatabaseError as e:
        print(f"Error occurred while running SQL query: {e}")
        return None
    finally:
        if conn is not None:
            conn.close()
