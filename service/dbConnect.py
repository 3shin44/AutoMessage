from sqlalchemy import create_engine, text
import urllib.parse
from authConfig import authConfig

# 連接DB並執行SQL
def connectDBandRun(SQLTemplate):
    
    # Initialize an empty list to store the result
    result_array = []
    
    # Encode the password
    encoded_password = urllib.parse.quote_plus(authConfig['password'])

    # Create the database URL
    db_url = f"mysql+pymysql://{authConfig['username']}:{encoded_password}@{authConfig['hostname']}:{authConfig['port']}/{authConfig['database_name']}"

    engine = create_engine(db_url)

    # Perform database operations
    try:
        with engine.connect() as conn:
            # Execute queries
            result = conn.execute(text(SQLTemplate))
            rows = result.fetchall()
            for row in rows:
                result_array.append(row)
    finally:
        # The pool is automatically disposed of when the engine is disposed of
        engine.dispose()

    return result_array