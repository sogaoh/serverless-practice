# -*- coding: utf-8 -*-

import json
from datetime import datetime, timedelta, timezone

from slack import post as n
from functions import respond as r


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


def now_to_slack(event, content):
    notify_param = {'msgJson' : now(None, None)}
    return n.message_body_post(notify_param, None)
