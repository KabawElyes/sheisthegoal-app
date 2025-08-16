# db_config.py

import os
import psycopg2
from psycopg2.extras import DictCursor

def connect_db():
    """Connects to the Render Postgres database using the DATABASE_URL."""
    # This correctly gets the variable named 'DATABASE_URL' from the environment
    database_url = os.environ.get('DATABASE_URL')

    if not database_url:
        raise Exception("CRITICAL: DATABASE_URL environment variable is not set.")

    # psycopg2 can connect directly from the URL string provided by Render
    conn = psycopg2.connect(database_url)
    
    # This makes the cursor return dictionaries, so you can access columns by name.
    conn.cursor_factory = DictCursor
    
    return conn