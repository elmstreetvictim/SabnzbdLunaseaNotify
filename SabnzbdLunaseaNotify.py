#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Enjoy! <3 ElmStreetVictim

import os
import sys
import http.client
import urllib.request, urllib.parse, urllib.error
import sys
import requests
import json

## argv[1]:
## Type of notification, as a string argument
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
    #argv[0] is the script name
    #argv[1] is the type, shown above
    notification_type = argv[1]
    title = ''
    if notification_type == 'complete':
        title = '[✅]'
    elif notification_type == 'queue_done':
        title = '[✅]'
    elif notification_type == 'failed':
        title = '[❌]'
    elif notification_type == 'other':
        title = '[🔔]'
    elif notification_type == 'new_login':
        title = '[🔔]'
    elif notification_type == 'startup':
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
        #failsafe to create a semi-pretty title
        title = '[' + argv[2] + ']'
        
    #argv[3] is the message payload sent by Sabnzbd
    notification_body = argv[3]
    LunaseaNotify(title,notification_body)
    sys.exit(0)

def LunaseaNotify(title,body):
    # iOS will only display the message title on the lock screen
    # to see the message body on the lock screen we need to put the
    # title and body together and send that string as the "title" of the message.
    #similar to : "[✅]Download XYZ Completed"

    device_token="YOUR TOKEN HERE (Leave the quotation marks!)"
    base_url = 'https://notify.lunasea.app/v1/custom/device/'
    full_url = base_url + device_token
    lock_screen_message = title + body
    json_body = {"title":"Sabnzbd Message","body":lock_screen_message}
    r = requests.post(full_url, json = json_body)
    

if __name__ == '__main__':
    main(sys.argv)
    
