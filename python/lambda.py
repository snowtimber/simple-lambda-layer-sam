import json
from datetime import datetime
import pytz

def handler(event, context):
    current_time = datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')
    return {
        "statusCode": 200,
        "body": json.dumps(f"Hello from Python Lambda! Current time: {current_time}")
    }