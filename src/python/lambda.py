import json
from datetime import datetime
import pytz
import sys

def handler(event, context):
    current_time = datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    return {
        "statusCode": 200,
        "body": json.dumps(f"Hello from Python {python_version} Lambda! Current time: {current_time}")
    }