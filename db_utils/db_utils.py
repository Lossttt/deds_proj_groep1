import pyodbc
import pandas as pd

def create_connection(database_name):
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

def run_query(query, database_name):
    """
    Function to execute SQL query and return results as DataFrame.
    
    Parameters:
    - query: SQL query to execute.
    - database_name: Name of the database to execute the query on.
    
    Returns:
    - df: DataFrame containing query results.
    """
    conn, cursor = create_connection(database_name)
    if "SELECT" in query.upper():
        df = pd.read_sql(query, conn)
        return df
    else:
        cursor.execute(query)
        conn.commit()
