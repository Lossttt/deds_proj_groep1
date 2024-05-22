import pathlib
import pyodbc
import pandas as pd

from dotenv import load_dotenv
import os

dir_path = pathlib.Path(__file__).parent.absolute()
load_dotenv(dotenv_path=dir_path / '.env')

def create_connection():
    try:
        DB = {'servername': os.getenv('DB_SERVERNAME'), 'database': os.getenv('DB_NAME')}
        export_conn = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + DB['servername'] +
            ';DATABASE=' + DB['database'] +
            ';UID=' + os.getenv('DB_USERNAME') +
            ';PWD=' + os.getenv('DB_PASSWORD')
        )
        export_cursor = export_conn.cursor()
        return export_conn, export_cursor
    except pyodbc.Error as e:
        print(f"Error occurred while connecting to the database: {e}")
        return None, None

def create_local_connection(database_name):
    """
    Function to create a connection to the SQL Server database.
    
    Parameters:
    - database_name: Name of the database to connect to.
    
    Returns:
    - conn: Database connection object.
    - cursor: Database cursor object.
    """
    try:
        DB = {'servername': r'AYOUB01\SQLEXPRESS', 'database': database_name}
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')
        cursor = conn.cursor()
        return conn, cursor
    except pyodbc.Error as e:
        print(f"Error occurred while connecting to the database: {e}")
        return None, None

def run_query(query):
    """
    Function to execute SQL query and return results as DataFrame.
    
    Parameters:
    - query: SQL query to execute.
    - database_name: Name of the database to execute the query on.
    
    Returns:
    - df: DataFrame containing query results.
    """
    conn, cursor = create_connection()
    if conn is None:
        return None
    try:
        if "SELECT" in query.upper():
            df = pd.read_sql(query, conn)
            return df
        else:
            cursor.execute(query)
            conn.commit()
            return None
    except pyodbc.Error as e:
        print(f"Error occurred while executing the query: {e}")
        return None

def run_local_query(query, database_name):
    conn, cursor = create_local_connection(database_name)
    if conn is None:
        return None
    try:
        if "SELECT" in query.upper():
            df = pd.read_sql(query, conn)
            return df
        else:
            cursor.execute(query)
            conn.commit()
            return None
    except pyodbc.Error as e:
        print(f"Error occurred while executing the query: {e}")
        return None