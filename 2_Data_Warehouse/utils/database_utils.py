import pathlib
import pyodbc
import pandas as pd

from dotenv import load_dotenv
import os

dir_path = pathlib.Path(__file__).parent.absolute()
load_dotenv(dotenv_path=dir_path / '.env')


def create_connectionLocal(database_name):
    try:
        DB = {'servername': r'HP-SPECTRE\SQLEXPRESS', 'database': database_name}
        export_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')
        export_cursor = export_conn.cursor()
        return export_conn, export_cursor
    except pyodbc.Error as e:
        print(f"Error occurred while connecting to the database: {e}")
        return None, None

def create_connection():
    try:
        DB = {'servername': os.getenv('DB_SERVERNAME'), 'database': os.getenv('DB_NAME')}
        export_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';UID=' + os.getenv('DB_USERNAME') + ';PWD=' + os.getenv('DB_PASSWORD'))
        export_cursor = export_conn.cursor()
        return export_conn, export_cursor
    except pyodbc.Error as e:
        print(f"Error occurred while connecting to the database: {e}")
        return None, None

def run_query(query, database_name):
    conn, cursor = create_connectionLocal(database_name)
    if "SELECT" in query.upper():
        df = pd.read_sql(query, conn)
        return df
    else:
        cursor.execute(query)
        conn.commit()
