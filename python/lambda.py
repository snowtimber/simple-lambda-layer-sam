import json
from datetime import datetime
import pytz
import pandas as pd
import pyarrow as pa

def handler(event, context):
    current_time = datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')
    
    # Create a simple DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Convert to PyArrow Table
    table = pa.Table.from_pandas(df)
    
    return {
        "statusCode": 200,
        "body": json.dumps(f"Hello from Python Lambda! Current time: {current_time}. Created a DataFrame with shape {df.shape} and a PyArrow table with {len(table)} columns.")
    }