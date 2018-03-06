#!/usr/bin/python

###IMPORTANT

### THIS IS NOT A "NOTIFICATION SCRIPT" IN SABNZBD
### THIS IS A "POST PROCESSING SCRIPT"
### AND IT RECEIVES A DIFFERENT GROUP OF ARGUMENTS
### THAN NOTIFICATION SCRIPTS RECEIVE
### PLACE THIS FILE IN THE DIRECTORY WHERE SABNZBD
### SEARCHES FOR SCRIPTS. YOU SET THIS SCRIPT AS
### ACTIVE ON THE 'CATEGORIES' PAGE OF SABNZBD
### IN THE DROPDOWN BOX FOR SCRIPTS

### IMPORTANT

import os
import sys
import httplib
import urllib
import sys
import requests
import json

try:
    (scriptname,directory,orgnzbname,jobname,reportnumber,category,group,postprocstatus,url) = sys.argv
except:
    try:
        # are we testing only?
        directory = sys.argv[1]

    except:
        print "No commandline parameters found"
        sys.exit(1)

## argv[n] - all passed as strings.
## 1    The final directory of the job (full path)
## 2    The original name of the NZB file
## 3    Clean version of the job name (no path info and ".nzb" removed)
## 4    Indexer's report number (if supported)
## 5    User-defined category
## 6    Group that the NZB was posted in e.g. alt.binaries.x
## 7    Status of post processing. 0 = OK, 1=failed verification, 2=failed unpack, 3=1+21
##
## priority: from -2 (lowest) to 2 (highest) (def:0)

def main(argv):
    # Message will include the cleaned up job name
    message = argv[3]
    status = ''
    if argv[7] == '0':
        status = 'Complete'
    elif argv[7] == '1':
        status = 'Failed Verification'
    elif argv[7] == '2':
        status = 'Failed Unpack'
    elif argv[7] == '3':
        status = 'Failed Unpack + Verification'
    else:
        status = 'Failed'

    # Combine the status and the job name, ie.
    # [Complete]Steal This Film 2006 1080p Bluray x264
    pushbullet('[' + status + ']' + message)
    print status
    sys.exit(0)

def pushbullet(stringToPush):
    appToken='YOUR_APP_TOKEN_HERE'
    postHeaders = {"Access-Token":appToken,"Content-Type":"application/json"}
    body = {"type":"note","title":stringToPush,"body":stringToPush,"Content-Type": "application/json"}
    r = requests.post('https://api.pushbullet.com/v2/pushes',data=json.dumps(body),headers=postHeaders)


if __name__ == '__main__':
    main(sys.argv)
    