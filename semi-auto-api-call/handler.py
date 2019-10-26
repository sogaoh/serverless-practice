import json
from datetime import datetime, timedelta, timezone


def now(event, context):
    now_utc = datetime.now(timezone.utc)
    now_pdt = datetime.now(timezone(timedelta(hours=-7), 'PDT'))
    now_jst = datetime.now(timezone(timedelta(hours=+9), 'JST'))

    body = {
        "now_utc": now_utc.isoformat(timespec='minutes'),
        "now_pdt": now_pdt.isoformat(timespec='minutes'),
        "now_jst": now_jst.isoformat(timespec='minutes'),
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
