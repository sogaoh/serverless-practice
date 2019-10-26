# -*- coding: utf-8 -*-

import os
import json
import urllib.request

import sys; sys.path.append('./functions')
import respond as r


def message_body_post(event, context):
    HOOK_URL = os.environ['HOOK_URL']
    CHANNEL  = os.environ['CHANNEL']

    msg_json = event['msgJson']
    pretty = json.dumps(msg_json['body'], indent=2, ensure_ascii=False)
    message = pretty

    send_data = {
        'channel': CHANNEL,
        'text': message,
    }

    req = urllib.request.Request(
        HOOK_URL,
        data=json.dumps(send_data).encode('utf-8'),
        method='POST'
    )

    try:
        with urllib.request.urlopen(req) as res:
            body = res.read().decode('utf-8')
            #print(body)
            return r.respond(body)
    except urllib.error.HTTPError as err:
        #print(err.code)
        return r.respond('{"err.reason" : "' + err.reason + '"}', err.code)
    except urllib.error.URLError as err:
        #print(err.reason)
        return r.respond('{"err.reason" : "' + err.reason + '"}', 404)
