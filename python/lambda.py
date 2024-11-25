import json
from datetime import datetime
import pytz
import pandas as pd
import pyarrow as pa

def handler(event, context):
    current_time = datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')
    pandas_version = pd.__version__
    pyarrow_version = pa.__version__
    return {
        "statusCode": 200,
        "body": json.dumps(f"Hello from Python Lambda! Current time: {current_time}. Pandas version: {pandas_version}. PyArrow version: {pyarrow_version}")
    }