#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import httplib
import urllib
import sys
import requests
import json

try:
    (scriptname, notification_type, notification_title, notification_text, parameters) = sys.argv
except:
    print "No commandline parameters found"
    sys.exit(1)

## argv[1]:
## Type of notification
##   startup = Startup/Shutdown 🔔
##   download = Added NZB 💾
##   pp = Post-processing started ⏳
##   complete = Job finished ✅
##   failed = Job failed ❌
##   warning = Warning ⚠️
##   error = Error ⛔️
##   disk_full = Disk full ⛔️
##   queue_done = Queue finished ✅
##   new_login = User logged in 🔔
##   other = Other Messages 🔔

## argv[2]: Localized Title

## argv[3]: Job name

def main(argv):

    # These are UTF-8 encoded emojis. In line 2 of this file the UTF-8 
    # encoding is declared.
    
    notification_type = argv[1]
    title = ''
    if notification_type == 'complete':
        title = '[✅]'
    if notification_type == 'queue_done':
        title = '[✅]'
    elif notification_type == 'failed':
        title = '[❌]'
    elif notification_type == 'other':
        title = '[🔔]'
    elif notification_type == 'new_login':
        title = '[🔔]'
    elif notification_body == 'startup':
        title = '[🔔]'
    elif notification_type == 'download':
        title = '[💾]'
    elif notification_type == 'pp':
        title = '[⏳]'
    elif notification_type == 'error':
        title = '[⛔️]'
    elif notification_type == 'disk_full':
        title = '[⛔️]'
    elif notification_type == 'warning':
        title = '[⚠️]'
    else: 
        title = argv[2]
    notification_body = argv[3]
    pushbullet(title,notification_body)
    sys.exit(0)

def pushbullet(title,body):

    # Pushbullet notifications on iOS only display the message title on the lock screen
    # to see the message body on the lock screen we need to put the body and title together
    # and send that string as the title of the message.

    appToken='YOUR_API_TOKEN_HERE'
    lock_screen_message = title + body
    postHeaders = {"Access-Token":appToken,"Content-Type":"application/json"}
    body = {"type":"note","title":lock_screen_message,"body":body,"Content-Type": "application/json"}
    r = requests.post('https://api.pushbullet.com/v2/pushes',data=json.dumps(body),headers=postHeaders)


if __name__ == '__main__':
    main(sys.argv)
    
